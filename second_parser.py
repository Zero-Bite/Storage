# хотим спарсить поля с: 
# javascript
# cookie                         
# User-agent

import requests
import fake_useragent
import bs4

# введем замену user-agent
user = fake_useragent.UserAgent().random
headers = {"user-agent": user}

link = "https://browser-info.ru/"
response = requests.get(link, headers=headers)


if response.status_code == 200:

    all_data = {}

    soup = bs4.BeautifulSoup(response.text, 'lxml')

    # javascript state
    js_state = soup.find('div', id = "javascript_check")
    typ = js_state.text
    all_data["JavaScript"] = typ

    # cookie
    cookie_check = soup.find('div', id = "cookie_check").text
    all_data["Cookie"] = cookie_check

    #user-agent
    user_info = soup.find('div', id = "user_agent").text
    all_data["User-agent"] = user_info

for element in all_data:
    print(element)
