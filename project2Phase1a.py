#import matplotlib as plt



#make a userlist data Structure that is a dictionary
def createUserList():
    userData = open("/Users/thomas/Desktop/Cs 1/Phases/phase 2/u.user")
    userList = []
    for line in userData:
        fields = line.split("|")
        ID = int(fields[0])-1
        userDict = {
           "age":int(fields[1]),
           "gender":fields[2],
           "occupation": fields[3],
           "zip":fields[4].strip("\n")
           }
        userList.append({})
        userList[ID] = userDict
    return userList


#make a movie List containing all the movies given in the file
#“title”, “release date”, “video release date”, “IMDB url”, and “genre”
#Note that the value associated with the key “genre” is
#a length-19 list of zeroes and ones.
def createMovieList():
    f = open('/Users/thomas/Desktop/Cs 1/Phases/phase 2/u.item', encoding = "windows-1252")
    movieList = [] 
    for movies in f:
        info = movies.split('|')
        current = {}
        current['title'] = info[1]
        current['release date'] = info[2]
        current['video release date'] = info[3]
        current['IMDB url'] = info[4] 
        genreList = []
        i = 1
        while i < len(info):
            if str(info[i]).isdigit():
                genreList.append(int(info[i]))
            i += 1
        genreList.append(int(info[len(info)-1].replace('\n', '')))
        current['genre'] = genreList
        movieList.append(current)
    return movieList


def readRatings():
    f = open('/Users/thomas/Desktop/Cs 1/Phases/phase 2/u.data')
    ratingTuples = []
    for ratings in f:
        info = ratings.split()
        user = int(info[0])
        movie = int(info[1])
        rating = int(info[2])
        currentTuple = (user, movie, rating)
        ratingTuples.append(currentTuple)
    return ratingTuples


def createGenreList():
    f = open('/Users/thomas/Desktop/Cs 1/Phases/phase 2/u.genre')
    genreList = [] 
    for genres in f:
        info = genres.split('|')
        if info[0] != '\n':
            genreList.append(info[0])
    return genreList  

def createRatingsDataStructure(numUsers, numItems, ratingTuples):
    Tups = sorted(ratingTuples)
    rLu = []
    rLm = []
    ratings = {}
    user = 1
    for tuples in Tups:
        if tuples[0] == user:
            ratings[tuples[1]] = tuples[2]
        else:
            user += 1
            rLu.append(ratings)
            ratings = {}
            ratings[tuples[1]] = tuples[2]
    rLu.append(ratings)
    
    movieTuples = ratingTuples
    Tups = []
    for x in movieTuples:
        user = x[0]
        movie = x[1]
        rating = x[2]
        x = (movie, user, rating)
        Tups.append(x)
    movieTups = sorted(Tups)
    movie = 1
    ratings = {}
    for tuples in movieTups:
        if tuples[0] == movie:
            ratings[tuples[1]] = tuples[2]
        else:
            movie += 1
            rLm.append(ratings)
            ratings = {}
            ratings[tuples[1]] = tuples[2]
    rLm.append(ratings)
    res = [rLu, rLm]
    return res   
    

def demGenreRatingFractions(userList, movieList, rLu, gender, ageRange, ratingRange):  
    if ageRange[0] == ageRange[1]:
        return [None] * 19    
    validRaters = [] 
   
    i = 0 
    for x in userList:
        if ((gender == 'A') or (x['gender'] == gender)) and (x['age'] < ageRange[1]) and (x['age'] >= ageRange[0]):
            validRaters.append(i)
        i += 1

    denom = 0
    for x in validRaters:
        denom += len(rLu[x])
    if denom == 0:
        return [None] * 19  
    moviesRated = [] 
   
    for x in validRaters:     
        yuh = [] 
        for validMovies in rLu[x]:
            yuh += [validMovies]
        moviesRated.append(yuh)
    validMoviesWithRatings = [] 
    i = 0

    while i < len(moviesRated):
        j = 0
        for x in moviesRated[i]:
            if (rLu[validRaters[i]][x] <= ratingRange[1]) and (rLu[validRaters[i]][x] >= ratingRange[0]):
                validMoviesWithRatings.append(moviesRated[i][j])
            j += 1
        i += 1
    genres = [0] * 19 

    for x in validMoviesWithRatings:
        i = 0
        for genreVals in movieList[x-1]['genre']:
            if genreVals == 1:
                genres[i] += 1
            i += 1
    res = [] 
    for idk in genres:
        res.append(idk/denom)
        
    return res



userList = createUserList()
movieList = createMovieList()
rawRatings = readRatings()
numUsers = len(userList)
numMovies = len(movieList)
[rLu, rLm] = createRatingsDataStructure(numUsers, numMovies, rawRatings)
genreList = createGenreList()
'''
def add_to_all_elements_in_list(list1, val):
    return [elem+val for elem in list1]

def plot_grouped_bar_chart(data, label_tuple, title, ylabel):
    x = [val for val in range(len(label_tuple))] # the label locations
    width = 1/(len(data)+1) # the width of the bars
    multiplier = 0
    fig, ax = plt.subplots()
    for attribute, measurement in data.items():
        offset = width * multiplier
        rects = ax.bar(add_to_all_elements_in_list(x, offset), measurement, width, label=attribute)
        multiplier += 1
    # Add some text for labels, title and custom x-axis tick labels, etc.
    ax.set_ylabel(ylabel)
    ax.set_title(title)
    ax.set_xticks(add_to_all_elements_in_list(x, width), label_tuple)
    # ax.legend(loc='upper left', ncols=3)
    ax.legend(loc='best')
    # ax.set_ylim(0, 250)
    y_max = max([max(v) for k,v in data.items()])
    ax.set_ylim(0, y_max*1.2)
    plt.show()

# -------------------------------------------------
# Given Data
label_tuple = ("Adelie", "Chinstrap", "Gentoo")
data = {
    'Bill Depth': (18.35, 18.43, 14.98),
    'Bill Length': (38.79, 48.83, 47.50),
    'Flipper Length': (189.95, 195.82, 217.19),
}
title='Penguin attributes by label_tuple'
ylabel='Length (mm)'
plot_grouped_bar_chart(data, label_tuple, title, ylabel)

# -------------------------------------------------
# Sample Data1
label_tuple = ("A", "B", "C", "D")
data = {
    'measurement1': (1, 2, 3, 4),
    'measurement2': (2, 3, 4, 5),
    'measurement3': (6, 5, 4, 3),
}
title='title of the plot'
ylabel='label on y-axis'
plot_grouped_bar_chart(data, label_tuple, title, ylabel)

# -------------------------------------------------
# Sample Data2
label_tuple = ("A", "B", "C")
data = {
    'measurement1': (1, 2, 3),
    'measurement2': (2, 3, 4),
    'measurement3': (6, 5, 4),
    'measurement4': (0, 2, 4),
}
title='title of the plot'
ylabel='label on y-axis'
plot_grouped_bar_chart(data, label_tuple, title, ylabel)
'''