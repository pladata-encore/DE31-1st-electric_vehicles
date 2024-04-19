import pandas as pd
import requests
from tqdm import tqdm
import json
import naver_geocoding_api as nga

with open("./keys/api_key.json", "r") as f:
    key_json = json.load(f)

def get_restarea_info()->pd.DataFrame:
    with requests.Session() as session:
        try:
            restarea_api_url_template = "https://data.ex.co.kr/openapi/locationinfo/locationinfoRest?{}{}{}{}"
            restarea_api_key = f"key={key_json['RESTAREA_API_KEY']}"
            restarea_api_type = f"&type=json"
            restarea_api_rownum = "&numOfRows=10"
            restarea_api_pageNo = "&pageNo={}"
            restarea_url = restarea_api_url_template.format(restarea_api_key, restarea_api_type, restarea_api_rownum,restarea_api_pageNo.format(1))
            
            init_req = session.get(restarea_url)
            restarea_df = pd.DataFrame(init_req.json()['list'])
            
            assert init_req.status_code==200, nga.log(f"requests status code exited with {init_req.status_code}")
            with open("./results/rest_areas.json", "w", encoding='utf-8') as f:
                json.dump(init_req.json(), f, ensure_ascii=False)
            
            page_size = init_req.json()['pageSize']
            
            for pageNo in tqdm(range(2, page_size+1)):
                restarea_url_total = restarea_api_url_template.format(restarea_api_key, restarea_api_type, restarea_api_rownum,restarea_api_pageNo.format(pageNo))
                concat_req = session.get(restarea_url_total)
                
                assert concat_req.status_code==200, nga.log(f"requests status code exited with {concat_req.status_code}")
                with open("./results/rest_areas.json", "w", encoding='utf-8') as f:
                    json.dump(concat_req.json(), f, ensure_ascii=False)
                concat_df = pd.DataFrame(concat_req.json()['list'])
                restarea_df = pd.concat([restarea_df, concat_df])
            return restarea_df
        except Exception as e:
            nga.log(f"Exception: {e}")
            return None