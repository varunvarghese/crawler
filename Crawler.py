import re
import sys
import time
import math
import urllib2
import urlparse
import optparse
from cgi import escape
from traceback import format_exc
from Queue import Queue, Empty as QueueEmpty

from BeautifulSoup import BeautifulSoup

__version__ = '0.2'
__copyright__ = 'Copyright (C) 2008-2011 by James Mills'
__license__ = 'MIT'
__author__ = 'James Mill'

USAGE = "%prog [options] <url>"
VERSION = "%prog v" + __version__


AGENT = "%s/%s" % (__name__,__version__)


class Crawler(object):
	def __init__(self, root, depth, locked=True):
		self.root = root
		self.depth = depth
		self.locked = locked
		self.host = urlparse.urlparse(root)[1]
		self.urls = []
		self.links = 0
		self.followed = 0


	def crawl(self):
		page = Fetcher(self.root)
		page.fetch()
		q = Queue()
		for url in page.urls:
			q.put(url)
		followed = [self.root]

		n = 0
