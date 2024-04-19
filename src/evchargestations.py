# import
import pandas as pd
import numpy as np
import selenium
import sqlalchemy
from urllib import parse
import requests
from bs4 import BeautifulSoup as BS
import os
import json
from tqdm import tqdm
import pickle
from geopy.geocoders import Nominatim
import subprocess

# custom lib
import src.naver_geocoding_api as NGA

with open("./keys/api_key.json", "r") as f:
    key_json = json.load(f)

def extract_as_csv():
    result_file_name_template = "ev_cs_{}.json"
    API_KEY = key_json['API_KEY']
    result_path = "./results"
    if not os.path.isdir(result_path):
        os.mkdir(result_path)
    for key in metro_codes.keys():
        assert ev_cs_get_by_metro_code(f"{result_path}/"+result_file_name_template.format(key), API_KEY, metro_code=metro_codes[key]), NGA.log(f"{key} extraction failed")
        NGA.log(f"{key} extraction success")

metro_codes =  {
    "서울특별시" : "11",
    "부산광역시" : "21",
    "대구광역시" : "22",
    "인천광역시" : "23",
    "광주광역시" : "24",
    "대전광역시" : "25",
    "울산광역시" : "26",
    "경기도" : "31",
    "강원도" : "32",
    "충청북도" : "33",
    "충청남도" : "34",
    "전라북도" : "35",
    "전라남도" : "36",
    "경상북도" : "37",
    "경상남도" : "38",
    "제주특별자치도" : "39"
}

headers = {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.0.0 Safari/537.36"}

def ev_cs_get_by_metro_code(result_file_name:str, API_KEY:str, metro_code:str, city_code=None)->bool:
    ev_api_url = "https://bigdata.kepco.co.kr/openapi/v1/EVcharge.do?{}{}apiKey={}&returnType=json"
    metroCd = f"metroCd={metro_code}&"
    cityCd = "" if city_code==None else f"cityCd={city_code}&"
    try:
        req = requests.get(ev_api_url.format(metroCd, cityCd, API_KEY), headers=headers)
        soup = BS(req.text)
        data = json.loads(soup.text)
        result_path = "./results"
        if not os.path.isdir(result_path):
            os.mkdir(result_path)
        with open(f"{result_file_name}", "w", encoding="utf-8") as f:
            json.dump(data, f, ensure_ascii=False)
            
    except Exception as e:
        NGA.log(f"exception : {e}")
        return False
    return True
    
result_file_name_template = "ev_cs_{}.json"

API_KEY = key_json['API_KEY']

def extract_charge_stations()->pd.DataFrame:
    result_path = "../results"
    if not os.path.isdir(result_path):
        os.mkdir(result_path)
    for key in metro_codes.keys():
        assert ev_cs_get_by_metro_code(f"{result_path}/"+result_file_name_template.format(key), API_KEY, metro_code=metro_codes[key]), NGA.log(f"{key} extraction failed")
        NGA.log(f"{key} extraction success")

    listdata = []
    for key in tqdm(metro_codes.keys()):
        filename = result_file_name_template.format(key)
        with open(f"{result_path}/{filename}", "r") as f:
            file = json.load(f)
        for info in file["data"]:
            listdata.append(info)
            
    data = pd.DataFrame(listdata)
    with open("./results/EV_CS_DATA.pkl", "wb") as f:
        pickle.dump(data, f)
    return data