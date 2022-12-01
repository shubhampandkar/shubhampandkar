# Quora Question Pairs
### Description  
  
Quora is a platform where people ask questions as well as connect with other people who contribute with their insights and quality solutions.  
As this is a great tool, people who ask questions, expect quick answers. Incase the questions have been repeated mulitple times on quora, then answers to these questions can be retrieved easily.  
For such a scenario, it is important to identify the duplicate questions.  
This project is to predict whether a question on quora has a similar existing question pair.

> Kaggle Project

#### Problem Statement
* Identify which questions asked on Quora are duplicates of questions that have already been asked.  
* This could be useful to instantly provide answers to questions that have already been answered.  
* We are tasked with predicting whether a pair of questions are duplicates or not. 

### Business Objectives and Constraints
1. Cost of misclassification is high  
2. Threshold of choice. 
3. NO strict latency concerns
4. Interpretability is partially important

## Machine Learning Problem
* Binary Classification problem - We need to predict if questions are duplicate or not
1. Performance Metric  
    * log loss  
    * Binary confusion matrix
2. Train-Test Construction
    * Train and test will be built from the dataset by splitting it in 80:20 ratio

## Class Distribution
![class_distribution](https://github.com/shubhampandkar/Quora_Question_pair/blob/main/images/class%20distribution.png 'Class Distribution')   
* The graph shows how the dataset is distributed for both classes, duplicate(1) and non-duplicate(0). 

## Question Distribution
![question_distribution](https://github.com/shubhampandkar/Quora_Question_pair/blob/main/images/unique_repeated.png 'Question Distribution')  
* The graph shows how the unique and repeated questions have been distributed in the dataset. 

## Number of Occurences of Each Question
![question_occurences](https://github.com/shubhampandkar/Quora_Question_pair/blob/main/images/occ_unique_ques.png 'Question Occurences')
* The graph is Log histogram of number of occurences of unique question

## Word Clouds for Duplicate and Non-duplicate Questions 
* Duplicate Question:
![wordcloud_1](https://github.com/shubhampandkar/Quora_Question_pair/blob/main/images/WC_dup.png 'Duplicate Questions')
* Non-duplicate Question:
![wordcloud_2](https://github.com/shubhampandkar/Quora_Question_pair/blob/main/images/WC_ndup.png 'Non-Duplicate Questions')

**NOTE - 24 new features were created including token features**  

## Model : GBDT
![GBDT](https://github.com/shubhampandkar/Quora_Question_pair/blob/main/images/gbdt.png 'Heat-map')

**From above heatmap of log-loss for different pairs of estimators, estimator 500 and depth 10 is giving least log-loss of 0.299 for training and 0.341 for testing** 

## Conclusion : Model Performance
* Table showing all model performances:
![pretty_table](https://github.com/shubhampandkar/Quora_Question_pair/blob/main/images/prettytable.png 'Pretty Table')

* Best model : GBDT with TFIDF vectors giving test log-loss of 0.3415
