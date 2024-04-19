# import
import pandas as pd
import sqlalchemy
from urllib import parse
from bs4 import BeautifulSoup as BS
import json
import folium

# custom python lib
import src.evchargestations as EV
import src.naver_geocoding_api as NGA

engine = sqlalchemy.Engine

query_template = "select * from {}"

with open('./data/skorea_metros_geo.json', 'r', encoding='utf-8') as f:
    geo_json = json.load(f)
    # geo json에 시도 목록 이름 변경
    for feat in geo_json['features']:
        sido_name = feat['properties']['CTP_KOR_NM']
        if sido_name.find('전라북도') > -1:
            feat['properties']['CTP_KOR_NM'] = '전북특별자치도'
        elif sido_name.find('강원도') > -1:
            feat['properties']['CTP_KOR_NM'] = '강원특별자치도'

    
with open("./keys/db_info.json", "r") as f:
    db_info = json.load(f)
    
def connect_to_db():
    global engine
    user = db_info['user']
    password = db_info['password']
    host = db_info['host']
    port = db_info['port']
    database = db_info['database']
    password = parse.quote_plus(password)
    engine = sqlalchemy.create_engine(f"mysql://{user}:{password}@{host}:{port}/{database}?charset=utf8mb4")

def coord(row):
    rlat = row['lat']
    rlng = row['lag']
    return [rlat, rlng]

def generate_gas_station_map():
    gs_info = pd.read_sql(query_template.format("gasStationInfo"), con=engine)
    gs_info_count = pd.DataFrame(gs_info.sido.value_counts()).reset_index().copy()

    gs_info['coordinates'] = gs_info.apply(coord ,axis=1)

    gs_map = folium.Map(location=[36.9127, 127.9958], zoom_start=7.5, tiles="cartodb positron")

    folium.Choropleth(
        geo_data = geo_json,
        data=gs_info_count,
        columns=['sido', 'count'],
        fill_color="YlOrBr",
        key_on= 'feature.properties.CTP_KOR_NM',
        legend_name="시도별 주유소 개수"
    ).add_to(gs_map)

    for idx, row in gs_info.iterrows():
        folium.CircleMarker(
            location=row.coordinates,
            radius=1,
            color='#800000',
            fill_opacity=0.5,
        ).add_to(gs_map)
        
    gs_map.save("./results/gs_map.html")
    
def generate_electricvehicle_chargestation_map():
    cs_info = pd.read_sql(query_template.format("chargeStationInfo"), con=engine)
    cs_info_count = pd.DataFrame(cs_info.sido.value_counts()).reset_index().copy()

    cs_info['coordinates'] = cs_info.apply(coord ,axis=1)

    ev_cs_map = folium.Map(location=[36.9127, 127.9958], zoom_start=7.5, tiles="cartodb positron")
        
    folium.Choropleth(
        geo_data = geo_json,
        data=cs_info_count,
        columns=['sido', 'count'],
        fill_color="YlGnBu",
        key_on= 'feature.properties.CTP_KOR_NM',
        legend_name="시도별 전기차 충전소 개수"
    ).add_to(ev_cs_map)

    for idx, row in cs_info.iterrows():
        folium.CircleMarker(
            location=row.coordinates,
            radius=1,
            color='#003366',
            fill_opacity=0.5,
        ).add_to(ev_cs_map)
        
    ev_cs_map.save("./results/ev_cs_map.html")
