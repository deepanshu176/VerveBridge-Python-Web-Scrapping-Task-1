import pandas as pd
import requests
from bs4 import BeautifulSoup

Product_name = []
Prices = []
Description = []
Reviews = []

for page_num in range(2, 12):
    url = f"https://www.flipkart.com/search?q=mobiles+under+50000&otracker=search&otracker1=search&marketplace=FLIPKART&as-show=on&as=off&page={page_num}"
    response = requests.get(url)
    
    if response.status_code == 200:
        soup = BeautifulSoup(response.text, "lxml")
        box = soup.find("div", class_="DOjaWF gdgoEp")
        
        if box:
            names = box.find_all("div", class_="KzDlHZ")
            for name in names:
                Product_name.append(name.text)
            
            prices = box.find_all("div", class_="Nx9bqj _4b5DiR")
            for price in prices:
                Prices.append(price.text)
            
            descs = box.find_all("ul", class_="G4BRas")
            for desc in descs:
                Description.append(desc.text)
            
            reviews = box.find_all("div", class_="XQDdHH")
            for review in reviews:
                Reviews.append(review.text)
        else:
            print(f"Element with the specified class name not found on page {page_num}.")
    else:
        print(f"Failed to retrieve the webpage. Status code: {response.status_code}")

min_length = min(len(Product_name), len(Prices), len(Description), len(Reviews))
Product_name = Product_name[:min_length]
Prices = Prices[:min_length]
Description = Description[:min_length]
Reviews = Reviews[:min_length]

df = pd.DataFrame({
    "Product Name": Product_name,
    "Prices": Prices,
    "Description": Description,
    "Reviews": Reviews
})

df.to_csv("D:/internship/flipkart_mobiles_50000.csv", index=False)
