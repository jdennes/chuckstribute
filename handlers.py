
import sys, os
from itertools import izip

from google.appengine.ext import webapp
from google.appengine.ext.webapp import util
from google.appengine.ext.webapp import template

from models import ChucksImage

class MainHandler(webapp.RequestHandler):

  def grouper(self, n, iterable, padvalue=None):
    return izip(*[iter(iterable)]*n)

  def get(self):

    # Just get a sample of images to start with - get cooler with colour later...
    query = ChucksImage.all()
    query.order('-date_added')
    images = query.fetch(144)
    
    rows = self.grouper(n=12, iterable=images)
    path = os.path.join(os.path.dirname(__file__), 'main.html')
    values = { 'rows': rows }
    self.response.out.write(template.render(path, values))
