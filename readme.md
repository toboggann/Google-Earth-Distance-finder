# Prediction-Algo

This is a project that I developed during my freshman year in college for the CS:1210 class. The algorithm retrieves data from online datasets and converts it into appropriate data structures. It then uses these data structures to predict ratings for both movies and users. The algorithm could be useful in recommending movies to users or predicting how a user might rate a particular movie.

## Summary & Usage License

MovieLens datasets were collected by the GroupLens Research Project at the University of Minnesota.

### This dataset consists of:
- 100,000 ratings (1-5) from 943 users on 1,682 movies.
- Each user has rated at least 20 movies.
- Simple demographic information for the users (age, gender, occupation, zip code).

The data was collected through the MovieLens website (movielens.umn.edu) during the seven-month period from September 19th, 1997 through April 22nd, 1998. This data has been cleaned up—users who had less than 20 ratings or did not have complete demographic information were removed from this dataset. Detailed descriptions of the data files can be found at the end of this file.

Neither the University of Minnesota nor any of the researchers involved can guarantee the correctness of the data, its suitability for any particular purpose, or the validity of results based on the use of the dataset. The dataset may be used for any research purposes under the following conditions:

- The user may not state or imply any endorsement from the University of Minnesota or the GroupLens Research Group.
- The user must acknowledge the use of the dataset in publications resulting from the use of the dataset (see below for citation information).
- The user may not redistribute the data without separate permission.
- The user may not use this information for any commercial or revenue-bearing purposes without first obtaining permission from a faculty member of the GroupLens Research Project at the University of Minnesota.

If you have any further questions or comments, please contact GroupLens at <grouplens-info@cs.umn.edu>.

## Citation

To acknowledge use of the dataset in publications, please cite the following paper:

F. Maxwell Harper and Joseph A. Konstan. 2015. The MovieLens Datasets: History and Context. ACM Transactions on Interactive Intelligent Systems (TiiS) 5, 4, Article 19 (December 2015), 19 pages. DOI=[http://dx.doi.org/10.1145/2827872](http://dx.doi.org/10.1145/2827872).

## Acknowledgements

Thanks to Al Borchers for cleaning up this data and writing the accompanying scripts.

## Published Work That Has Used This Dataset

- Herlocker, J., Konstan, J., Borchers, A., Riedl, J.. An Algorithmic Framework for Performing Collaborative Filtering. Proceedings of the 1999 Conference on Research and Development in Information Retrieval. Aug. 1999.

## Further Information About the GroupLens Research Project

The GroupLens Research Project is a research group in the Department of Computer Science and Engineering at the University of Minnesota. Members of the GroupLens Research Project are involved in many research projects related to the fields of information filtering, collaborative filtering, and recommender systems. The project is led by professors John Riedl and Joseph Konstan. The project began to explore automated collaborative filtering in 1992 but is most well known for its worldwide trial of an automated collaborative filtering system for Usenet news in 1996. The technology developed in the Usenet trial formed the base for the formation of Net Perceptions, Inc., which was founded by members of GroupLens Research. Since then, the project has expanded its scope to research overall information filtering solutions, integrating content-based methods as well as improving current collaborative filtering technology.

Further information on the GroupLens Research project, including research publications, can be found at the following website:

[http://www.grouplens.org/](http://www.grouplens.org/)

GroupLens Research currently operates a movie recommender based on collaborative filtering:

[http://www.movielens.org/](http://www.movielens.org/)

## Detailed Descriptions of Data Files

Here are brief descriptions of the data files:

- **ml-data.tar.gz**: Compressed tar file. To rebuild the u data files, do this:
  ```sh
  gunzip ml-data.tar.gz
  tar xvf ml-data.tar
  ./mku.sh

u.data: The full u data set, 100,000 ratings by 943 users on 1,682 items. Each user has rated at least 20 movies. Users and items are numbered consecutively from 1. The data is randomly ordered. This is a tab-separated list of user id | item id | rating | timestamp. The timestamps are Unix seconds since 1/1/1970 UTC.

u.info: The number of users, items, and ratings in the u data set.

u.item: Information about the items (movies); this is a tab-separated list of movie id | movie title | release date | video release date | IMDb URL | unknown | Action | Adventure | Animation | Children's | Comedy | Crime | Documentary | Drama | Fantasy | Film-Noir | Horror | Musical | Mystery | Romance | Sci-Fi | Thriller | War | Western. The last 19 fields are the genres, where a 1 indicates the movie is of that genre, and a 0 indicates it is not; movies can be in several genres at once. The movie ids are the ones used in the u.data data set.

u.genre: A list of the genres.

u.user: Demographic information about the users; this is a tab-separated list of user id | age | gender | occupation | zip code. The user ids are the ones used in the u.data data set.

u.occupation: A list of the occupations.

u1.base: The data sets u1.base and u1.test through u5.base and u5.test are 80%/20% splits of the u data into training and test data.

u1.test: Each of u1, ..., u5 have disjoint test sets; this is for 5-fold cross-validation (where you repeat your experiment with each training and test set and average the results). These data sets can be generated from u.data by mku.sh.

u2.base

u2.test

u3.base

u3.test

u4.base

u4.test

u5.base

u5.test

ua.base: The data sets ua.base, ua.test, ub.base, and ub.test split the u data into a training set and a test set with exactly 10 ratings per user in the test set. The sets ua.test and ub.test are disjoint. These data sets can be generated from u.data by mku.sh.

allbut.pl: The script that generates training and test sets where all but n of a user's ratings are in the training data.

mku.sh: A shell script to generate all the u data sets from u.data.
