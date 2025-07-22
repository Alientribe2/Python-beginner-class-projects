import csv
# imports movie data into the program file

list_of_stuff = []
# the main list used for the movie data

def read_data(file_name):
    with open(file_name, newline="") as csvfile:
        reader = csv.reader(csvfile)
        # Skip the header row if it exists
        next(reader, None)
        for row in reader:
            list_of_stuff.append(row)
# this function makes sure to open the csv file and read it, appending it to the main list

action_movies = read_data("action.csv")
# defines wchich csv file that the program will access

def find_highest_rated(list_of_stuff):
    highest_rating = 0
    highest_rated_movie = None
    for movie in list_of_stuff:
        try:
            if movie[6].strip():
                rating = float(movie[6])
            if rating > highest_rating:
                highest_rating = rating
                highest_rated_movie = movie
        except:
            continue

    print(highest_rated_movie[1])
    print(highest_rating)
# finds the movie with the highest rating in the entire list

def average(list_of_stuff):
    ratings = []
    for movie in list_of_stuff:
        try:
            rating = float(movie[6])
            ratings.append(rating)
        except:
            continue
    if len(ratings) > 0:
        print("the average rating is: ", sum(ratings) / len(ratings))
    else:
        print("Why aren't there ratings!?!?!?!?!?!?!?!?!!?!?!!?!?!?!?!?!?!??!?!?!?!?!?")
# Finds the average rating across the entire csv file

def filter(list_of_stuff):
    genre = input("type a genre to look for: ")
    found = False
    for movie in list_of_stuff:
        if genre.lower() in movie[5].lower():
            print("Title:", movie[1])
            print("Genres:", movie[5])
            print("Rating:", movie[6])
            found = True
    if not found:
        print("That Genre is no good, we dont have movies of that genre here.")


while True:

    print("Welcome to the movie reccomendation program")
    random1 = input(
        "This program was built to help recomend movies to it's users. Press enter to continue: "
    )
    random2 = input(
        "This program features a curated list of movies, genres, and ratings. Press enter to continue: "
    )
    random3 = input(
        "This program is built to help you find movies that you might like based on societal preferences. Press enter to continue: "
    )
    print(
        "You can find the Highest rated movie, the average rating of all movies in the database, or you can filter movies by genre."
    )
    selection = input(
        "To find the highest rated movie, type 'highest rated', to find the average rating type 'average', and to filter movies by genre type 'filter': "
    )

    if selection.lower() == "highest rated":
        find_highest_rated(list_of_stuff)
    elif selection.lower() == "average":
        average(list_of_stuff)
    elif selection.lower() == "filter":
        filter(list_of_stuff)
    else:
        print("Something went wrong, please try again.")
    terminate = input("If you want to keep going, type 'yes'. If not type 'no'.")
    if terminate.lower() == "yes":
        print("Restarting....")
    elif terminate.lower() == "no":
        print("Program Terminated.")
        break
