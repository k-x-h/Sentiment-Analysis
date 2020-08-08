import csv 
import tweepy
from textblob import TextBlob
import pandas as pd

#token declarations
print("++++++++++ Enter your Twitter API Developer Key information ++++++++++")
consumer_token=input("Consumer token:")
consumer_secret=input("Consumer Secret:")
access_token=input("Access Token:")
access_token_secret=input("Access Secret:")

#authorization
auth = tweepy.OAuthHandler(consumer_token, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api=tweepy.API(auth)

#input of term to search
searchInput=input("Input search term:")
#sets input to beginning of csv file name
searchInputFormatted=searchInput.replace(" ","_")
csvName="{}SentimentAnalysis.csv".format(searchInputFormatted)

#tweet search
tweetLimit=50 #number of tweets
tweet_search = api.search(searchInput, count=tweetLimit) 
for tweet in tweet_search:
    analysis=TextBlob(tweet.text)

#writes to csv
with open (csvName, "w", encoding="utf-8") as csvFile:
    csvFileWriter=csv.writer(csvFile, lineterminator = '\n')
    csvFileWriter.writerow(["text", "polarity", "subjectivity"])
    for tweet in tweet_search:
        analysis=TextBlob(tweet.text)
        #print(analysis.sentiment)
        csvFileWriter.writerow([tweet.text, analysis.sentiment.polarity, analysis.sentiment.subjectivity])
            
#calculating of averages using pandas
data=pd.read_csv(csvName)
polarityAvg=round(data["polarity"].mean(),3)
subjectivityAvg=round(data["subjectivity"].mean(),3)

if polarityAvg <0:
    polarityResult="Polarity is more negative"
elif polarityAvg >0:
    polarityResult="Polarity is more positive"
elif polarityAvg == 0:
    polarityResult="Polarity is neutral"

if subjectivityAvg < .5:
    subjectivityResults="More objective"
elif subjectivityAvg > .5:
    subjectivityResults="More subjective"
elif subjectivityAvg == .5:
    subjectivityResults="Neutral objectivity/subjectivity"

#results printout
print("++++++++++++Results++++++++++++")
print("1. Term searched:", searchInput)
print("2. Number of items:", tweetLimit)
print("3. Polarity average:", polarityAvg, polarityResult, "(-1=Negative, 1=Positive)")
print("4. Subjectivity average:", subjectivityAvg, subjectivityResults, "(0=Objective, 1=Subjective") 
print("5. Csv file name:", csvName)






