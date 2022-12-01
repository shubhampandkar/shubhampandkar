# Book-Recommendation-System

## Description

The goal of this project is to develop a recommendation system that provides a list of 10 books that are similar to a book that a customer has read. This project will implement a collaborative-based filtering method via scikit learn's K-Nearest Neighbours clustering algorithm using the Amazon books dataset. 

## Dataset
* The books data contains all the book titles, ISBNs, author, publisher and year of publication. 
* The user dataset contains the user IDs, location and age. 
* The ratings dataset contains user ids, ISBNs and book rating scores. 
**All datasets are a subset of books available on Amazon.**

Link to dataset : [Dataset](https://www.kaggle.com/datasets/arashnic/book-recommendation-dataset)

## Colaborative filtering

Recommends items based on similarity measures between users and/or items leveraging the use of a user-item matrix.
* Core Features:
  1. The model's assumption is that people generally tend to like similar things
  2. Predictions are made based on item preferences of similar users
  3. User-Item matrix is used to generate recommendations
  4. Direct User Ratings are obtained through explicit feedback via rating scores
  5. Indirect User Behavior can be obtained through implicit feedback such as listening, watching, purchasing, etc.)
  
## Contents
1. Data Cleaning code - Data_cleaning.ipynb
2. Recommendation model code - Recommendation_system.ipynb
3. Application code - app.py
4. Requirements - Requirements.txt

## Cleaning

### Books data
1. Null values - Some null values were identified with the author and publisher, thus correct values were added to the books dataset from researching and cross-referencing ISBNs via Amazon and BookFinder.
2. Year of Publication - I discovered that some years in the dataset contained values for the year 0, 2024, 2026, 2030, 2037, 2038 and 2050. Evidently, the year 0 doesn't make sense and years in the future also do not make sense. All observations with these values were dropped. After this operation, the oldest publication year is set at 1376 and the most recent is 2021.
3. ISBN and Book titles - It should be noted that there are duplicate book titles due to certain books having multiple publishers or different years of publication. For example, The Left Hand of Darkness by Ursula K. Le Guin was published in 1984 by Penguin Putnam-Mass and again in 1999 by Sagebrush Bound. At this time, these duplications have not been managed, but there is a future opportunity to consolidate these duplications to further optimize the recommendation system.

### Users data
1. Age - Age values that were less than 5 and greater than 90 were imputed to null values. This was done since I believe it is unlikely that a person younger than 5 and older than 90 would be submitting ratings for books purchased via Amazon. Null values were then imputed to the average age of 35 in the dataset.
2. Location - Some location values were not null, but were actually strings of 'n/a, n/a, n/a'. Observations with this value were dropped from the dataset.

### Ratings Data
1. Book rating - '0' - There was a high count of 716,109 book rating scores of 0 of the total 1,149,780 observations. The 0 rating provides no value to the recommendation system and thus all observations with a 0 rating were removed from the dataset.

## EDA

Merging all 3 datasets and exploring the data as we want to be sire of what features should be fed to the model that will provide good results

#### Statistics
![Statistics](https://github.com/shubhampandkar/Book-Recommendation-System/blob/main/images/statistics.png "Statistics")

#### Top 10 books 
![Top 10 books](https://github.com/shubhampandkar/Book-Recommendation-System/blob/main/images/top%2010%20books.png "Top 10 books")

#### Top 10 Users
![Top 10 users](https://github.com/shubhampandkar/Book-Recommendation-System/blob/main/images/top%2010%20user%20rating.png "Top 10 users")

#### Distance plot for Average Rating
![Average rating](https://github.com/shubhampandkar/Book-Recommendation-System/blob/main/images/average_ratings.png "Average rating")
**There is extreme peak around 0 and peaks around 4 to 10 shows there are high number of books having count 0**

#### Joint plot
![Joint plot](https://github.com/shubhampandkar/Book-Recommendation-System/blob/main/images/joint_plot.png "Joint plot")
**The ratings are mostly given in the range of 6-9**

## Recommendation system

In order to feed the data into the machine learning model, the alphanumeric ISBN values had to be assigned unique integer IDs. This process was executed in the following steps:

* Use .ravel() method to create array of unique ISBN values and store in book_ids variable.
* Cast book_ids array to pandas series.
* Convert book_ids to pandas DataFrame
* Reset index of book_ids, rename columns to ISBN and Book-ID
* Merge book_ids DataFrame with larger merged dataset

## Compressed Sparse row matrix
![CSR](https://github.com/shubhampandkar/Book-Recommendation-System/blob/main/images/CSR.png "CSR")

## K nearest neighbors
![KNN](https://github.com/shubhampandkar/Book-Recommendation-System/blob/main/images/KNN.png "KNN")

## Application
The application was built using streamlit. Then the app was deployed on heroku.
The user will select or enter a name of the book, once he clicks on recommend, similar 10 books will be recommended to the user.

Deployed application : [App](https://book-recommender-srp.herokuapp.com)

![App](https://github.com/shubhampandkar/Book-Recommendation-System/blob/main/images/app.png "App")
