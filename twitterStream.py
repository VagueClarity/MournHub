import tweepy

consumer_key = 'HSPRQUNqbMKeKm68dbgdL3ZZu'
consumer_key_secret = 'oPZtMa0XmvNGU3eRvilVq5z7SjSVilD0wKb4Iqc59dTQC8qUoc'
access_token = '984164839047114752-EVwG0QcDdPSgZfNwZFwGmtAl7bOtoVd'
access_token_secret = 'vICAsozueokYNNmdodaK5Gc1Odt2tRZItigebnPP6f4T2'


class TweetListener(tweepy.StreamListener):
    def on_status(self, status):
        print('Tweet text: ' + status.text)
        return True

    def on_error(self, status_code):
        print('Got an error with status code: ' + str(status_code))
        return True

    def on_timeout(self):
        print('Timeout...')
        return True

if __name__ == '__main__':
    listener = TweetListener()
    auth = tweepy.OAuthHandler(consumer_key, consumer_key_secret)
    auth.set_access_token(access_token, access_token_secret)

stream = tweepy.Stream(auth, listener)
stream.filter(follow=[], track = ['#SFGiants', '#Athletics'])


