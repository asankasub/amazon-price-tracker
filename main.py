from bs4 import BeautifulSoup
import requests
import lxml
import smtplib
import os
my_email = os.environ.get("my_email")
my_pass = os.environ.get("my_pass")
user_agent = os.environ.get("user_agent")
acc_lang = os.environ.get("acc_lang")
url="https://www.amazon.com/High-Back-Chair-Office-Ergonomic-Executive/dp/B07KJYY9BD/ref=sr_1_4?crid=37KH3Z1YBAS0J&keywords=gaming+chairs&qid=1663904184&sprefix=gaming+cha%2Caps%2C360&sr=8-4"
headers = {
    "Accept-Language": acc_lang,
    "User-Agent": user_agent
}

response = requests.get(url=url,headers=headers)
link = response.text
soup=BeautifulSoup(link,'lxml')

price = float((soup.find(name="span", class_="a-offscreen").getText()).replace("$",""))


target_price = 102

if price <= target_price:

    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(my_email, my_pass)
        connection.sendmail(from_addr=my_email, to_addrs=my_email, msg=f"Subject: Amazon price update for The High-Back Gaming Chair\n\nThe High-Back Gaming Chair is ${price}.\n{url} ")
