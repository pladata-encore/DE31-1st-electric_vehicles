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

# custom python lib
import src.evchargestations as EV
import src.naver_geocoding_api as NGA

metro_codes = EV.metro_codes

with open("./keys/db_info.json", "r") as f:
    db_info = json.load(f)
    
def connect_to_db():
    user = db_info['user']
    password = db_info['password']
    host = db_info['host']
    port = db_info['port']
    database = db_info['database']
    password = parse.quote_plus(password)
    engine = sqlalchemy.create_engine(f"mysql://{user}:{password}@{host}:{port}/{database}?charset=utf8mb4")

