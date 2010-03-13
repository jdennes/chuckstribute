from google.appengine.ext import db
from google.appengine.tools import bulkloader

from models import ChucksImage

class ChucksImageLoader(bulkloader.Loader):
    def __init__(self):
        bulkloader.Loader.__init__(self, 'ChucksImage',
                                   [('flickr_id', lambda x: x.decode('utf-8')),
                                    ('flickr_secret', lambda x: x.decode('utf-8')),
                                    ('flickr_server', lambda x: x.decode('utf-8')),
                                    ('flickr_farm', lambda x: x.decode('utf-8')),
                                    ('flickr_user_id', lambda x: x.decode('utf-8')),
                                   ])
loaders = [ChucksImageLoader]