import requests
from bs4 import BeautifulSoup
import json

class IGHandel:
    def __init__(self,handel):
        self.url=f"https://www.instagram.com/{handel}/"
        self.response=requests.get(self.url)

        if self.response:
            self.soup=BeautifulSoup(self.response.content,"html.parser")
            self.info=self.soup.find('script', {'type': 'application/ld+json'})
            self.info=json.loads(self.info.string)

            self.meta_data=self.soup.find_all('meta')[-3].get('content')
            self.meta=self.meta_data.split(',')
            self.meta[2]=self.meta[2].split(" - ")
    #To get the user Name
    def Name(self):
        return self.info['author']['name']
    #To get the bio-data
    def Descripton(self):
        return self.info['description']
    #Link to profile image
    def ProfileImage(self):
        return self.info['author']['image']
    #Handler
    def AlternateName(self):
        return self.info['author']['alternateName']
    #No of followers
    def Followers(self):
        return self.meta[0].strip()
    #No of Following
    def Following(self):
        return self.meta[1].strip()
    #No of POst uploaded
    def Posts(self):
        return self.meta[2][0]
    def by(self):
        return "Vaibhav Pandey"
