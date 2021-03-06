#!/usr/bin/env python

from google.appengine.ext import webapp
from google.appengine.ext.webapp import util

from handlers import MainHandler

def main():
  application = webapp.WSGIApplication(
    [('/', MainHandler)], debug=True)
  util.run_wsgi_app(application)

if __name__ == '__main__':
  main()
