import requests

link = 'https://browser-info.ru/'
response = requests.get(link)

if response.status_code == 200:
    print("----Connected----")
    with open("data_about.html", "w", encoding="utf-8") as file:
        file.write(response.text)
