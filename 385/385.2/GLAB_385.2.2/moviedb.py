# Movie DB Dictionary Project

# Movie Database
from logging import exception
from turtle import title


movie_db = {}

# Add a movie
def add_movie():
    # Got data from user and saved into variables
    title = input('Enter the movie title: ')
    year = input('Enter the movie year: ')
    genre = input('Enter the movie genre: ')
    director = input('Enter the movie director: ')
    actors = input('Enter the name of actors(comma separated): ')

    # Used data to create a movie in the database
    movie_db[title] = {
        'year': year,
        'genre': genre,
        'director': director,
        'actors': actors.split(",")
    }

    print(f'🎉 Success: {title} added!' )

# Edit a movie
def edit_movie():
    try:
        # find movie to edit
        if title not in movie_db:
        # if can't find movie keyerror
        raise KeyError(f'Movie {title} not found in database.')
        # show current info
        print(f'Current info for {title}:')
        print(movie_db[title])

        # collect updated info from user
        year = input('Enter the movie year (or press enter to keep current value(s)): ')
        genre = input('Enter the movie genre (or press enter to keep current value(s)): ')
        director = input('Enter the movie director (or press enter to keep current value(s)): ')
        actors = input('Enter the name of actors(comma separated) (or press enter to keep current value(s)): ')

        # update with new information
        # canother datatype than booleans evaluate to true or false 
        if year:
            movie_db[title]['year'] = year
        if genre:
            movie_db[title]['genre'] = genre
        if director:
            movie_db[title]['director'] = director
        if actors:
            movie_db[title]['actors'] = actors.split(",")

        print(f'✅ {title} has been updated.')
    except exception as e:
        print(f'❌ Error: {e}') 

# Delete a movie
# declare delete_movie() function
# ask the user for the movie to be deleted
# error handle if the movie doesn't exist 
# if movie exists, delete from db and print

# Delete a movie
# declare delete_movie() function
def del_movie():
    # ask the user for the movie to be deleted
    title = input('Enter movie title to delete: ')

    try:
        if title not in movie_db:
            raise KeyError(f'{title} not in database')

        del movie_db[title]

        print(f'🎉 Success. {title} deleted!')
    # if movie exists, delete from db and print success!
    except Exception as e:
        print(f'❌ Error: {e}')
    # error handle if the movie doesnt exists 


# View all movies
def show_all():
    print('⭐️ All movies in Database ⭐️')
    print('===============')
    for movie in movie_db:
        print(f"Movie: {movie}")
        for key, value in movie_db[movie].items():
            print(f"{key}: {value}")
        print('===============')

# Search Movies

# Define a search function
def search_movies():
    # Prompted the user for search criteria
    print('🔎 Search Movies in DB')
    criteria = input('Enter search criteria: ')
    matches = [] # memory allocation for matching movies
    ["Dark Knight", 'Spirited Away', 'Forest Gump']

    # Loop through my db to find matches
    for movie, info in movie_db.items():
        # use control flow statement with membership operator to find matches
        if criteria in movie or criteria in info['director'] or criteria in info['actors'] or criteria in info['genre']:
            matches.append(movie) # Add title to list of found movie

    # if movie(s) found
    if matches:
        print('Matches Found:')
        for movie in matches: # looping over movie titles, dict[key]
            print(f'{movie}: {movie_db[movie]}')
    # else no movies found
    else:
        print('❌ No matches found.')

# Save data
def save_data():
    # ask name filename to create
    filename = input('Enter the filename to save to: ')
    # open file, 'w' mode, put in 'f' variable
    with open(f'data/{filename}.json', 'w') as f:
        # Dump data into external file
        json.dump(movie_db, f)
    print('🎉 Success, Data Saved!')

# load movie - pull previews database file into this program

# define load_data function
    # ask user where to import file from
    # try to open the file
        # save file contents to temp database in app.
    #print success message
def load_data():
    filename = input('Enter the filename to load: ')

    with open(f'data/{filename}.json', 'r') as f:
        data = json.load(f)

        global movie_db
        movie_db = data

    print('🎉 Data loaded successfully')


# We have to find a way, to repeatly ask the user what action they want to take
while True:
    print('==== 🎬 Movie Database MGMT System 🎬 ====')
    print('1. Exit')
    print('2. Add Movie')
    print('3. Show All Movies')
    print('4. Edit Existing Movie')
    print('5. Delete a Movie')
    print('6. Search for a Movie')
    print('7. Save data to a file')
    print('8. Load data from a file')

    choice = input('What do you want to do? ')

    if choice == '1':
        print('👋 Goodbye. Comeback soon!')
        break
    elif choice == '2':
        add_movie()
    elif choice == '3':
        show_all()
    elif choice == '4':
        edit_movie()
    elif choice == '5':
        del_movie()
    elif choice == '6':
        print('Searching for movie')
    elif choice == '7':
        print('Saving data to file')
    elif choice == '8':
        print('Loading data from file')
    else:
        print('❌ Invalid Option. Please try again.')
