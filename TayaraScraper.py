import Car
import requests
from bs4 import BeautifulSoup
import csv
from itertools import zip_longest
from urllib.parse import urljoin
import time

class TayaraScraper:
    def __init__(self, max_pages=300, delay=2):
        self.base_url = "https://www.tayara.tn"
        self.links = []
        self.cars = []
        self.max_pages = max_pages
        self.delay = delay

    def scrape_links(self):
        nbr_page = 1
        while nbr_page <= self.max_pages:
            result = requests.get(f"https://www.tayara.tn/fr/ads/c/V%C3%A9hicules/Voitures/?minPrice=100&page={nbr_page}")
            src = result.content
            soup = BeautifulSoup(src, 'lxml')
            articles = soup.find_all('article', {'class': 'mx-0'})
            for data in range(len(articles)):
                self.links.append(articles[data].find('a').attrs['href'])
            nbr_page += 1
            print("Page switched " + str(nbr_page))

            # Introduce a delay between requests
            time.sleep(self.delay)

    def scrape_cars(self):
        for link in self.links:
            car = Car.Car()
            full_url = urljoin(self.base_url, link)

            result = requests.get(full_url)
            src = result.content
            soup = BeautifulSoup(src, "lxml")

            try:
                spans = soup.find_all('span', {"class": "mr-1"})
                s = ""
                for span in spans:
                    s += span.text
                car.prix = s
            except:
                car.prix = "NULL"

            li = soup.find_all('li', {"class": "col-span-6 lg:col-span-3"})
            # get kilometre
            try:
                kilometre_li = li[0]
                spans = kilometre_li.find_all("span", {"class": "flex flex-col py-1"})
                for span_container in spans:
                    span = span_container.find("span", {
                        "class": "text-gray-700/80 text-xs md:text-sm lg:text-sm font-semibold"})
                    car.kilo = span.text.strip()
            except:
                car.kilo = "NULL"

            # get color
            try:
                color_li = li[1]
                spans = color_li.find_all("span", {"class": "flex flex-col py-1"})
                for span_container in spans:
                    span = span_container.find("span", {
                        "class": "text-gray-700/80 text-xs md:text-sm lg:text-sm font-semibold"})
                    car.color = span.text.strip()
            except:
                car.color = "NULL"

            # get type of boite
            try:
                boite_li = li[3]
                spans = boite_li.find_all("span", {"class": "flex flex-col py-1"})
                for span_container in spans:
                    span = span_container.find("span", {
                        "class": "text-gray-700/80 text-xs md:text-sm lg:text-sm font-semibold"})
                    car.boite = span.text.strip()
            except:
                car.boite = "NULL"

            # get année
            try:
                annee_li = li[4]
                spans = annee_li.find_all("span", {"class": "flex flex-col py-1"})
                for span_container in spans:
                    span = span_container.find("span", {
                        "class": "text-gray-700/80 text-xs md:text-sm lg:text-sm font-semibold"})
                    car.annee = span.text.strip()
            except:
                car.annee = "NULL"

            # get cylindre
            try:
                cylindre_li = li[5]
                spans = cylindre_li.find_all("span", {"class": "flex flex-col py-1"})
                for span_container in spans:
                    span = span_container.find("span", {
                        "class": "text-gray-700/80 text-xs md:text-sm lg:text-sm font-semibold"})
                    car.cylindre = span.text.strip()
            except:
                car.cylindre = "NULL"

            # get Marque
            try:
                marque_li = li[6]
                spans = marque_li.find_all("span", {"class": "flex flex-col py-1"})
                for span_container in spans:
                    span = span_container.find("span", {
                        "class": "text-gray-700/80 text-xs md:text-sm lg:text-sm font-semibold"})
                    car.marque = span.text.strip()
            except:
                car.marque = "NULL"

            # get modele
            try:
                modele_li = li[7]
                spans = modele_li.find_all("span", {"class": "flex flex-col py-1"})
                for span_container in spans:
                    span = span_container.find("span", {
                        "class": "text-gray-700/80 text-xs md:text-sm lg:text-sm font-semibold"})
                    car.modele = span.text.strip()
            except:
                car.modele = "NULL"

            # get puissance
            try:
                puissance_li = li[8]
                spans = puissance_li.find_all("span", {"class": "flex flex-col py-1"})
                for span_container in spans:
                    span = span_container.find("span", {
                        "class": "text-gray-700/80 text-xs md:text-sm lg:text-sm font-semibold"})
                    car.puissance = span.text.strip()
            except:
                car.puissance = "NULL"

            # get carburant
            try:
                carburant_li = li[10]
                spans = carburant_li.find_all("span", {"class": "flex flex-col py-1"})
                for span_container in spans:
                    span = span_container.find("span", {
                        "class": "text-gray-700/80 text-xs md:text-sm lg:text-sm font-semibold"})
                    car.carburant = span.text.strip()
            except:
                car.carburant = "NULL"

            self.cars.append(car)

    def display_cars(self):
        for i in range(len(self.cars)):
            print(f"Car {i + 1}: {self.cars[i]}")

    def export_to_csv(self, csv_path):
        file_list = [
            [getattr(car, "marque", "NULL") for car in self.cars],
            [getattr(car, "modele", "NULL") for car in self.cars],
            [getattr(car, "kilo", "NULL") for car in self.cars],
            [getattr(car, "color", "NULL") for car in self.cars],
            [getattr(car, "boite", "NULL") for car in self.cars],
            [getattr(car, "annee", "NULL") for car in self.cars],
            [getattr(car, "cylindre", "NULL") for car in self.cars],
            [getattr(car, "puissance", "NULL") for car in self.cars],
            [getattr(car, "carburant", "NULL") for car in self.cars],
            [getattr(car, "prix", "NULL") for car in self.cars]
        ]

        exported = zip_longest(*file_list, fillvalue="")

        with open(csv_path, "w", newline='', encoding='utf-8') as myfile:
            wr = csv.writer(myfile)
            wr.writerow(["Marque_voiture", "Modele", "Kilometrage", "Couleur", "TypeBoite", "Annee", "Cylindre",
                         "Puissance", "Carburant", "Prix"])
            wr.writerows(exported)

        print(f"The CSV file has been created successfully: {csv_path}")


# Instantiate the class and use its methods
# scraper = TayaraScraper()
# scraper.scrape_links()
# scraper.scrape_cars()
# scraper.display_cars()
# scraper.export_to_csv("C:/Users/ayari/NoteBook_Py/Py_Ensi/PS_Tayara/voitures.csv")
