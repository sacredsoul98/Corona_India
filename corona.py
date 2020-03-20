import bs4 
import requests

from bs4 import BeautifulSoup

r=requests.get('https://covidout.in/')

soup=BeautifulSoup(r.content,'html.parser')
#print(soup.prettify())

cases=soup.find('div', {'class':'cases-container'}).find('h2',{'class':'case'}).text

rec=soup.find('div',{'class':'card-body status-recovered'}).find('h2',{'class':'case'}).text

ICU=soup.find('div',{'class':'card-body status-icu'}).find('h2',{'class':'case'}).text

ded=soup.find('div',{'class':'card-body status-died'}).find('h2',{'class':'case'}).text

print('Total numer of cases in India-')
print(cases)

print('Recovered-')
print(rec)

print('In ICU-')
print(ICU)

print('Dead-')
print(ded)