import random
import math
import matplotlib.pyplot as plt

from project2Phase2a import *

def main():
    algo1 = []
    algo2 = []
    algo3 = []
    algo4 = []
    algo5 = []

    j = 0
    while j < 10:
        
        [trainingSet, testSet] = partitionRatings(rawRatings, 20)
        [trainingRLu, trainingRLm] = createRatingsDataStructure(numUsers, numMovies, trainingSet)    
        #-----
        #Variables
        #-----
        randomList = []
        meanUserList = []
        meanMovieList = []
        demRatingList = []
        genreRatingList = [] 

        for test in testSet:
            u = test[0]
            m = test[1]
            randomList.append(randomPrediction(u, m))
            meanUserList.append(meanUserRatingPrediction(u, m, rLu))
            meanMovieList.append(meanMovieRatingPrediction(u, m, rLm))
            demRatingList.append(demRatingPrediction(u, m, userList, rLu))
            genreRatingList.append(genreRatingPrediction(u, m, movieList, rLu))
        
        actualRatings = []
        
        for users in testSet:
            u = users[0]
            m = users[1]
            actualRatings.append(rLu[u-1][m])


        randomRmse = rmse(actualRatings, randomList)
        meanUserRmse = rmse(actualRatings, meanUserList)
        meanMovieRmse = rmse(actualRatings, meanMovieList)
        demRatingRmse = rmse(actualRatings, demRatingList)
        genreRatingRmse = rmse(actualRatings, genreRatingList)
        
        algo1.append(randomRmse)
        algo2.append(meanUserRmse)
        algo3.append(meanMovieRmse)
        algo4.append(demRatingRmse)
        algo5.append(genreRatingRmse)
        
        j +=1
        
        
    def draw_boxplot(data, labels):
        plt.boxplot(x=data, labels=labels)
        plt.title("Algorithm performance comparison")
        plt.ylabel("RMSE values")
        plt.show()
        plt.close()

        
        
    #-----
    #DATA
    #-----
    data = [algo1, algo2, algo3, algo4,algo5]
    labels = ["Algo1", "Algo2", "Algo3", "Algo4","Algo5"]
        
    draw_boxplot(data, labels)

if __name__ == "__main__":
    main()
