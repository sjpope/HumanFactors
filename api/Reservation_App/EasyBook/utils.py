from sklearn.metrics.pairwise import cosine_similarity

from surprise import SVD, Dataset, Reader
from surprise.model_selection import cross_validate

from .models import *

def get_collaborative_filtering_recommendations(user):
    
    # Load dataset from Review (model)
    reviews = Review.objects.all().values_list('user_id', 'restaurant_id', 'rating')
    reader = Reader(rating_scale=(1, 5))
    data = Dataset.load_from_df(reviews, reader)
    
    # Matrix factorization (SVD algo)
    algo = SVD()
    training_set = data.build_full_trainset()
    algo.fit(training_set)
    
    # Predict ratings for all pairs (user, items) not in training set
    test_set = training_set.build_anti_testset()
    predictions = algo.test(test_set)
    
    # Filter predictions 4 given user
    user_predictions = [pred for pred in predictions if pred.uid == user.id]
    
    # Sort predictions by estimated rating
    N = 3
    user_predictions.sort(key=lambda x: x.est, reverse=True)
    top_N = user_predictions[:N]
    return [pred.iid for pred in top_N]  # return restaurant_ids

def get_content_based_recommendations(user_profile, all_restaurants):
    
    # Convert to vectors
    user_vector = profile_to_vector(user_profile)
    restaurant_vectors = [profile_to_vector(restaurant) for restaurant in all_restaurants]
    
    # Compute cosine similarity between user and all restaurants
    similarity_scores = cosine_similarity([user_vector], restaurant_vectors)
    
    N = 3
    top_indices = similarity_scores.argsort()[0][-N:] # Sort scores, return top (N) recommendations
    return [all_restaurants[i] for i in top_indices]

def profile_to_vector(profile):
    
    vector = []
    # Convert profile, features into vector<float>() 
    return vector

def compute_similarity(user1, user2):
    # compares user profiles, preferences, and review/rating history.
    # cosine similarity matrix??
    pass

def get_recommendations(user):
    # use the similarity scores between users to suggest restaurants.
    pass