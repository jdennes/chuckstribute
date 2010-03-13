
from google.appengine.ext import db

class ChucksImage(db.Model):
  flickr_id = db.StringProperty(required=True)
  flickr_secret = db.StringProperty(required=True)
  flickr_server = db.StringProperty(required=True)
  flickr_farm = db.StringProperty(required=True)
  flickr_user_id = db.StringProperty(required=True)
  date_added = db.DateTimeProperty(auto_now_add=True)
