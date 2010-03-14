#!/usr/bin/env python
# encoding: utf-8

import sys, os
from datetime import datetime, date, time
import urllib2
import json

flickr_api_key = '43d8da805db522b18f28040f55cfd020'
flickr_query = 'chuck+taylor+shoe'
sort = 'interestingness-desc'
# Change this for subsequent queries
page_number = 3

flickr_url = 'http://api.flickr.com/services/rest/?method=flickr.photos.search&api_key=%s&text=%s&page=%d&sort=%s&format=json&nojsoncallback=1' % (flickr_api_key, flickr_query, page_number, sort)

# File name format: flickr-chucks-<page-number>-<yyyymmddhhmmss>.csv
file_name_format = 'flickr-chucks-%d-%s.csv'
file_record_format = '%s,%s,%s,%s,%s\n'

def get_file_name(page_number):
  return file_name_format % (page_number, datetime.now().strftime("%Y%m%d%H%M%S"))

def get_chucks_images():
  req = urllib2.Request(url=flickr_url)
  opener = urllib2.build_opener()
  f = opener.open(req)
  json_data = json.load(f)
  print 'Found %s pages of photos (100 photos per page)' % json_data['photos']['pages']
  return json_data['photos']['photo']

def write_data():
  chucks = get_chucks_images()
  fn = get_file_name(page_number)
  with open(fn, 'w') as f:
    for c in chucks:
      print 'Writing image with ID %s' % c['id']
      f.write(file_record_format % (c['id'], c['secret'], c['server'], c['farm'], c['owner']))
  print 'Completed writing %d image records to %s' % (len(chucks), fn)

def main():
  write_data()

if __name__ == '__main__':
  main()
