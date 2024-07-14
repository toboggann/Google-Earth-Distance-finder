#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Apr 16 13:32:10 2023

@author: macbook_user
"""

from project2Phase1 import *

tests = []

userList = createUserList()
movieList = createMovieList()
rawRatings = readRatings()
numUsers = len(userList)
numMovies = len(movieList)
[rLu, rLm] = createRatingsDataStructure(numUsers, numMovies, rawRatings)
genreList = createGenreList()

# test 1
tests.append([round(x, 4) for x in demGenreRatingFractions(userList, movieList, rLu, "A", [20, 21], [1, 5])] == [0.0005, 0.3008, 0.1521, 0.0384, 0.0719, 0.3077, 0.0934, 0.0037, 0.3536, 0.0142, 0.0112, 0.0655, 0.0394, 0.0484, 0.1793, 0.1374, 0.2524, 0.0751, 0.0183])

#test 2
tests.append([round(x, 4) for x in demGenreRatingFractions(userList, movieList, rLu, "F", [20, 22], [4, 5])] == [0.0, 0.1425, 0.0849, 0.0216, 0.055, 0.1553, 0.0427, 0.001, 0.2366, 0.0062, 0.0036, 0.0334, 0.0283, 0.0247, 0.1322, 0.0617, 0.1204, 0.0556, 0.0057])

# test 3
tests.append([round(x, 4) for x in demGenreRatingFractions(userList, movieList, rLu, "M", [20, 21], [1, 5])] == [0.0007, 0.3292, 0.1566, 0.0372, 0.0555, 0.2926, 0.1022, 0.0044, 0.3413, 0.0122, 0.0139, 0.0687, 0.0348, 0.0511, 0.158, 0.1566, 0.2703, 0.0761, 0.02])

# test 4
tests.append([round(x, 4) for x in demGenreRatingFractions(userList, movieList, rLu, "A", [1, 100], [1, 5])] == [0.0001, 0.2559, 0.1375, 0.036, 0.0718, 0.2983, 0.0805, 0.0076, 0.399, 0.0135, 0.0173, 0.0532, 0.0495, 0.0524, 0.1946, 0.1273, 0.2187, 0.094, 0.0185])

# test 5
tests.append([round(x, 4) for x in demGenreRatingFractions(userList, movieList, rLu, "M", [50, 60], [1, 2])] == [0.0, 0.0332, 0.0173, 0.0027, 0.0089, 0.0392, 0.0106, 0.0008, 0.0467, 0.0014, 0.0017, 0.0092, 0.0076, 0.0076, 0.0232, 0.0172, 0.0267, 0.0084, 0.003])

# test 6
tests.append([round(x, 4) for x in demGenreRatingFractions(userList, movieList, rLu, "M", [50, 60], [4, 2])] == [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0])

# test 7
tests.append(demGenreRatingFractions(userList, movieList, rLu, "M", [20, 20], [1, 2]) == [None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None])

# test 8
tests.append([round(x, 4) for x in demGenreRatingFractions(userList, movieList, rLu, "F", [40, 50], [4, 5])] == [0.0, 0.1112, 0.0621, 0.0152, 0.0374, 0.1304, 0.0445, 0.0064, 0.2995, 0.0064, 0.0145, 0.0126, 0.0317, 0.0376, 0.1331, 0.0495, 0.1102, 0.0671, 0.009])

# test 9
tests.append([round(x, 4) for x in demGenreRatingFractions(userList, movieList, rLu, "M", [40, 41], [4, 5])] == [0.0, 0.1553, 0.0987, 0.0275, 0.0623, 0.1489, 0.0299, 0.0024, 0.2468, 0.0138, 0.0073, 0.0138, 0.038, 0.0275, 0.1222, 0.0801, 0.0955, 0.0583, 0.0121])

# test 10
tests.append([round(x, 4) for x in demGenreRatingFractions(userList, movieList, rLu, "A", [50, 55], [1, 5])] == [0.0, 0.2075, 0.1063, 0.0209, 0.0467, 0.2637, 0.0829, 0.011, 0.4893, 0.0107, 0.0233, 0.0348, 0.045, 0.0649, 0.2066, 0.102, 0.2002, 0.1087, 0.0209])



# Output the test results
i = 0
for result in tests:
    if not result:
        print("Test", i + 1, "failed")
    else:
        print("Test", i + 1, "passed")
    i = i + 1
