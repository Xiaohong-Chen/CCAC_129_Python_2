# Application programming interface(APIs)
## Prepared for DAT-129 at the Community College of Allegheny County

Creating a simple ptyhon programs which scrape data from

## Coding resources
[Python Requests module official documentation](http://docs.python-requests.org/en/master/)

## Uses for web scraping
* Learning the ins and outs of HTML
* Extracting data from website which don't run a fromal 

## image
![git](git.jpg)

      this is computer <code> that is automatically
      import requests
      from bs4 import BeautifulSoup

      shoppingList=[]
      pageNum = 0

      shoppingNameList=[]
      shoppingReviewList=[]

      while pageNum <50:

          url="https://www.yelp.com/search?cflt=shopping&find_loc=Pittsburgh%2C%20PA&start="+str(pageNum)
          pageNum = pageNum+10

          response =requests.get(url)
          soup = BeautifulSoup(response.text,'html.parser')
          shoppingName=soup.find_all('h3',class_="lemon--h3__373c0__sQmiG heading--h3__373c0__1n4Of alternate__373c0__1uacp")
          shoppingReview=soup.find_all('span',class_="lemon--span__373c0__3997G text__373c0__2pB8f reviewCount__373c0__2r4xT text-color--mid__373c0__3G312 text-align--left__373c0__2pnx_")


          for i in shoppingName:
              if(i.text != "u'STAAR Alert"):
                  shoppingNameList.append(i.text)

          for m in shoppingReview:
              shoppingReviewList.append(m.text)


      print(shoppingNameList)
      print(shoppingReviewList)
