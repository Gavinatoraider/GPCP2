import csv

def main():
    movie_list = load_movie_data()
    while True:
        like_to_do = input("""What would you like to do? 
                            1. Search for Movies by Filters
                            2. View Entire Movie List
                            3. Exit
                            Please enter your choice: """)
        
        if like_to_do == "1":
            filters = get_filters()
            results = apply_filters(movie_list, filters)
            if results:
                print(f"\nFound {len(results)} movie(s) matching your criteria:")
                for movie in results:
                    print(f"Title: {movie['Title']}, Genre: {movie['Genre']}, Director: {movie['Director']}, Length: {movie['Length (min)']} mins")
            else:
                print("No movies found matching the provided filters.")
        
        elif like_to_do == "2":
            print_movie_list(movie_list)
        
        elif like_to_do == "3":
            print("Exiting program. Goodbye!")
            break
        else:
            print("Invalid choice, please try again.")

def load_movie_data():
    try:
        with open("Movie Recommender/Movies_list.csv", newline='') as file:
            csv_reader = csv.DictReader(file)
            movie_list = list(csv_reader)
            return movie_list
    except Exception as e:
        print(f"Error opening or reading the CSV file: {e}")
        return []

def get_filters():
    filters = {}

    print("\nWhich filters would you like to apply? (leave blank to skip)")

    title = input("Enter title (e.g., Star Wars): ").strip().lower()
    if title:
        filters['Title'] = title

    genre = input("Enter genre (e.g., Drama, Comedy, Sci-Fi): ").strip().lower()
    if genre:
        filters['Genre'] = genre

    director = input("Enter director (e.g., Steven Spielberg, Christopher Nolan): ").strip().lower()
    if director:
        filters['Director'] = director

    length = input("Enter movie length (in minutes, e.g., 120): ").strip()
    if length.isdigit():
        filters['Length (min)'] = int(length)

    actors = input("Enter actors (e.g., Tom Hanks, Leonardo DiCaprio): ").strip().lower()
    if actors:
        filters['Notable Actors'] = actors

    return filters

def apply_filters(movie_list, filters):
    filtered_movies = movie_list

    for key, value in filters.items():
        if key == 'Length (min)':
            filtered_movies = [movie for movie in filtered_movies if int(movie[key]) == value]
        else:
            filtered_movies = [movie for movie in filtered_movies if value in movie[key].strip().lower()]

    return filtered_movies

def print_movie_list(movie_list):
    print(f"\nPrinting {len(movie_list)} movies in the list:")
    for movie in movie_list:
        print(f"Title: {movie['Title']}, Genre: {movie['Genre']}, Director: {movie['Director']}, Length: {movie['Length (min)']} mins")

# Run the main function
main()
