# This code grabs a list of lobbyists registered in the city of Pittsburgh.
# It only pulls in those with the last name "A" at this point. Need to edit code so that it pages 
# through the site to get all the names.

import urllib
from bs4 import BeautifulSoup

url_a = 'http://www.openbookpittsburgh.com/Lobbyists.aspx?lobbyist=a&page=0&cat=LobbyistID&sort=DESC&num=100'

web_cnx = urllib.urlopen(url_a)

html = web_cnx.read()

soup = BeautifulSoup(html)

table = soup.find(id='table')

rows = table.find_all(tag.name = 'tr')

headers = rows[0].find_all('th')

columns = []

for header in headers:
	columns.append(header.text)

print '\t'.join(columns)

for row in rows[1:]:
	data = row.findAll('td')

	full_name = data[1].text
	position = data[2].text
	employer = data[3].text
	add_companies = data[4].text
	status = data[5].text

	print "\t".join([full_name, position, employer, add_companies, status])


