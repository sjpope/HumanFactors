import json
import statistics
from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

def get_default_user():
    return User.objects.get_or_create(username='default_user')[0].id

class Category(models.Model):
    category_text = models.CharField(max_length=50)

    def __str__(self):
        return self.category_text

class Restaurant(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE)

    name = models.CharField(max_length=255)
    
    address = models.CharField(max_length=1024, default='Unknown Address')
    location = models.CharField(max_length=500)
    latitude = models.DecimalField(max_digits=9, decimal_places=6, null=True, blank=True)
    longitude = models.DecimalField(max_digits=9, decimal_places=6, null=True, blank=True)
    
    cuisine_type = models.CharField(max_length=100)
    health_rating = models.DecimalField(max_digits=2, decimal_places=1)
    price_level = models.IntegerField()
    
    hours_of_operation = models.TextField(null=True, blank=True)
    
    def get_hours(self):
        return json.loads(self.hours_of_operation)
    
    def __str__(self):
        return self.name
    
    def review_amount(self):
        return self.review_set.count()

    def rating(self):
        if not self.review_set.exists():
            return 0
        ratings = [review.rating for review in self.review_set.all()]
        return round(statistics.mean(ratings), 1) if ratings else 0

    def pricing(self):
        if not self.review_set.exists():
            return 0
        prices = [review.price for review in self.review_set.all()]
        return round(statistics.mean(prices), 1) if prices else 0
    
class Review(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='reviews')
    restaurant = models.ForeignKey(Restaurant, on_delete=models.CASCADE, related_name='reviews')
    rating = models.IntegerField(default=0)
    price = models.IntegerField(default=0)
    title = models.CharField(max_length=100)
    description = models.TextField(max_length=500)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.description
    
class Comment(models.Model):
    review = models.ForeignKey(Review, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    description = models.TextField(max_length=500)

    def __str__(self):
        return self.description

class Reply(models.Model):
    comment = models.ForeignKey(Comment, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    description = models.TextField(max_length=500)

    def __str__(self):
        return self.description

class Like(models.Model):
    review = models.ForeignKey(Review, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return f'Review: {self.review.id}, User: {self.user.username}'

class DiningProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    preferences = models.TextField()
    allergies = models.TextField()
    favorite_cuisines = models.TextField()
    desired_dining_experiences = models.TextField()

    def __str__(self):
        return f'{self.user.username} Profile'

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    profile_picture = models.ImageField(upload_to='profile_pics', blank=True)
    dining_preferences = models.TextField(blank=True)

    def __str__(self):
        return self.user.username
    

class MenuItem(models.Model):
    restaurant = models.ForeignKey(Restaurant, on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    description = models.TextField()
    price = models.DecimalField(max_digits=5, decimal_places=2)

    def __str__(self):
        return self.name

class ReservationSlot(models.Model):
    #     user = models.ForeignKey(User, on_delete=models.CASCADE, default=get_default_user)

    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    restaurant = models.ForeignKey(Restaurant, on_delete=models.CASCADE)
    date_time = models.DateTimeField()

    def __str__(self):
        return f"{self.restaurant.name} - {self.date_time}"


@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        DiningProfile.objects.create(user=instance)

@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.diningprofile.save()