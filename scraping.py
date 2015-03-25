from lxml import html
import requests
import bs4
import re
for cat in range(29):
	catnumb = str(cat + 1)
	url = "http://www.publicsurplus.com/sms/all,va/browse/cataucs?catid=%s" % catnumb
	page = requests.get(url)
	soup = bs4.BeautifulSoup(page.text)
#	print "Cat: %s" % str(catnumb)
	if soup.find_all(text="No auctions found") == []:
		linelist = soup.find_all(href=re.compile("view\?"))
		for item in range(len(linelist)):
			auctionitem = str(linelist[item])
			auctionhtml = "http://www.publicsurplus.com/" + auctionitem[9:45]
			auctionpage = requests.get(auctionhtml)
			auctionsoup = bs4.BeautifulSoup(auctionpage.text)
			print auctionsoup.select("title")
			print auctionsoup.select("#auctionTitleLeftColumn")
			

#noauctions = soup.select('style="margin-left: 20px;"')

#print soup.find_all(text="No auctions found")
