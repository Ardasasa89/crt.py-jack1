import requests
from bs4 import BeautifulSoup

x = ("https://crt.sh/?q=")

#Kullanıcıdan Link Al
mail = input("Lütfen Siteyi Giriniz!")
mail = x + mail 

#işlerimizi yapalım 
response = requests.get(mail)
html_content = response.content

response = requests.get(mail)
soup = BeautifulSoup(response.content, "html.parser")

br_tags = soup.find_all("br")
td_tags = soup.find_all("td")

for tag in br_tags:
    next_element = tag.next_sibling
    if next_element is not None and callable(next_element.strip):
        print(next_element.strip())


for td_tag in td_tags:
    # Bütün TD tagli yazıları al
    td_text = td_tag.get_text(strip=True)
    
    # eğer td td text boş değilse yazdır
    if td_text:
        print(td_text)

input("uygulama kapnması için ctrl + c yapınız")
