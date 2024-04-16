from sklearn.metrics.pairwise import cosine_similarity

from surprise import SVD, Dataset, Reader
from surprise.model_selection import cross_validate
import numpy as np

from django.contrib.auth.models import User
from .models import *

def get_collaborative_filtering_recommendations(user, N=3):
    
    reviews = Review.objects.all().values_list('user_id', 'restaurant_id', 'rating')
    reader = Reader(rating_scale=(1, 5))
    data = Dataset.load_from_df(reviews, reader)
    
    algo = SVD()
    training_set = data.build_full_trainset()
    algo.fit(training_set)
    
    test_set = training_set.build_anti_testset()
    predictions = algo.test(test_set)
    
    user_predictions = [pred for pred in predictions if pred.uid == user.id]
    
    user_predictions.sort(key=lambda x: x.est, reverse=True)
    top_N = user_predictions[:N]
    return [pred.iid for pred in top_N]  

def get_content_based_recommendations(user_profile, all_restaurants):
    try:
        user_vector = profile_to_vector(user_profile)
        restaurant_vectors = [profile_to_vector(restaurant) for restaurant in all_restaurants]
        
        similarity_scores = cosine_similarity([user_vector], restaurant_vectors).flatten()
        top_indices = np.argsort(similarity_scores)[-3:]
        return [all_restaurants[i] for i in reversed(top_indices)]
    except Exception as e:
        print(f"Error in content-based recommendation: {e}")
        return []

def profile_to_vector(profile):
    vector = [len(profile.preferences), len(profile.allergies), len(profile.favorite_cuisines), len(profile.desired_dining_experiences)]
    return vector 

def compute_similarity(user1, user2):
    return np.dot(profile_to_vector(user1.diningprofile), profile_to_vector(user2.diningprofile))

def get_recommendations(user_id):
    user = User.objects.get(id=user_id)
    if not user.diningprofile:
        return []
    return get_content_based_recommendations(user.diningprofile, Restaurant.objects.all())