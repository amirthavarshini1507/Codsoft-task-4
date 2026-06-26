
# ADVANCED RECOMMENDATION SYSTEM

# Developed by Amirtha

import random

class RecommendationSystem:

    def __init__(self):

        self.movies = [
            {
                "title": "Inception",
                "genre": "Sci-Fi",
                "year": 2010,
                "rating": 9.0
            },
            {
                "title": "Interstellar",
                "genre": "Sci-Fi",
                "year": 2014,
                "rating": 9.2
            },
            {
                "title": "The Dark Knight",
                "genre": "Action",
                "year": 2008,
                "rating": 9.5
            },
            {
                "title": "Avengers Endgame",
                "genre": "Action",
                "year": 2019,
                "rating": 8.8
            },
            {
                "title": "Titanic",
                "genre": "Romance",
                "year": 1997,
                "rating": 8.6
            },
            {
                "title": "The Notebook",
                "genre": "Romance",
                "year": 2004,
                "rating": 8.4
            },
            {
                "title": "Coco",
                "genre": "Animation",
                "year": 2017,
                "rating": 8.9
            },
            {
                "title": "Toy Story",
                "genre": "Animation",
                "year": 1995,
                "rating": 8.7
            },
            {
                "title": "The Conjuring",
                "genre": "Horror",
                "year": 2013,
                "rating": 8.3
            },
            {
                "title": "A Quiet Place",
                "genre": "Horror",
                "year": 2018,
                "rating": 8.1
            }
        ]

        self.user_history = []

    def display_movies(self):

        print("\nAVAILABLE MOVIES")
        print("-" * 60)

        for index, movie in enumerate(self.movies, start=1):
            print(
                f"{index}. {movie['title']} | "
                f"{movie['genre']} | "
                f"{movie['year']} | "
                f"⭐ {movie['rating']}"
            )

    def search_movie(self):

        keyword = input("\nEnter movie name: ").lower()

        found = False

        for movie in self.movies:
            if keyword in movie["title"].lower():
                print("\nMovie Found")
                print(movie)
                found = True

        if not found:
            print("Movie not found.")

    def rate_movie(self):

        self.display_movies()

        try:
            choice = int(input("\nSelect movie number: "))
            user_rating = float(input("Your rating (1-10): "))

            selected_movie = self.movies[choice - 1]

            self.user_history.append({
                "title": selected_movie["title"],
                "genre": selected_movie["genre"],
                "rating": user_rating
            })

            print("Rating Saved Successfully!")

        except:
            print("Invalid Input!")

    def recommend_movies(self):

        if not self.user_history:
            print("\nNo ratings found.")
            print("Showing Top Rated Movies...\n")

            top_movies = sorted(
                self.movies,
                key=lambda x: x["rating"],
                reverse=True
            )

            for movie in top_movies[:5]:
                print(
                    f"{movie['title']} "
                    f"({movie['genre']}) "
                    f"⭐ {movie['rating']}"
                )

            return

        favorite_genres = {}

        for item in self.user_history:
            genre = item["genre"]

            if genre not in favorite_genres:
                favorite_genres[genre] = 0

            favorite_genres[genre] += item["rating"]

        best_genre = max(
            favorite_genres,
            key=favorite_genres.get
        )

        recommendations = []

        for movie in self.movies:
            if movie["genre"] == best_genre:
                recommendations.append(movie)

        recommendations.sort(
            key=lambda x: x["rating"],
            reverse=True
        )

        print("\nPERSONALIZED RECOMMENDATIONS")
        print("-" * 60)

        for movie in recommendations:
            print(
                f"{movie['title']} | "
                f"{movie['genre']} | "
                f"⭐ {movie['rating']}"
            )

    def analytics(self):

        print("\nUSER ANALYTICS")
        print("-" * 60)

        if not self.user_history:
            print("No user activity available.")
            return

        total_ratings = len(self.user_history)

        average_rating = sum(
            item["rating"]
            for item in self.user_history
        ) / total_ratings

        print(f"Movies Rated : {total_ratings}")
        print(f"Average Rating : {average_rating:.2f}")

        genres = {}

        for item in self.user_history:

            if item["genre"] not in genres:
                genres[item["genre"]] = 0

            genres[item["genre"]] += 1

        print("\nFavorite Genres:")

        for genre, count in genres.items():
            print(f"{genre} -> {count}")

    def surprise_recommendation(self):

        movie = random.choice(self.movies)

        print("\nSURPRISE PICK")
        print("-" * 60)
        print(
            f"{movie['title']} | "
            f"{movie['genre']} | "
            f"⭐ {movie['rating']}"
        )

    def run(self):

        while True:

            print("\n")
            print("=" * 60)
            print("ADVANCED MOVIE RECOMMENDATION SYSTEM")
            print("=" * 60)

            print("1. View Movies")
            print("2. Search Movie")
            print("3. Rate Movie")
            print("4. Get Recommendations")
            print("5. User Analytics")
            print("6. Surprise Pick")
            print("7. Exit")

            choice = input("\nEnter Choice: ")

            if choice == "1":
                self.display_movies()

            elif choice == "2":
                self.search_movie()

            elif choice == "3":
                self.rate_movie()

            elif choice == "4":
                self.recommend_movies()

            elif choice == "5":
                self.analytics()

            elif choice == "6":
                self.surprise_recommendation()

            elif choice == "7":
                print("\nThank You For Using The System!")
                break

            else:
                print("Invalid Choice!")

system = RecommendationSystem()
system.run()