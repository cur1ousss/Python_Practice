# example scraping static basic site
	# https://coreyms.com/
	# for more complex use scrapy , mechanize etc framework module

# use Beautiful Soup
# can use url lib inbuit module but requests library better

# Beautiful Soup
	# using L XML Parser here , html5 lib parser can also be used

# refer simple.html for scraping


# pass html into beautifulSoup to get an beautiful soup object
	# pass html as string
	# pass html file {example below local file}

from bs4 import BeautifulSoup
import requests
from requests.api import head

# since file in same directory can directly access no need to pass full path
with open('46_simple.html') as html_file:
	soup=BeautifulSoup(html_file,'lxml')
				# using lxml parser

	# soup is a BeautifulSoup object of our parsed html{? object of html}

print(soup)	# unformatted html prints like string all left aligned use pretify method to make more readable

print(soup.prettify())
		# prettify() method to print in human indented form readable

# getting info from html tag as an attribute

match=soup.title	# includes surrounding tags in op
print(match)

match=soup.title.text	# to get only text part
print(match)

match=soup.div # gets the first tag , to get more after this or specific tags we use find method
print(match)

# with find method() can pass in arguments of attributes that narrow down tag to find
match=soup.find('div')	# prints first found div
print(match)

match=soup.find('div',class_='footer') # use class_ {_ underscore} to differentiate from keyword class builtin
print(match)


article=soup.find('div',class_='article')
print(article)
	# we can access child tags with the dot access like an attribute or can use find method
headline=article.h2.a.text	# combine access in order to get innermost structure
print(headline)

summary=article.p
summary=article.p.text 	# to get only text content without p tags
print(summary)
	# can use find() or normal . to access attributes of article<> content

# find() returns only single first found tag , to get all use find_all() returns all tags that match those arguments as a list[]

for article in soup.find_all('div',class_='article'):
	headline=article.h2.a.text
	print(headline)

	summary=article.p.text
	print(summary)

	print('**********************************')


#*****************************************************************************
 
# using on actual website coreyms.com

from bs4 import BeautifulSoup
import requests

# get source code from website
source=requests.get('http://coreyms.com')
	# will return response object 
		# op - <Response [200]>
	# add .text to get html

source=requests.get('http://coreyms.com').text
		# .text gets html from site source code
print(source)

soup=BeautifulSoup(source,'lxml')
print(soup.prettify())

# getting single first headline and summary
	# using inspect F12 in browser to get details of specific tag object

article=soup.find('article')	# gets the first article tag
print(article.prettify())

headline=article.h2.a.text
print(headline)

# finding summary inside article tag so use find() method , using find() on article object not article html tag avoid confusion
summary=article.find('div',class_='entry-content').p.text
print(summary)

# getting link of youtube emebeded vid
	# generally in <iFrame>
		# if video url in embeded form of youtube need to get youtube id then make into legit 

vid_src=article.find('iframe',class_='youtube-player')
print(vid_src)
	# to get value of src="" attribute from the iframe tag
		# to get that value from attribute of a tag iframe then you can access it like an dicitionary 
vid_src=article.find('iframe',class_='youtube-player')['src']
					# instead of text use dictionary like specific access of key value
print(vid_src)
	# sanitise link
vid_id=vid_src.split('/')
	# split returns a list of broken string
		# use list index to access video id
vid_id=vid_src.split('/')[4]
vid_id=vid_id.split('?')[0]

print(vid_id)

yt_link=f'https://youtube.com/watch?v={vid_id}' 	# f strings from py 3.6 onwards
print(yt_link)
	
	#************************************************************  
# final Looping through all
from bs4 import BeautifulSoup
import requests

sourceCode=requests.get('http://coreyms.com').text
soup=BeautifulSoup(sourceCode,'lxml')
print(soup.prettify())

for article in soup.find_all('article'):
	headline=article.h2.a.text
	print(headline)
	summary=article.find('div',class_='entry-content').p.text
	print(summary)
	vid_src=article.find('iframe',class_='youtube-player')['src']
	vid_id=vid_src.split('/')[4]
	vid_id=vid_id.split('?')[0]
	
	yt_link=f'https://youtube.com/watch?v={vid_id}'

	print(yt_link)
	print('******************************************************')


# scraper may break if some non uniformity present example some link or image missing not expected by code throws error

from bs4 import BeautifulSoup
import requests

sourceCode=requests.get('http://coreyms.com').text
soup=BeautifulSoup(sourceCode,'lxml')
print(soup.prettify())

for article in soup.find_all('article'):
	headline=article.h2.a.text
	print(headline)
	summary=article.find('div',class_='entry-content').p.text
	print(summary)

	try:
		vid_src=article.find('iframe',class_='youtube-player')['src']
		vid_id=vid_src.split('/')[4]
		vid_id=vid_id.split('?')[0]
		yt_link=f'https://youtube.com/watch?v={vid_id}'
	except Exception as e:
		yt_link=None # can use pass as well	
		print('Link not present for this video')

	print(yt_link)
	print('******************************************************')


# saving Scraped data to CSV file or txt fil
from bs4 import BeautifulSoup
import requests
import csv

sourceCode=requests.get('http://coreyms.com').text
soup=BeautifulSoup(sourceCode,'lxml')
print(soup.prettify())

csv_file=open('46_cms_scrape.csv','w') 
	# can also use 'with' context manager to open file 

csv_writer=csv_writer(csv_file)

csv_writer.writerow(['headline','summary','video_link'])	# writing header to csv file / column names

for article in soup.find_all('article'):
	headline=article.h2.a.text
	print(headline)
	summary=article.find('div',class_='entry-content').p.text
	print(summary)

	try:
		vid_src=article.find('iframe',class_='youtube-player')['src']
		vid_id=vid_src.split('/')[4]
		vid_id=vid_id.split('?')[0]
		yt_link=f'https://youtube.com/watch?v={vid_id}'
	except Exception as e:
		yt_link=None # can use pass as well	
		print('Link not present for this video')

	print(yt_link)
	print('******************************************************')

	csv_writer.writerow([headline,summary,yt_link])

csv_file.close()