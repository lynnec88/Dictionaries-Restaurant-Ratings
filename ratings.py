"""Restaurant rating lister."""


# put your code here

def process_scores():
    scores_txt= open('scores.txt')
    scores= {}
    for line in scores_txt:
        line = line.rstrip()
        restaurant,score = line.split(":")
        scores[restaurant]= int(score)

    return scores

def add_restaurant(scores):
    print("please add your favorite restaurant and rating for them!")
    restaurant =  input ("restaurant name:")
    rating= int(input("rating:"))

    scores[restaurant] = rating

def print_sorted_scores(scores):
# Print all of the ratings in alphabetical order (including the new one, of course)
    for restaurant , rating in sorted(scores.items()):
        print(f"{restaurant} is rated at {rating}.")


scores = process_scores()
add_restaurant(scores)
print_sorted_scores(scores)
