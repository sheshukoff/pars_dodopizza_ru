import selenium
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
# from selenium.webdriver.common.by import By
# from selenium.webdriver.common.keys import Keys

import time
from bs4 import BeautifulSoup
from parser import find_url_cities, get_data_from_locality
from word_correction import get_correct_city


def get_page_soup_from_url(city_url):
    chrome_options = Options()  # после получение разметки можно не использовать
    chrome_options.add_argument('--no-sandbox')  # после получение разметки можно не использовать
    chrome_options.add_argument('--disable-dev-shm-usage')

    driver = webdriver.Chrome(options=chrome_options)  # после получение разметки можно не использовать
    URL = f"https://dodopizza.ru{city_url}"  # после получение разметки можно не использовать
    try:
        driver.get(URL)
    except selenium.common.exceptions.WebDriverException as error:
        print(f"адрес сайта не доступен или есть ошибка {URL}")
        exit(1)
    time.sleep(5)

    soup = BeautifulSoup(driver.page_source, 'html.parser')

    return soup


def write_file_from_soup(soup, name_city):
    with open(f"{name_city}.html", "w", encoding='utf-8') as file:  # делаем файл в html, чтобы дергать сайт лишний раз
        file.write(str(soup))

    print(name_city)


def main():
    all_url_cities = find_url_cities()  # получение всех возможных городов для парсинга
    all_correct_city = get_correct_city()
    print(all_correct_city)

    for city in all_correct_city:
        url_city = all_url_cities[city]
        soup_city = get_page_soup_from_url(url_city)
        write_file_from_soup(soup_city, city)
        file_name = f'{city}.html'
        get_data_from_locality(file_name)


if __name__ == '__main__':
    main()
