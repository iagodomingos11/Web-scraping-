import requests
from bs4 import BeautifulSoup
import json

url = 'https://books.toscrape.com/'

response = requests.get(url)
soup = BeautifulSoup(response.text, 'html.parser')

livros = []

for item in soup.select('.product_pod'):
    titulo = item.h3.a['title']
    preco = item.select_one('.price_color').text
    livros.append({'ulo': titulo, 'preco': preco})

# Salvando em JSON
with open('livros.json', 'w', encoding='utf-8') as f:
    json.dump(livros, f, ensure_ascii=False, indent=4)

print('Scraping concluído. Livros salvos em livros.json.')