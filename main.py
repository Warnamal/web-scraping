from bs4 import BeautifulSoup
import requests

# with open ('home.html', 'r') as html_file:
#     content = html_file.read()

#     soup = BeautifulSoup(content, 'lxml')
#     tags = soup.find('form', class_='fm')
#     for tag in tags:
#         print(tag.text)

url = 'https://ikman.lk/en/ads/q/sri-lanka/motorcycle'
html_text = requests.get(url).text
# print(html_text.encode('utf-8'))

soup = BeautifulSoup(html_text, 'lxml')
bikes = soup.find_all('li', class_='normal--2QYVk')

for bike in bikes:
    # bike_model = bike.find('h2', class_='title--3yncE').text.replace(' ', '_')
    # location = bike.find('div', class_='description--2-ez3').text
    # price = bike.find('div', class_='price--3SnqI').text
    # published_date = bike.find('div', class_='updated-time--1DbCk').text

    published_date_element = bike.find('div', class_='updated-time--1DbCk')
    if published_date_element:
        published_date = published_date_element.text
    else:
        published_date = "N/A"

    if 'now' in published_date or 'minutes' in published_date or 'hour' in published_date:
        bike_model_element = bike.find('h2', class_='title--3yncE')
        if bike_model_element:
            bike_model = bike_model_element.text.replace(' ', '_')
        else:
            bike_model = "N/A"

        location_element = bike.find('div', class_='description--2-ez3')
        if location_element:
            location = location_element.text
        else:
            location = "N/A"

        price_element = bike.find('div', class_='price--3SnqI')
        if price_element:
            price = price_element.text
        else:
            price = "N/A"

        print("Bike Model:", bike_model)
        print("Location:", location)
        print("Price:", price)
        print()
