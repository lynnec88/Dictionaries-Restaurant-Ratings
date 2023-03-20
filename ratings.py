"""Restaurant rating lister."""


# put your code here

def process_scores():
    """Read scores file and return dictionary of {restaurant-name: score}."""

    scores_txt= open('scores.txt')
    scores= {}
    for line in scores_txt:
        line = line.rstrip()
        restaurant,score = line.split(":")
        scores[restaurant]= int(score)

    return scores

def add_restaurant(scores):
    """Add a restaurant and rating."""
    
    print("please add your favorite restaurant and rating for them!")
    restaurant =  input ("restaurant name:")
    rating= int(input("rating:"))

    scores[restaurant] = rating

def print_sorted_scores(scores):
    """Print restaurants and ratings, sorted."""
# Print all of the ratings in alphabetical order (including the new one, of course)
    for restaurant , rating in sorted(scores.items()):
        print(f"{restaurant} is rated at {rating}.")

# read existing scores in from scores.txt file
scores = process_scores()

# allow user to add a restaurant/rating pair
add_restaurant(scores)

# print an alphabetical list of all rated restaurants and their ratings
print_sorted_scores(scores)
