import requests
from bs4 import BeautifulSoup
# Page number
pageNum = 0
# Creating a list to store the URL of shopping mall website in yelp
shoppingMallURLList=[]

while pageNum <100:
    # Page url
    url="https://www.yelp.com/search?cflt=shopping&find_loc=Pittsburgh%2C%20PA&start="+str(pageNum)
    # Using BeautifulSoup to get the name tag of Html
    response =requests.get(url)
    soup = BeautifulSoup(response.text,'html.parser')
    shoppingURL=soup.find_all('a',class_="lemon--a__373c0__IEZFH link__373c0__29943 photo-box-link__373c0__1AvT5 link-color--blue-dark__373c0__1mhJo link-size--default__373c0__1skgq")

    # Storing the URL into the shoppingNameList
    for i in shoppingURL:
        if i['href'][1]=='b':
            shoppingMallURL ='https://www.yelp.com'+ i['href']
            shoppingMallURLList.append(shoppingMallURL)
    pageNum = pageNum+10

print(shoppingMallURLList)

