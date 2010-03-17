#!/usr/bin/env python
# encoding: utf-8

import sys, os
import urlparse
import urllib2
import urllib
import csv

file_name = sys.argv[1]

# Gets a medium sized image given farm, server, id and secret
# http://farm{farm-id}.static.flickr.com/{server-id}/{id}_{secret}_[mstb].jpg
def get_image_url(farm, server, id, secret):
  return 'http://farm%s.static.flickr.com/%s/%s_%s_m.jpg' % (farm, server, id, secret)

def get_image(url):
  fn = url.split("/")[-1]
  outpath = os.path.join("../../chuckstribute-img-data/", fn)
  urllib.urlretrieve(url, outpath)

def get_images(file_name):
  ir = csv.reader(open(file_name))
  num = 0
  for i in ir:
    get_image(get_image_url(i[3], i[2], i[0], i[1]))
    print 'Downloaded image with ID %s' % i[0]
    num += 1
  print 'Completed saving %d images.' % num

def main():
  get_images(file_name)

if __name__ == '__main__':
  main()
