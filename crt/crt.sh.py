import requests
from bs4 import BeautifulSoup

x = ("https://crt.sh/?q=")

print('''\

                                                                                                 ,---.-,
                                                                                                '   ,'  '.    ,---.-,
   ,---,                                                                                       /   /      \  '   ,'  '.
  '  .' \                   ,---,                                                             .   ;  ,/.  : /   /      \
 /  ;    '.      __  ,-.  ,---.'|                                                             '   |  | :  ;.   ;  ,/.  :
:  :       \   ,' ,'/ /|  |   | :               .--.--.                 .--.--.               '   |  ./   :'   |  | :  ;
:  |   /\   \  '  | |' |  |   | |   ,--.--.    /  /    '    ,--.--.    /  /    '    ,--.--.   |   :       ,'   |  ./   :
|  :  ' ;.   : |  |   ,',--.__| |  /       \  |  :  /`./   /       \  |  :  /`./   /       \   \   \     / |   :       ,
|  |  ;/  \   \'  :  / /   ,'   | .--.  .-. | |  :  ;_    .--.  .-. | |  :  ;_    .--.  .-. |   ;   ,   '\  \   \      |
'  :  | \  \ ,'|  | ' .   '  /  |  \__\/: . .  \  \    `.  \__\/: . .  \  \    `.  \__\/: . .  /   /      \  `---`---  ;
|  |  '  '--'  ;  : | '   ; |:  |  ," .--.; |   `----.   \ ," .--.; |   `----.   \ ," .--.; | .   ;  ,/.  :     |   |  |
|  :  :        |  , ; |   | '/  ' /  /  ,.  |  /  /`--'  //  /  ,.  |  /  /`--'  //  /  ,.  | '   |  | :  ;     '   :  ;
|  | ,'         ---'  |   :    :|;  :   .'   \'--'.     /;  :   .'   \'--'.     /;  :   .'   \'   |  ./   :     |   |  '
`--''                  \   \  /  |  ,     .-./  `--'---' |  ,     .-./  `--'---' |  ,     .-./|   :      /      ;   |.'
                        `----'    `--`---'                `--`---'                `--`---'     \   \   .'       '---'
                                                                                                `---`-'
ÇIKMAK İÇİN CTRL + C YAPIN
Discord: Jack 1#1321 eğer çalışmaz ise :) discord.gg/hormon sunucusuna gelerek soru sorabilirsiniz cevaplarım
If code doesn't work, please come to my Discord server and let me know about the error you're experiencing''')

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
