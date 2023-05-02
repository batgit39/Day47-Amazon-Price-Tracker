import requests
from bs4 import BeautifulSoup 
import smtplib

URL = ""

my_email = ""
password = ""
# enter your details and add the link

def compare_prices(price):
    if price < 2300:
        send_mail()

def check_price():
    headers = { 
            'Accept-Language' : "en-US,en;q=0.5",
            'User-Agent': "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:109.0) Gecko/20100101 Firefox/112.0"
            # change these as per your browser
        }

    response = requests.get(url= URL, headers=headers)
    response.raise_for_status()
    website = response.text
    # print(response)

    soup = BeautifulSoup(response.content, "lxml")
    # print(soup.prettify())

    item_price = soup.find("span", class_="a-offscreen").getText().split('₹')[-1]

    print(item_price)
    converted_price = float(item_price.replace(",",""))
    return converted_price

def send_mail():
    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(user = my_email, password = password)
        connection.sendmail(
                from_addr = my_email,
                to_addrs = my_email,
                msg = f"Subject:Price Drop\n\nPrice drop on {URL}\nIts under the lowest price now, GO grab it :)"
                )

price = check_price()
# print(type(price))
compare_prices(price)
