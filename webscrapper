import requests # it helps to download the html file
from bs4 import BeautifulSoup # helps to utilize the html file
import pprint

res=requests.get('https://news.ycombinator.com/')
res2=requests.get('https://news.ycombinator.com/news?p=2')
# print(res.text) . here we get the text which is on the hackernews website
# now we are modifying the res.text to the html file , that we can actually use
soup=BeautifulSoup(res.text,'html.parser') # we parse the res.text to the html file
soup2=BeautifulSoup(res2.text,'html.parser')
# print(soup.body) . here we get only the body of soup.
# print(soup.find_all('div')) . we get all the div objects
# print(soup.title) . we can get the title of the website which is <title>Hacker News</title>
# print(soup.select('.score')) . here we get all the scores . the dot stands for class
# print(soup.select('.storylink')[0]) <a class="storylink" href="https://www.mattkeeter.com/blog/2021-03-01-happen/">It Can Happen to You</a>
# so the storylink grabs you the first link , which is present in the hackernews website
links=soup.select('.storylink')
subtext=soup.select('.subtext')
links2=soup2.select('.storylink')
subtext2=soup2.select('.subtext')
mega_links=links+links2
mega_subtext=subtext+subtext2

def sort_news_by_votes(hackernewslist):
    return sorted(hackernewslist,key=lambda k:k['votes'],reverse=True)

def create_custom_hackernews_website(links,subtext):
    hackernews=[]
    for index,item in enumerate(links):
        title=item.getText() # getting the title
        href=item.get('href',None)  # getting the links . here we use the href because in the website the links are in the href form
        vote=subtext[index].select('.score')  # we are getting the votes
        if len(vote):
            points=int(vote[0].getText().replace(' points', ''))
            if points>99:
                hackernews.append({'title':title,'link':href,'votes':points})
    return sort_news_by_votes(hackernews)
pprint.pprint(create_custom_hackernews_website(mega_links,mega_subtext))
