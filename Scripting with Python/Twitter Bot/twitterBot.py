import tweepy
import time

auth = tweepy.OAuthHandler('AaM2xMHs3l0rqTv2YeIW4pvkB', 'Ru6JHzXITWO8lOy8xDRHD2FJ3QuBpXC89hm0FV2QkSfnhJctu9')
auth.set_access_token('2958298458-n3qav6cedbjvqtAhiyFVfGlEjs0oJ9XPu0Zo4SJ', 'YntLEl5gwxzFFYGkUJtatCx5Knnv4dJt6Cz92eey6BJPP')

api = tweepy.API(auth)

#way to get all oublic tweets made
'''
public_tweets = api.home_timeline()
for tweet in public_tweets:
    print(tweet.text)
    '''
user = api.me()
print(user.screen_name + " : "+ str(user.followers_count))

def limit_handler(cursor):
    try:
        while True:
            yield cursor.next()
    except tweepy.RateLimitError:
        time.sleep(1000)

#Below Function to show count and list of followers and a functionality to asollow them as well
'''
for follower in limit_handler(tweepy.Cursor(api.followers).items()):
    try:
        print(follower.name)

         #to follow everybody in the list
        #follower.follow()

    except tweepy.TweepError as err:
        print(err.reason)
    except StopIteration:
        break
'''  

search_string = 'python'
numOfTweets = 2

for tweet in tweepy.Cursor(api.search, search_string).items(numOfTweets):
    try:
        tweet.favorite()
        print("I liked that tweet")
    except tweepy.TweepError as err:
        print(err.reason)
    except StopIteration:
        break
