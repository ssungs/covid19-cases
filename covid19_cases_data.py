import requests
from bs4 import BeautifulSoup
import lxml

def Covid19_cases_data():
    url = 'https://en.wikipedia.org/wiki/Template:COVID-19_pandemic_data/South_Korea_medical_cases_chart'
    response = requests.get(url)
    html_text = response.text
    soup = BeautifulSoup(html_text, 'lxml')
    class_id = soup.find_all('tr', attrs={'id':'mw-customcollapsible-2021feb-l15'})
    return class_id


