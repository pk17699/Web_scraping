from bs4 import BeautifulSoup
import requests
import pandas as pd
products = []
prices = []
ratings = []
discounts = []
n = input("Enter number of pages : ")
for i in range(1, int(n) + 1):
    response = requests.get('https://www.flipkart.com/search?q=best%20laptops&otracker=search&otracker1=search&marketplace=FLIPKART&as-show=on&as=' + str(i))
    soup = BeautifulSoup(response.content, 'html.parser')
    for a in soup.find_all('a', attrs = {'class':'_1fQZEK'}):
        name = a.find('div', attrs={'class': '_4rR01T'})
        products.append(name.text)
        price = a.find('div', attrs={'class': '_30jeq3 _1_WHN1'})
        prices.append(int(price.text[1:].replace(',','')))
        rating = a.find('div', attrs={'class': '_3LWZlK'})
        if rating is not None:
            ratings.append(rating.text)
        else:
            ratings.append('N/A')
        offer = a.find('div', attrs={'class': '_3Ay6Sb'})
        if offer is not None:
            discounts.append(offer.text)
        else:
            discounts.append('0')
df = pd.DataFrame({'product name': products, 'Price': prices, 'Rating': ratings, 'offer': discounts})
output = df.sort_values(by = 'Price')
output.to_excel('best_laptops_on_flipkart.xlsx', index=False, encoding='utf-8')
