from splinter import Browser
from bs4 import BeautifulSoup
import pandas as pd
import datetime as dt 
import time
import re
import json
import time


def marsScraper():

    executable_path = {'executable_path': "C:/Users/kylec/Desktop/chromedriver.exe"}
    browser = Browser('chrome', **executable_path, headless=True)
    
    #Mars News
    url = 'https://mars.nasa.gov/news/'
    browser.visit(url)
    
    html = browser.html
    soup = BeautifulSoup(html, "html.parser")
    
    news = soup.find("li", class_='slide')

    # newsTitle = news.find('div',class_="content_title").get_text()
    
    newsTeaser = soup.find("div",class_="article_teaser_body")
    
    #Picture
    imageUrl = 'https://www.jpl.nasa.gov/spaceimages/?search=&category=Mars'
    browser.visit(imageUrl)
    imageHtml = browser.html
    soups = BeautifulSoup(imageHtml, "lxml")
    
    images = soups.find_all(class_="carousel_item")
    imageURL = 'https://www.jpl.nasa.gov' + images[0]["style"].split(" ")[1].split("'")[1]
    
    #Twitter (I stole this from Alexander completely)
    twitterUrl = 'https://twitter.com/marswxreport?lang=en'
    browser.visit(twitterUrl)
    twitterHtml = browser.html
    soupss = BeautifulSoup(twitterHtml, "lxml")
    
    allTweets = soupss.find_all("span")
    tweetText = ""
    for tweet in allTweets:
        if tweet.text:
            if "InSight sol" in tweet.text:
                tweetText = tweet.text
                break
    
    #Mars Facts
    factsUrl = 'https://space-facts.com/mars/'
    browser.visit(factsUrl)
    factsHtml = browser.html
    dfs = pd.read_html(factsHtml)
    stats = dfs[0]
    stats.columns = ["Attribute", "Value"]
    
    #format and save
    data_html = stats.to_html(index=False)
    data_stats = json.loads(stats.to_json(orient="records"))

    #Closing Browser
    browser.quit()
    
    #Returning Dictionary
    retDict = {
        # "newsTitle": newsTitle,
        "newsTeaser": newsTeaser,
        "featureImageURL": imageURL,
        "marsStats": data_stats,
        "dateScraped": dt.datetime.now()
    }
    
    return retDict

if __name__ == "__main__":
    print(marsScraper())