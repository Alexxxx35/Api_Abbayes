import os, re, requests
from bs4 import BeautifulSoup
from selenium.webdriver.common.keys import Keys
from selenium import webdriver

# BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
# NAV_DIR = os.path.abspath(os.path.join(BASE_DIR, '../Mozilla Firefox'))
# print(NAV_DIR)
from selenium.webdriver.firefox.firefox_binary import FirefoxBinary

# binary = FirefoxBinary('D:\\Mozilla Firefox\\firefox.exe')
# driver = webdriver.Firefox(firefox_binary=binary, executable_path=r"D:\\DEVOP\\CHRIST\\Drivers\\geckodriver.exe")
# driver.get(url)
# print(driver.title)
# driver.close()

url = "https://fr.wikipedia.org/wiki/Liste_des_abbayes,_monast%C3%A8res_et_couvents_en_France"
API_list = []
all_data_abbaye_list = []
dictionary_main_regions_secondary_regions = {}
dictionary_secondary_regions_abbayes = {}
string_ref = "https://fr.wikipedia.org"
soup = BeautifulSoup(requests.get(url).text, 'lxml')
# print(soup.prettify())

main_regions = [e.text for e in soup.find("div", {"class": "mw-parser-output"}).find_all(
    ["h2", "span", {"class": "mw-headline"}, "a"], recursive=False)]
# regions = soup.find_all("span", {"class": "mw-headline"})
abbayes_pattern = re.compile(r"Abbaye[a-zA-Zèé' -]+")

waste = re.compile(r"\[(.*?)\]")
main_regions = ([waste.sub("", e) for e in main_regions])
main_regions = main_regions[:-2]
# print("liste des régions principales: ", main_regions)

secondary_regions = [e.text for e in soup.find("div", {"class": "mw-parser-output"}).find_all(
    ["h3", "span", {"class": "mw-headline"}, "a"], recursive=False)]
secondary_regions = ([waste.sub("", e) for e in secondary_regions])
secondary_regions = secondary_regions[:-2]
print("liste des régions secondaires: ", secondary_regions)

all_abbayes = [e.text for e in soup.find("div", {"class": "mw-parser-output"}).find_all(
    ["ul", "li"])]
waste2 = re.compile(r"\([^\)]+\)")
all_abbayes = [e.replace("\xa0", "") for e in all_abbayes]
all_abbayes = [e.replace("\n", "") for e in all_abbayes]
all_abbayes = [e.replace("esiècle", "ème siècle") for e in all_abbayes]
all_abbayes = [e.replace("(royale, archives AD)", "") for e in all_abbayes]
all_abbayes = [e.replace("(archives AD)", "") for e in all_abbayes]
all_abbayes = list(filter(abbayes_pattern.match, all_abbayes))
print("liste des abbayes francaise: ", all_abbayes)

all_href = [a['href'] for a in soup.find("div", {"class": "mw-parser-output"}).find_all(["ul", "li", "a"], href=True)]
abbayes_href_pattern = re.compile(r"\/wiki\/Abbaye_[\w_-]+")
abbaye_href_filtre = list(filter(abbayes_href_pattern.match, all_href))
abbaye_href_filtre = [string_ref + e for e in abbaye_href_filtre]
# print("liste des tous les liens http contenant les informations historiques: ", abbaye_href_filtre)

# print("dictionnaire représentatif de la répartition géographique des abbayes: ",
#       dictionary_abbayes_per_secondary_region)
# for e in main_regions:
#     API_list.append(dictionary_abbayes_per_secondary_region)
# print(API_list)

dictionary_main_regions_secondary_regions[main_regions[0]] = secondary_regions[:13]
dictionary_main_regions_secondary_regions[main_regions[1]] = secondary_regions[14:21]
dictionary_main_regions_secondary_regions[main_regions[2]] = secondary_regions[21:25]
dictionary_main_regions_secondary_regions[main_regions[3]] = secondary_regions[25:31]
dictionary_main_regions_secondary_regions[main_regions[5]] = secondary_regions[31:41]
dictionary_main_regions_secondary_regions[main_regions[6]] = secondary_regions[41:46]
dictionary_main_regions_secondary_regions[main_regions[7]] = secondary_regions[46:53]
dictionary_main_regions_secondary_regions[main_regions[8]] = secondary_regions[53:58]
dictionary_main_regions_secondary_regions[main_regions[9]] = secondary_regions[58:70]
dictionary_main_regions_secondary_regions[main_regions[10]] = secondary_regions[70:83]
dictionary_main_regions_secondary_regions[main_regions[11]] = secondary_regions[83:88]
dictionary_main_regions_secondary_regions[main_regions[12]] = secondary_regions[88:]
print("dictionnaire géographique: ", dictionary_main_regions_secondary_regions)

dictionary_secondary_regions_abbayes[secondary_regions[0]]=all_abbayes[0:7]
dictionary_secondary_regions_abbayes[secondary_regions[1]]=all_abbayes[8]
dictionary_secondary_regions_abbayes[secondary_regions[2]]=all_abbayes[9:16]
dictionary_secondary_regions_abbayes[secondary_regions[3]]=all_abbayes[16:20]
dictionary_secondary_regions_abbayes[secondary_regions[4]]=all_abbayes[20:23]
dictionary_secondary_regions_abbayes[secondary_regions[5]]=all_abbayes[23:29]
print(dictionary_secondary_regions_abbayes)

for e in abbaye_href_filtre:
    soup = BeautifulSoup(requests.get(e).text, 'lxml')
    abbaye_data = soup.find_all("p")
    abbaye_data_list_text = [e.text for e in abbaye_data]
    abbaye_data_list_text = abbaye_data_list_text[1:]
    abbaye_data_list_text = [e.replace("\n", "") for e in abbaye_data_list_text]
    abbaye_data_list_text = [e.replace("\xa0", "") for e in abbaye_data_list_text]
    abbaye_data_list_text = [e.replace("Ier", "Ier ") for e in abbaye_data_list_text]
    abbaye_data_list_text = [e.replace("esiècle", "ème siècle") for e in abbaye_data_list_text]
    abbaye_data_list_text = [e.replace(".", ". ") for e in abbaye_data_list_text]
    abbaye_data_list_text = [e + e for e in abbaye_data_list_text]
    abbaye_data_list_text_waste = re.compile(r"\[.*?\]")
    abbaye_data_list_text = [abbaye_data_list_text_waste.sub("", e) for e in abbaye_data_list_text]
    abbaye_data_list_text = [e for e in abbaye_data_list_text if
                             "modifier - modifier le code - modifier Wikidatamodifier - modifier le code - modifier Wikidata" not in e]
    # print(abbaye_data_list_text)

    for e in abbaye_data_list_text:
        all_data_abbaye_list.append(e)
        # print(all_data_abbaye_list)
