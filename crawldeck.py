import requests
from bs4 import BeautifulSoup

def check_career(str):
    if 'エルフ' in str:
        return "精靈"
    if 'ロイヤル' in str:
        return "皇家"
    if 'ウィッチ' in str:
        return "巫師"
    if 'ドラゴン' in str:
        return "龍族"
    if 'ネクロ' in str:
        return "死靈"
    if 'ヴァンプ' in str:
        return "吸血鬼"
    if 'ビショップ' in str:
        return "主教"
    if 'ネメシス' in str:
        return "復仇者"

def load():
    career = {}
    url = {}
    tier = []
    deck_list = []
    gamewith = "https://shadowverse.gamewith.jp/article/show/84174"
    response = requests.get(gamewith)
    soup = BeautifulSoup(response.text ,'html.parser')
    tier_list = soup.find_all("div",{"class":"sv_saikyo_table"})

    curr = 1
    for i in tier_list:
        tr = i.find_all("tr")
        del tr[0]
        tmp = []
        for item in tr:
            a = item.find("a")
            deck_name = a.text
            tmp.append(deck_name)
            career[deck_name] = check_career(deck_name)
            url[deck_name] = a["href"]
            deck_list.append(deck_name)
        curr = curr + 1
        tier.append(tmp)
    
    return [career,url,tier,deck_list]

def load_pro_deck():
    pro_deck = "https://shadowverse.gamewith.jp/article/show/44584"
    response = requests.get(pro_deck)
    soup = BeautifulSoup(response.text ,'html.parser')

    url = {}
    deck_list = soup.find_all("section",{"class":"w-idb-element"})[:10]
    list = []
    for i in deck_list:
        tr = i.find_all("tr")
        a = tr[0].find("a")
        name = a.text
        user = tr[1].text[:-2]
        title = tr[0].find_all("td")[1].text
        date = tr[2].text[5:]
        url[f"{date}{title} {user} {name}"] = a["href"]
        list.append([date,title,user,name])

    return [list,url]

def get_pro_deck_recipe(url,career):
    response = requests.get(url)
    soup = BeautifulSoup(response.text ,'html.parser')