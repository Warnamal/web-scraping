from bs4 import BeautifulSoup
import requests
import time

# with open ('home.html', 'r') as html_file:
#     content = html_file.read()

#     soup = BeautifulSoup(content, 'lxml')
#     tags = soup.find('form', class_='fm')
#     for tag in tags:
#         print(tag.text)


def find_bikes():
    max_price = int(input('Put your maximum price: '))
    print(f'Searching bikes under Rs {max_price}')
    print('')

    url = 'https://ikman.lk/en/ads/q/sri-lanka/motorcycle'
    html_text = requests.get(url).text
    # print(html_text.encode('utf-8'))

    # soup = BeautifulSoup(html_text, 'lxml')
    soup = BeautifulSoup(html_text, 'html.parser')
    bikes = soup.find_all('li', class_='normal--2QYVk')

    for index, bike in enumerate(bikes):
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
                location = location_element.text.split()[0].strip(',')
            else:
                location = "N/A"

            price_element = bike.find('div', class_='price--3SnqI')
            if price_element:
                price = price_element.text
            else:
                price = "N/A"

            price_numeric = int(''.join(filter(str.isdigit, price))) if price != "N/A" else 0

            link = bike.a['href']

            if price_numeric <= max_price:
                with open(f'post/{index}.txt', 'w') as f:
                    f.write(f"Bike Model: {bike_model} \n")
                    f.write(f"Location: {location} \n")
                    f.write(f"Price: {price} \n")
                    f.write(f"More Info: https://ikman.lk {link} \n")
                print(f'File saved: {index}')


if __name__ == '__main__':
    while True:
        find_bikes()
        time_waite = 5
        print(f'Waiting {time_waite} minutes...')
        time.sleep(time_waite * 60)