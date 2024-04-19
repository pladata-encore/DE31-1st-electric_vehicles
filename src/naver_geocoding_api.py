# imports
from urllib import parse
import requests
from bs4 import BeautifulSoup as BS
import os
import json
import subprocess
import html5lib

#도로교통공사에서 주소를 도로명주소로 변환한다음, Naver Geocoding API에 넘겨서 좌표를 받아오는 코드
with open("./keys/naver_geocoding_api.json", "r") as f:
    naver_api_keys = json.load(f)

    """generate \"debug.log\" file to results directory; and print message with its time. flags are for message distinguish, which 0 is debug, 1 is error, 2 is status message. by default, flag is 0
    """
def log(msg, flag=None):    
    if flag==None:
        flag = 0
    head = ["debug", "error", "status"]
    from time import gmtime, strftime
    now = strftime("%H:%M:%S", gmtime())
    if not os.path.isfile("./debug.log"):
        assert subprocess.call(f"echo \"[{now}][{head[flag]}] > {msg}\" > debug.log", shell=True)==0, print(f"[error] > shell command failed to execute")
    else: assert subprocess.call(f"echo \"[{now}][{head[flag]}] > {msg}\" >> debug.log", shell=True)==0, print(f"[error] > shell command failed to execute")

def convert_address(address)->str:
    url = "https://www.juso.go.kr/support/AddressMainSearch.do?searchKeyword={}"
    try:
        with requests.Session() as session:
            header = {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.0.0 Safari/537.36"}
            juso_req = session.get(url.format(parse.quote(address)), headers=header)
            assert juso_req.status_code==200, log(f"status code exited with {juso_req.status_code}")
            juso_soup = BS(juso_req.text, "html5lib")
            converted_address = juso_soup.find("div", class_="search_list").find("span", class_="roadNameText").text.strip().replace("\xa0", " ")
        return converted_address
    except Exception as e:
        log(f"Exception occured during address conversion : {e}", 1)
        return None

def get_ngeocoding(address:str):
    try:
        with requests.Session() as nsession:
            nv_gc_api_url_template = "https://naveropenapi.apigw.ntruss.com/map-geocode/v2/geocode?query={}"
            nv_gc_api_headers = {
                "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.0.0 Safari/537.36",
                "X-NCP-APIGW-API-KEY-ID" : naver_api_keys['clientID'],
                "X-NCP-APIGW-API-KEY" : naver_api_keys['clientSecret'],
                "Accept" : "application/json"
            }
            caddress = convert_address(address)
            caddress = caddress if caddress != None else address
            nv_gc_api_url = nv_gc_api_url_template.format(parse.quote(caddress))
            nv_gc_req = nsession.get(nv_gc_api_url, headers=nv_gc_api_headers)
            assert nv_gc_req.status_code==200, log(f"connection error with status code {nv_gc_req.status_code}", 1)
        naver_json = nv_gc_req.json()
        assert naver_json['status']=="OK", log(f"status error", 1)
        return naver_json
    except Exception as e:
        log(f"Exception: {e}")
        return None

def geocoding(address):
    try:
        rjson = get_ngeocoding(address)
        assert rjson!=None, log(f"naver json fetch failed")
        with open("./results/naver_geocoding_result.json", "w", encoding="utf-8") as f:
            json.dump(rjson, f, ensure_ascii=False)
        assert rjson['meta']['totalCount'] > 0, log(f"naver json fetched {rjson['meta']['totalCount']} address")
        lat, lng = rjson['addresses'][0]['x'], rjson['addresses'][0]['y']
        return [lat, lng]
    except Exception as e:
        log(f"Exception occured while geocoding: {e}", 1)
        return [0, 0]