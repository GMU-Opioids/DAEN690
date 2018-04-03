import requests
from bs4 import BeautifulSoup
import csv

data = []

for i in range(1998,2018):
    page = requests.get('https://www.opensecrets.org/lobby/indusclient.php?id=H04&year=%s' % i)
    soup = BeautifulSoup(page.text, 'html.parser')
    table = soup.find('table', attrs={'id':'industry_summary'})
    table_body = table.find('tbody')
    rows = table_body.find_all('tr')
    for row in rows:
        cols = row.find_all('td')
        cols = [ele.text.strip() for ele in cols]
        cols.append(i)
        cols[1] = cols[1].replace(',','').replace('$','')
        data.append([ele for ele in cols if ele])

with open('lobby_data.csv','w') as f:
    csvwriter = csv.writer(f,delimiter=',',lineterminator='\n')
    csvwriter.writerow(['Company','Amount','Year'])
    csvwriter.writerows(data)
