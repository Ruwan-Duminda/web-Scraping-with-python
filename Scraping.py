import requests
from bs4 import BeautifulSoup

/#web URL
url='https://topjobs.lk/'
response = requests.get(url)

soup = BeautifulSoup(response.text, 'html.parser')

#This will find the span class=job-link
site_titles = soup.findAll('span', attrs={"class":"job-link"})
#print all elements
for title in site_titles:
    print(title.text+"\n")
    #export to text file
    with open("Scraping.txt", "a",encoding="utf-8")as f:
        f.write(title.text+"\n")
    
    
