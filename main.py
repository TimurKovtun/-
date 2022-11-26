from bs4 import BeautifulSoup
import requests
response = requests.get("https://bank.gov.ua")

kurs_NBU =""
if response.status_code == 200:
    soup = BeautifulSoup(response.text,features="html.parser")
    soup_list = soup.find_all("div", {"class": "col-xs-4"})
    res = soup_list[3].find("div")

for kurs in res.text.strip():
    if kurs != " ":
        kurs_NBU += kurs
    if kurs == "\n":
        break
print (kurs_NBU)