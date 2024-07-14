import random
import math
import matplotlib.pyplot as plt

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

def randomPrediction(u, m):
    return random.randint(1,5)

def meanUserRatingPrediction(u, m, rLu):
    count = 0
    ratings = 0
    for r in rLu[u-1].items():
        ratings += r[1]
        count +=1
    return ratings/count

def meanMovieRatingPrediction(u, m, rLm):
    count = 0
    ratings = 0
    for r in rLm[m-1].items():
        ratings += r[1]
        count +=1
    return ratings/count   

def demRatingPrediction(u, m, userList, rLu):
    age = userList[u-1]["age"]
    gender = userList[u-1]["gender"]
    count = 0
    ratings = 0
    rList=[]
    for p in range(len(userList)):
        if userList[p]["gender"]==gender and (userList[p]["age"] >= age-5 and userList[p]["age"] <= age+5) and p!=u-1:
            for r in rLu[p].items():
                if r[0]==m:
                    ratings += r[1]
                    count +=1

    if count==0:
        return None
    else:
        return ratings/count

def genreRatingPrediction(u, m, movieList, rLu):
    count = 0
    ratings = 0
    for r in rLu[u-1].items():
        for g in range(19):
            if (movieList[r[0]-1]["genre"][g] == movieList[m-1]["genre"][g]) and movieList[m-1]["genre"][g] == 1 and (r[0]-1)!=m-1:
                count+=1
                ratings += r[1]
                break
    if count == 0:
        return None
    else:
        return ratings/count

def partitionRatings(rawRatings, testPercent):
    number = len(rawRatings)*(testPercent/100)
    number = round(number)
    trainingSet=list(rawRatings)
    testSet=[1]*number
    for r in range(number):
        p=trainingSet.pop(random.randint(0,len(trainingSet)-1))
        testSet[r]=p
    return trainingSet, testSet


def rmse(actualRatings, predictedRatings):
    total=0
    count=0
    for r in range(len(actualRatings)):
        if actualRatings[r] != None and predictedRatings[r]!=None:
            q=actualRatings[r]-predictedRatings[r]
            f=q*q
            total+=f
        else:
            count+=1
    g=total/(len(actualRatings)-count)
    return math.sqrt(g)


userList = createUserList()
numUsers = len(userList)
movieList = createMovieList()
numMovies = len(movieList)
rawRatings = readRatings()
[rLu, rLm] = createRatingsDataStructure(numUsers, numMovies, rawRatings)





#-----
#part 3
#-----

def similarity(u, v , rLu):
    num = 0
    denomI=0
    denomV=0
    rI=meanUserRatingPrediction(u, 0, rLu)
    rV=meanUserRatingPrediction(v, 0, rLu)
    for m in rLu[u-1].items():
        if m[0] in rLu[v-1]:
            num += (m[1] - rI) * (rLu[v-1][m[0]] - rV)
            denomI+=(m[1]-rI)*(m[1]-rI)
            denomV+=(rLu[v-1][m[0]] - rV)*(rLu[v-1][m[0]] - rV)
    if num ==0 or denomI==0 or denomV==0:
        return 0
    else:
        return num/(math.sqrt(denomI)*math.sqrt(denomV))
    
def kNearestNeighbors(u, rLu, k):
    uRatings = rLu[u-1]
    similarList = [[x+1, similarity(u,x+1,rLu)] for x in range(len(rLu)) if u!= (x+1)]
    similarList.sort(reverse = True , key lmbda x: x[1])
    mostSimilar = similarList[:k]
    return [(index[0],index[1]) for index in mostSimilar]

def CFRatingPrediction(u, m, rLu, friends):
    rI=meanUserRatingPrediction(u,0,rLu)
    num=0
    denom=0
    for x in friends:
        if m in rLu[x[0]-1]:
            num+=((rLu[x[0]-1][m]-meanUserRatingPrediction(x[0],0,rLu))*similarity(u,x[0],rLu))
            denom += abs(similarity(u,x[0],rLu))
    if denom == 0:
        denom = 1
    return rI + (num/denom)

rLu = createRatingsDataStructure(len(createUserList()), len(createMovieList()), readReatings())[0]
friends = kNearestNeighbors(1, rLu, friends)


def 

