#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Apr 25 18:48:33 2023

@author: Sriram Pemmaraju
"""
from project2Phase2a import *

#main program
# Read and store in data structures
userList = createUserList()
numUsers = len(userList)
movieList = createMovieList()
numMovies = len(movieList)
rawRatings = readRatings()
[rLu, rLm] = createRatingsDataStructure(numUsers, numMovies, rawRatings)

tests = []

# Tests for randomPrediction
# Test 1
tests.append(1<= randomPrediction(100, 100) <= 5)

# Test 2
tests.append(1 <= randomPrediction(numUsers, numMovies) <= 5)

# Test 3
tests.append(2.9 <= sum([randomPrediction(10, 20) for x in range(10000)])/10000 <= 3.1)


# Tests for meanUserRatingPrediction
# Test 4
predList = []
for j in range(1, 4):
    predList.append(round(meanUserRatingPrediction(1, j, rLu), 4))
tests.append(predList == [3.6103, 3.6103, 3.6103])

# Test 5
predList = []
for j in range(1, 4):
    predList.append(round(meanUserRatingPrediction(2, j, rLu), 4))
tests.append(predList == [3.7097, 3.7097, 3.7097])

# Test 6
predList = []
for j in range(1, 4):
    predList.append(round(meanUserRatingPrediction(3, j, rLu), 4))
tests.append(predList == [2.7963, 2.7963, 2.7963])

# Tests for meanUserRatingPrediction
# Test 7
predList = []
for j in range(1, 4):
    predList.append(round(meanMovieRatingPrediction(1, j, rLm), 4))
tests.append(predList == [3.8783, 3.2061, 3.0333])

# Test 8
predList = []
for j in range(1, 4):
    predList.append(round(meanMovieRatingPrediction(2, j, rLm), 4))
tests.append(predList == [3.8783, 3.2061, 3.0333])

# Test 9
predList = []
for j in range(1, 4):
    predList.append(round(meanMovieRatingPrediction(3, j, rLm), 4))
tests.append(predList == [3.8783, 3.2061, 3.0333])


# Tests for demRatingPrediction
# Test 10
predList = []
for j in range(1, 4):
    predList.append(round(demRatingPrediction(1, j, userList, rLu), 4))
tests.append(predList == [3.8903, 3.1875, 3.2549])

# Test 11
predList = []
for j in range(1, 4):
    predList.append(round(demRatingPrediction(2, j, userList, rLu), 4))
tests.append(predList == [3.0833, 3.0, 3.0])

# Test 12
predList = []
for j in range(1, 4):
    predList.append(round(demRatingPrediction(3, j, userList, rLu), 4))
tests.append(predList == [3.8803, 3.2, 3.2963])


# Tests for genreRatingPrediction
# Test 13
predList = []
for j in range(1, 4):
    predList.append(round(genreRatingPrediction(1, j, movieList, rLu), 4))
tests.append(predList == [3.2857, 3.3945, 3.6078])

# Test 14
predList = []
for j in range(1, 4):
    predList.append(round(genreRatingPrediction(2, j, movieList, rLu), 4))
tests.append(predList == [3.6111, 3.7222, 3.5833])

# Test 15
predList = []
for j in range(1, 4):
    predList.append(round(genreRatingPrediction(3, j, movieList, rLu), 4))
tests.append(predList == [2.5833, 2.5714, 2.5238])


# Tests for partition
[trainingSet, testSet] = partitionRatings(rawRatings, 10)

# Test 16
tests.append((len(trainingSet) == 90000) and (len(testSet) == 10000))

# Test 17
tests.append(sorted(rawRatings) == sorted(trainingSet + testSet))

[trainingSet, testSet] = partitionRatings(rawRatings, 20)
# Test 18
tests.append((len(trainingSet) == 80000) and (len(testSet) == 20000))

# Test 19
tests.append(sorted(rawRatings) == sorted(trainingSet + testSet))

# Tests for rmse
# Test 20
tests.append(int(rmse([1]*20000, [2]*20000)) == 1)

# Test 21
tests.append(int(rmse([1]*20000 + [1], [3]*20000 + [None])) == 2)

# Test 22
tests.append(round(rmse([1]*20000, [x[2] for x in rawRatings[:20000]]), 4) == 2.786)

# Test 23
tests.append(round(rmse([2]*20000, [x[2] for x in rawRatings[:20000]]), 4) == 1.9209)

# Test 24
tests.append(round(rmse([3]*20000, [x[2] for x in rawRatings[:20000]]), 4) == 1.272)

# Test 25
tests.append(round(rmse([4]*20000, [x[2] for x in rawRatings[:20000]]), 4) == 1.2435)

# Output the test results
i = 0
for result in tests:
    if not result:
        print("Test", i + 1, "failed")
    else:
        print("Test", i + 1, "passed")
    i = i + 1
