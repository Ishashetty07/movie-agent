import json
import requests
from pathlib import Path

DATA_FILE = Path("../data/movies.json")
API_URL = "https://ghibliapi.vercel.app/films"


def load_movies():
    if DATA_FILE.exists():
        with open(DATA_FILE, "r") as file:
            return json.load(file)
    return []


def save_movies(movies):
    with open(DATA_FILE, "w") as file:
        json.dump(movies, file, indent=4)


def add_movie(title, genre, rating):
    movies = load_movies()
    movies.append({
        "title": title,
        "genre": genre,
        "rating": rating
    })
    save_movies(movies)
    print("✅ Movie added successfully!")


def list_movies():
    movies = load_movies()
    if not movies:
        print("No movies found.")
        return
    for movie in movies:
        print(f"{movie['title']} | {movie['genre']} | ⭐ {movie['rating']}")


def search_by_genre(genre):
    movies = load_movies()
    results = [m for m in movies if m["genre"].lower() == genre.lower()]
    for movie in results:
        print(movie["title"])


def recommend_by_rating(min_rating):
    movies = load_movies()
    for movie in movies:
        if movie["rating"] >= min_rating:
            print(movie["title"])


def fetch_movies_from_api():
    response = requests.get(API_URL)
    films = response.json()
    for film in films:
        print(f"{film['title']} ({film['release_date']})")


def menu():
    while True:
        print("\n🎬 Movie Assistant")
        print("1. Add Movie")
        print("2. List Movies")
        print("3. Search by Genre")
        print("4. Recommend by Rating")
        print("5. Fetch Movies from API")
        print("6. Exit")

        choice = input("Choose option: ")

        if choice == "1":
            title = input("Title: ")
            genre = input("Genre: ")
            rating = float(input("Rating (1-10): "))
            add_movie(title, genre, rating)

        elif choice == "2":
            list_movies()

        elif choice == "3":
            genre = input("Genre: ")
            search_by_genre(genre)

        elif choice == "4":
            rating = float(input("Minimum Rating: "))
            recommend_by_rating(rating)

        elif choice == "5":
            fetch_movies_from_api()

        elif choice == "6":
            break

        else:
            print("Invalid choice!")


if __name__ == "__main__":
    menu()
