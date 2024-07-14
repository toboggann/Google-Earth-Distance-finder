def createUserList():
    userData = open("u.user")
    userList = []
    for line in userData:
        Field = line.split("|")
        ID = int(Field[0])-1
        userDict = {
           "age":int(Field[1]),
           "gender":Field[2],
           "occupation": Field[3],
           "zip":Field[4].strip("\n")
           }
        userList.append({})
        userList[ID] = userDict
    return userList


def createMovieList():
    f = open('u.item', encoding = "windows-1252")
    movieList = [] 
    for movies in f:
        Information = movies.split('|')
        current = {}
        current['title'] = Information[1]
        current['release date'] = Information[2]
        current['video release date'] = Information[3]
        current['IMDB url'] = Information[4] 
        genreList = []
        i = 1
        while i < len(Information):
            if str(Information[i]).isdigit():
                genreList.append(int(Information[i]))
            i = i + 1
        genreList.append(int(Information[len(Information)-1].replace('\n', '')))
        current['genre'] = genreList
        movieList.append(current)
    return movieList


def readRatings():
    f = open('u.data')
    RatingsTuple = []
    for Ratings in f:
        Information = Ratings.split()
        user = int(Information[0])
        movie = int(Information[1])
        rating = int(Information[2])
        CurrentTuple = (user, movie, rating)
        RatingsTuple.append(CurrentTuple)
    return RatingsTuple


def createGenreList():
    f = open('u.genre')
    GenreList = [] 
    for Genres in f:
        Information = Genres.split('|')
        if Information[0] != '\n':
            GenreList.append(Information[0])
    return GenreList  

def createRatingsDataStructure(numUsers, numItems, ratingTuples):
    Tups = sorted(ratingTuples)
    rLu = []
    rLm = []
    Ratings = {}
    User = 1
    for Tuples in Tups:
        if Tuples[0] == User:
            Ratings[Tuples[1]] = Tuples[2]
        else:
            User = User + 1
            rLu.append(Ratings)
            Ratings = {}
            Ratings[Tuples[1]] = Tuples[2]
    rLu.append(Ratings)
    
    MovieTuples = ratingTuples
    Tups = []
    for x in MovieTuples:
        user = x[0]
        movie = x[1]
        rating = x[2]
        x = (movie, user, rating)
        Tups.append(x)
    movieTups = sorted(Tups)
    movie = 1
    ratings = {}
    for Tuples in movieTups:
        if Tuples[0] == movie:
            Ratings[Tuples[1]] = Tuples[2]
        else:
            movie = movie + 1
            rLm.append(Ratings)
            Ratings = {}
            Ratings[Tuples[1]] = Tuples[2]
    rLm.append(Ratings)
    result = [rLu, rLm]
    return result   
    

def demGenreRatingFractions(userList, movieList, rLu, gender, ageRange, ratingRange):  
    if ageRange[0] == ageRange[1]:
        return [None] * 19    
    ValidRaters = [] 
   
    i = 0 
    for x in userList:
        if ((gender == 'A') or (x['gender'] == gender)) and (x['age'] < ageRange[1]) and (x['age'] >= ageRange[0]):
            ValidRaters.append(i)
        i = i + 1

    Denominator = 0
    for x in ValidRaters:
        Denominator = Denominator + len(rLu[x])
    if Denominator == 0:
        return [None] * 19  
    moviesRated = [] 
   
    for x in ValidRaters:     
        TempList = [] 
        for ValidMovies in rLu[x]:
            TempList = TempList + [ValidMovies]
        moviesRated.append(TempList)
    validMoviesWithRatings = [] 
    i = 0

    while i < len(moviesRated):
        j = 0
        for x in moviesRated[i]:
            if (rLu[ValidRaters[i]][x] <= ratingRange[1]) and (rLu[ValidRaters[i]][x] >= ratingRange[0]):
                validMoviesWithRatings.append(moviesRated[i][j])
            j = j + 1
        i = i + 1
    Genres = [0] * 19 

    for x in validMoviesWithRatings:
        i = 0
        for genreVals in movieList[x-1]['genre']:
            if genreVals == 1:
                Genres[i] = Genres[i] + 1
            i = i + 1
    result = [] 
    for Rate in Genres:
        result.append(Rate/Denominator)
        
    return result




                                                                                         
import matplotlib.pyplot as plt
import numpy as np
# create user, movie, and ratings lists and genre
userList = createUserList()
movieList = createMovieList()
ratingTuples = readRatings()
rLu, rLm = createRatingsDataStructure(len(userList), len(movieList), ratingTuples)
genreList = createGenreList()
#genres
selectedGenres = ["Action", "Comedy", "Drama", "Horror", "Romance"]
# plot fraction of high ratings (4 or 5) for all
fractionsM = demGenreRatingFractions(userList, movieList, rLu, 'M', (0, 100), (4, 5))
fractionsF = demGenreRatingFractions(userList, movieList, rLu, 'F', (0, 100), (4, 5))
colors = ['orange','red']
#bar width and x-positions
barWidth = 0.4
r1 = np.arange(len(selectedGenres))
r2 = [x + barWidth for x in r1]
# Plot bars
for i, genre in enumerate(selectedGenres):
    genreIndex = genreList.index(genre)
    plt.bar(r1[i], fractionsM[genreIndex], color = colors[0], width = barWidth, label='Male' if i == 0 else None)
    plt.bar(r2[i], fractionsF[genreIndex], color = colors[1], width = barWidth, label='Female' if i == 0 else None)
# Set x-axis tick labels
plt.xticks([r + barWidth / 2 for r in range(len(selectedGenres))], selectedGenres)
plt.title(f"High Ratings for All Users")
plt.xlabel("(Genre)")
plt.ylabel("(Fraction of High Ratings)")
plt.legend()
plt.show()
fractionsM = demGenreRatingFractions(userList, movieList, rLu, 'M', (0, 100), (1, 2))
fractionsF = demGenreRatingFractions(userList, movieList, rLu, 'F', (0, 100), (1, 2))
colors = ['orange','red']
# Set bar width and x-positions
barWidth = 0.4
r1 = np.arange(len(selectedGenres))
r2 = [x + barWidth for x in r1]
# Plot bars
for i, genre in enumerate(selectedGenres):
    genreIndex = genreList.index(genre)
    plt.bar(r1[i], fractionsM[genreIndex], color = colors[0], width = barWidth, label='Male' if i == 0 else None)
    plt.bar(r2[i], fractionsF[genreIndex], color = colors[1], width = barWidth, label='Female' if i == 0 else None)
# Set x-axis tick labels
plt.xticks([r + barWidth / 2 for r in range(len(selectedGenres))], selectedGenres)
plt.title(f"Low Ratings for All Users")
plt.xlabel("(Genre)")
plt.ylabel("(Fraction of Low Ratings)")
plt.legend()
plt.show()
#20-30
fractionsM = demGenreRatingFractions(userList, movieList, rLu, 'M', (20, 30), (1, 5))
fractionsF = demGenreRatingFractions(userList, movieList, rLu, 'F', (20, 30), (1, 5))
colors = ['orange','red']
# Set bar width and x-positions
barWidth = 0.4
r1 = np.arange(len(selectedGenres))
r2 = [x + barWidth for x in r1]
# Plot bars
for i, genre in enumerate(selectedGenres):
    genreIndex = genreList.index(genre)
    plt.bar(r1[i], fractionsM[genreIndex], color = colors[0], width = barWidth, label='Male' if i == 0 else None)
    plt.bar(r2[i], fractionsF[genreIndex], color = colors[1], width = barWidth, label='Female' if i == 0 else None)
# Set x-axis tick labels
plt.xticks([r + barWidth / 2 for r in range(len(selectedGenres))], selectedGenres)
plt.title(f"Ratings for 20-30 Year Olds")
plt.xlabel("(Genre)")
plt.ylabel("(Fraction of Ratings)")
plt.legend()
plt.show()
#50-60
fractionsM = demGenreRatingFractions(userList, movieList, rLu, 'M', (50, 60), (1, 5))
fractionsF = demGenreRatingFractions(userList, movieList, rLu, 'F', (50, 60), (1, 5))
colors = ['orange','red']

barWidth = 0.4
r1 = np.arange(len(selectedGenres))
r2 = [x + barWidth for x in r1]

# Plot bars
for i, genre in enumerate(selectedGenres):
    genreIndex = genreList.index(genre)
    plt.bar(r1[i], fractionsM[genreIndex], color = colors[0], width = barWidth, label='Male' if i == 0 else None)
    plt.bar(r2[i], fractionsF[genreIndex], color = colors[1], width = barWidth, label='Female' if i == 0 else None)

plt.xticks([r + barWidth / 2 for r in range(len(selectedGenres))], selectedGenres)
plt.title(f"Ratings for 50-60 Year Olds")
plt.xlabel("(Genre)")
plt.ylabel("(Fraction of Ratings)")
plt.legend()
plt.show()




def randomPrediction(u, m):
    pass

def meanUserRatingPrediction(u, m, rLu):
    pass


def meanMovieRatingPrediction(u, m, rLm):
    pass

def demRatingPrediction(u, m, userList, rLu):
    pass


def genreRatingPrediction(u, m, movieList, rLu):
    pass




















