import tweepy
from datas.models import  Record

# 需要申請(Elevated access)

class TweetGenerator:
    # 相關ID
    consumer_key =  ''
    consumer_secret = ''
    access_token = ''
    access_token_secret =  ''

    auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_token_secret)
    api = tweepy.API(auth, wait_on_rate_limit = True)

    def profile_image(self, filename):
        self.api.update_profile_image(filename)

    def update_profile_info(self, name, url, location, description):
        self.api.update_profile(name, url, location, description)

    def post_tweet(self, text):
        self.api.update_status(text)

    # 上傳有圖片推文
    def upload_media(self, text, filename):
        media = self.api.media_upload(filename)
        self.api.update_status(text, media_ids = [media.media_id_string])

