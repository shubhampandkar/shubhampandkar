# Calibrating Credibility of Covid19 tweets  
  
## Goals  
The dashboard presents a brief view of how covid tweets are distributed based on topic names, degree of subjectivity and sentiment attached to the tweet.

In our dashboard, we have used several filters and actions that showcase an overall interaction between the three visualizations: The first worksheet- “Weekly tweets based on subjectivity” displays the number of tweets showing count of expert and non-expert opinions tweeted every week and categorized it based on the categorical attribute - subjectivity label which has 2 categories: 0 being less subjective and 1 being highly subjective. This shows us the weekly trend-line of the number of tweets. The “Distribution by topic” worksheet gives us the distributed view of several topics in the form of bubble charts and their number of tweets in each of these topics. The scatterplot shows subjective probability with its related sentiment score displaying each tweet on an individual level. We used a diverging color scale to represent sentiment score groups. 

For the second dashboard, the word-cloud visualization to represent the keywords being used in tweets and its size indicated the number of times the keyword occurred in the tweets. The purpose of this was to categorize the topic name ‘Other’ as a major portion of the data belonged under this topic name.
  
## Dashboard 1:  
### Interactions  
Each interaction is explained below-
1.	Filter: We filtered the topic names in all the worksheets by taking into consideration several topics which displayed some important insights.
2.	Sort: We sorted the bubble chart based on the number of tweets under each topic in descending order. For the third worksheet displaying scatterplot we sorted the sentiment score legend manually from most negative to most positive.
3.	Actions: In the dashboard, we made use of filter action where ‘Weekly Tweets based on Subjectivity’ is the Source worksheet allowing us to select the number of tweets for each week and also number of tweets categorized by its subjectivity label for every week which results in change of topics in ‘Distribution by topic’ and tweets in ‘Subjectivity probability vs Sentiment Score’. We have applied filter action on ‘Distribution by topic’ and ‘Subjectivity probability vs Sentiment Score’ keeping both as source and destination, so selection in one view makes changes in other view and vice-versa. To get quick summary of the selection made in dashboard, we have applied filter action on all the views as source and destination as Total number of tweets, Percentage of Label(i.e Expert and Non-expert), and Percentage of Sentiment score(i.e Most Negative, Negative, Neutral, Positive, Most Positive). 
  
## Dashboard 2:    
### Interactions  
In our dashboard for the Topic Name ‘Other’ , we can interact in the following ways:

1.	Filter: In all the worksheets, we have used filters for the categorical attribute ‘Topic name’ to select ‘Other’ category, which helped us understand the remaining data that we had filtered out in our previous dashboard. This data consisted of 11,365 tweets. 
2.	Sort: We applied sort in the worksheet ‘Subjectivity probability vs Sentiment Score’ to manually sort the legend of the categorical attribute ‘Sentiment Score’ from Most Negative to Most Positive. 
3.	Actions: Here, we have used ‘Filter’ action by making the ‘Weekly Tweets based on Subjectivity’ as our Source which lets us select the number of tweets for each week and also number of tweets categorized by its subjectivity label for every week . This action eventually gets reflected in the ‘Frequency of Keywords in Tweets’ and ‘Subjectivity probability vs Sentiment Score’. Also we have used the filter action in ‘Frequency of Keywords in Tweets’ and ‘Subjectivity probability vs Sentiment Score’ worksheets where both of them act as source and destination for each other. In this way, when the keywords are selected the individual tweets are visible for those keywords. Also, when an individual tweet is selected, then the keyword associated with that tweet is visible in the view. When any selection  is made on the dashboard, it gets reflected in the Total number of tweets, percentage of Label(i.e Expert and Non-expert), and Percentage of Sentiment score(i.e Most Negative, Negative, Neutral, Positive, Most Positive). 
4.	Legends: We changed the color palette manually to generate a diverging color scale to show negative in shades of red , positive in shades of green, and neutral in gray.
  
## Key Insights:
From the first visualization of weekly distribution, we can see that there is a huge difference in the number of tweets belonging to highly subjective and less subjective categories. There were more highly opinionated tweets in each week of the month of March. In the first week, experts have tweeted more than non-experts but, in each week, the number of non-expert tweets started increasing. Also, the second week had the greatest number of tweets.
2.	The third visualization of subjectivity vs sentiment score displays a cluster for neutral sentiment, whereas positive and negative sentiment tweets were scattered. Positive tweets were more than the negative tweets. Also, if a tweet is less opinionated, there is a high chance of it being negative.
3.	From the second dashboard for ‘Other’ topic name, tweets with keywords as health, test and time belonged more to experts. The tweets including ‘time’ keyword had high chances of being opinionated.

## Links to Dashboards
[Dashboard1](https://public.tableau.com/app/profile/shubham.rajan.pandkar/viz/Covid19TweetsCredibility-1/Final)   
[Dashboard2](https://public.tableau.com/app/profile/shubham.rajan.pandkar/viz/Covid19TweetsCredibility-2/Other)  
