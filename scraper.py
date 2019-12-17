
# - - - Brandhunt External Scraper - - -
# ---> Used for fetching clothing information from various clothing sites!

# --- IMPORT SECTION --- #

import scraperwiki
import lxml.html
import os

#  Connect to Wordpress Site via REST API and get all the proper URLs to be scraped!

wp_username = os.environ['MORPH_WP_USERNAME']
wp_password = os.environ['MORPH_WP_PASSWORD']
wp_connectwp_url = os.environ['MORPH_WP_RAPI_URL']

token = base64.standard_b64encode(wp_username + ':' + wp_password)
headers = {'Authorization': 'Basic ' + token}

#r = requests.post(wp_connectwp_url, headers=headers, json=post)
r = requests.get(wp_connectwp_url, headers=headers)
#print('Your post is published on ' + json.loads(r.content)['link'])
#print('Data found: ' + json.loads(r.content)['link'])
print('Data found: ' + r.json())

# # Read in a page
# html = scraperwiki.scrape("http://foo.com")
#
# # Find something on the page using css selectors
# root = lxml.html.fromstring(html)
# root.cssselect("div[align='left']")
#
# # Write out to the sqlite database using scraperwiki library
# scraperwiki.sqlite.save(unique_keys=['name'], data={"name": "susan", "occupation": "software developer"})
#
# # An arbitrary query against the database
# scraperwiki.sql.select("* from data where 'name'='peter'")

# You don't have to do things with the ScraperWiki and lxml libraries.
# You can use whatever libraries you want: https://morph.io/documentation/python
# All that matters is that your final data is written to an SQLite database
# called "data.sqlite" in the current working directory which has at least a table
# called "data".
