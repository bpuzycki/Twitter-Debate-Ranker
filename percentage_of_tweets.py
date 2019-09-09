
from tweepy import OAuthHandler
from tweepy import Stream
import tweepy
from textblob import TextBlob
import twitter_credentials
import datetime as dt

auth = OAuthHandler(twitter_credentials.CONSUMER_KEY,twitter_credentials.CONSUMER_SECRET)
auth.set_access_token(twitter_credentials.ACCESS_TOKEN, twitter_credentials.ACCESS_TOKEN_SECRET)


api = tweepy.API(auth,wait_on_rate_limit = True, wait_on_rate_limit_notify = True)

# Open/create a file to append data to
txtFile = open('percentage_before3.txt', 'w')

num_tweets = 0
ids = set()
terms = 'Mayor Pete OR Elizabeth Warren OR Biden OR Bernie Sanders OR Kamala Harris'
num_pete = 0
num_pete_pro = 0
num_pete_con = 0

num_warren = 0
num_warren_pro = 0
num_warren_con = 0

num_biden = 0
num_biden_pro = 0
num_biden_con = 0

num_sanders = 0
num_sanders_pro = 0
num_sanders_con = 0

num_kam = 0
num_kam_pro = 0
num_kam_con = 0
for tweet in tweepy.Cursor(api.search,
                    q = terms,
                    since = "2019-07-26",
                    until = "2019-07-30",
                    lang = "en").items():
    num_tweets += 1
    print(num_tweets)

    if num_tweets > 250000:
        break
    if (not tweet.retweeted) and ('RT @' not in tweet.text):
        ids.add(tweet.id)
        if ('Mayor Pete' in tweet.text):
            num_pete += 1
            if float(TextBlob(tweet.text).polarity) < -0.2:
                num_pete_con += 1
            elif float(TextBlob(tweet.text).polarity) > 0.2:
                num_pete_pro += 1
        if ('Elizabeth Warren' in tweet.text):
            num_warren += 1
            if float(TextBlob(tweet.text).polarity) < -0.2:
                num_warren_con += 1
            elif float(TextBlob(tweet.text).polarity) > 0.2:
                num_warren_pro += 1
        if ('Biden' in tweet.text):
            num_biden += 1
            if float(TextBlob(tweet.text).polarity) < -0.2:
                num_biden_con += 1
            elif float(TextBlob(tweet.text).polarity) > 0.2:
                num_biden_pro += 1
        if ('Bernie Sanders' in tweet.text):
            num_sanders += 1
            if float(TextBlob(tweet.text).polarity) < -0.2:
                num_sanders_con += 1
            elif float(TextBlob(tweet.text).polarity) > 0.2:
                num_sanders_pro += 1
        if ('Kamala Harris' in tweet.text):
            num_kam += 1
            if float(TextBlob(tweet.text).polarity) < -0.2:
                num_kam_con += 1
            elif float(TextBlob(tweet.text).polarity) > 0.2:
                num_kam_pro += 1
        
        #csvWriter.writerow([tweet.created_at, tweet.text.encode('utf-8'), TextBlob(tweet.text).polarity])
        print (len(ids))
        print(tweet.text)
        print('Pete: ' + str(num_pete) + '   Warren: ' + str(num_warren) + '   Biden: ' + str(num_biden) + '   Sanders: ' + str(num_sanders) + '   Harris: ' + str(num_kam))
    
    


txtFile.write("Buttigeig:"+"\n")
txtFile.write("Pros: " + str(num_pete_pro)+"\n")
txtFile.write("Cons: " + str(num_pete_con)+"\n")
txtFile.write("Total Buttigieg Tweets: " + str(num_pete)+"\n")
txtFile.write("Ratio of Pros to Cons = " + str(num_pete_pro) + ":" + str(num_pete_con)+"\n")

txtFile.write("Warren:"+"\n")
txtFile.write("Pros: " + str(num_warren_pro)+"\n")
txtFile.write("Cons: " + str(num_warren_con)+"\n")
txtFile.write("Total Warren Tweets: " + str(num_warren)+"\n")
txtFile.write("Ratio of Pros to Cons = " + str(num_warren_pro) + ":" + str(num_warren_con)+"\n")

txtFile.write("Biden:"+"\n")
txtFile.write("Pros: " + str(num_biden_pro)+"\n")
txtFile.write("Cons: " + str(num_biden_con)+"\n")
txtFile.write("Total Biden Tweets: " + str(num_biden)+"\n")
txtFile.write("Ratio of Pros to Cons = " + str(num_biden_pro) + ":" + str(num_biden_con)+"\n")

txtFile.write("Kamala Harris:"+"\n")
txtFile.write("Pros: " + str(num_kam_pro)+"\n")
txtFile.write("Cons: " + str(num_kam_con)+"\n")
txtFile.write("Total Kamala Tweets: " + str(num_kam)+"\n")
txtFile.write("Ratio of Pros to Cons = " + str(num_kam_pro) + ":" + str(num_kam_con)+"\n")

txtFile.write("Sanders:"+"\n")
txtFile.write("Pros: " + str(num_sanders_pro)+"\n")
txtFile.write("Cons: " + str(num_sanders_con)+"\n")
txtFile.write("Total Sanders Tweets: " + str(num_sanders)+"\n")
txtFile.write("Ratio of Pros to Cons = " + str(num_sanders_pro) + ":" + str(num_sanders_con)+"\n")

txtFile.close()