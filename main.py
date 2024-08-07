
def view_all_movies():
    num_movies = len(movies)
    for name, rating in movies.items():
        print(f"{name}'s rating is {rating}. ")
    if num_movies == 0:
        print("You have no movies")



def view_movie():
    movie = input("What is movie you want to view? ")
    if movie in movies:
        print(f"{movie}'s rating is {movies[movie]}. ")
    else:
        print("This movie isnt in your list!")


def add_movie():
    movie = input("What is the name of the movie? ")
    rating = input("What is the rating? ")
    if movie in movies:
        print(f"You already have {movie}! ")
        return
    movies[movie] = rating
    print(f"Added {movie} to your watched movies")


def update_movie():
    view_all_movies()
    name = input("Enter name of the movie you want to update: ")
    if name in movies:
        rating = input("Enter the new rating: ")
        movies.update({name: rating})
        print("Updated movie rating! ")

    else:
        print(f"{name} isn't on your movie list")



def remove_movie():
    view_all_movies()
    name = input("Enter name of the movie you want to remove: ")
    if name in movies:
        delete_movie = movies.pop(name)
        print(f"Removed {delete_movie} from movie list.")

    else:
        print(f"{name} is already on the movie list")



options = """
    (1) View all watched movies (2) View movie rating 
    (3) Add movie               (4) Update movie rating 
    (5) Remove movie            (6) Exit
"""


movies = {
    "Elemental": 2,
    "Wish" : 10,
    "Everything Everywhere All At Once" : 11,
    "Coco" : 6,
    "Into the SpiderVerse" : 12,
    "A Silent Voice" : 9,
    "The Lorax" : 4,
    "Bad Guys" : 8,
    "Over the Moon" : 7,
    "Puss in Boots 2" : 10
}



while True:
    choice = int(input(options))

    if choice == 1:
        view_all_movies() 
    elif choice == 2:
        view_movie()
    elif choice == 3:
        add_movie() 
    elif choice == 4:
        update_movie()

    elif choice == 5:
        remove_movie()
    elif choice == 6:
        break
    else:
        print(f"{choice} is not a valid option")
