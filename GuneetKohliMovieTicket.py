# GuneetKohliMovieTicket.py
#Guneet Kohli, Date: 02.14.2024. IS 601004
# Movie information stored in a list of dictionaries
movies = [
    {"title": "Avengers: Endgame", "genre": "Action", "price": 20, "available_tickets": 50},
    {"title": "The Lion King", "genre": "Animation", "price": 15, "available_tickets": 30},
    {"title": "John Wick 3", "genre": "Action", "price": 18, "available_tickets": 25},
    {"title": "Toy Story 4", "genre": "Animation", "price": 12, "available_tickets": 40},
    {"title": "Joker", "genre": "Thriller", "price": 16, "available_tickets": 20}
]

# Welcome message and get user name
name = input("Welcome to the Movie Booker! What's your first name? ")
last_name = input("And your last name? ")
print(f"Hello, {name} {last_name}! Let's find you a movie to watch.")

# Display movie options
print("\nAvailable movies:")
for i, movie in enumerate(movies, 1):
    print(f"{i}. {movie['title']} ({movie['genre']}) - ${movie['price']}")

# Get user's choice and validate
while True:
    chosen_movie_index = input("\nEnter the number of the movie you want to watch: ")
    if chosen_movie_index.isdigit() and 0 < int(chosen_movie_index) <= len(movies):
        chosen_movie = movies[int(chosen_movie_index) - 1]
        break
    else:
        print("Invalid input. Please enter the number corresponding to the movie.")

# Display movie details and get number of tickets
print(f"\nYou chose '{chosen_movie['title']}' ({chosen_movie['genre']}) - ${chosen_movie['price']}")
num_tickets = int(input("How many tickets would you like to purchase? "))

# Check ticket availability and calculate total price
if num_tickets <= chosen_movie["available_tickets"]:
    chosen_movie["available_tickets"] -= num_tickets  # Update available tickets
    # Coupon code feature
    coupon_code = input("Do you have a coupon code? If yes, enter it here (otherwise, press Enter): ")
    discount_rate = 0
    if coupon_code == "5OFF":
        discount_rate = 0.05
    elif coupon_code == "10OFF":
        discount_rate = 0.10
    elif coupon_code == "15OFF":
        discount_rate = 0.15
    
    total_price = num_tickets * chosen_movie["price"] * (1 - discount_rate) # Apply discount if applicable
    print(f"\nCongratulations! You purchased {num_tickets} tickets for '{chosen_movie['title']}' at a total of ${total_price}.")
else:
    print(f"Sorry, only {chosen_movie['available_tickets']} tickets are available for '{chosen_movie['title']}'.")
    # Offer to choose a different number or movie

# Thank you message
print(f"\nThank you, {name} {last_name}, for using Movie Booker. Enjoy the movie!")