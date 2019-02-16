"""
Grab credentials
"""
from pprint import pprint
from YouTubeTv import YouTubeTv



y = YouTubeTv()
data = y.scrape_for_data()
pprint(data)



