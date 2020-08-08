# Sentiment-Analysis
This project conducts a sentiment analysis based on a search of the most recent tweets containing a specified term.
This project is written in Python and uses Tweepy, TextBlob, and Pandas.
To use this project, you must have your Twitter Dev API information (Consumer token/secret, access token/secret)
This program defaults to pulling the 50 most recent tweets, but can be altered to go above that (You can max out the Twitter request limit by putting it at 200, going beyond that would require modifications)
In the results printout, a polarity average result closer to -1 means that on average most of the tweets found are negative, whereas a polarity average closer to 1 means that most of the tweets found are positive.
Similarly, for the subjectivity average, results closer to 0 mean that the tweets are more objective, whereas a result closer to 1 means that the tweets are more subjective.

An example results csv has been included (New_YorkSentimentAnalysis.csv)
