DB명: encore4
Table 개수 : 10개

- Table1: `areaInfo` : 전국 국토 총조사 데이터
>   `year` char(4) NOT NULL : 연도
>   `sido` varchar(10) NOT NULL : 시도
>   `sigungu` varchar(10) NOT NULL : 시군구
>   `area` bigint NOT NULL DEFAULT '0' : 해당 행정구역의 면적
>   `land_address_count` int NOT NULL : 해당 행정구역에 등록된 지번수



- Table2: `carModel`  : 전기차 모델별 주행거리 데이터
>   `car_model` varchar(50) NOT NULL : 전기차 모델명
>   `range_per_charge_km` int NOT NULL : 해당 모델 1회 완충 기준 주행거리



- Table3: `carRegitrectionCount` : 전국 자동차 등록 현황 데이터
>   `year` char(4) NOT NULL : 연도
>   `month` char(2) NOT NULL : 월
>   `sido` varchar(10) NOT NULL : 시도
>   `sigungu` varchar(10) NOT NULL : 시군구
>   `count` int NOT NULL : 해당 연도월별 행정구역 내 전기차 등록대수



- Table4: `chargeStationCount` : 전국 전기차 충전소 갯수 데이터
>   `year` char(4) NOT NULL : 연도
>   `sido` varchar(10) NOT NULL : 시도
>   `charge_type` char(2) NOT NULL : 충전 형태완속, 급속)
>   `count` int NOT NULL : 해당 연도의 시도 행정구역 내 전기자동차 개수



- Table5: `chargeStationInfo` : 전국 전기차 충전소 지리 데이터
>   `sido` varchar(10) NOT NULL : 시도
>   `sigungu` varchar(10) NOT NULL : 시군구
>   `station_name` varchar(30) NOT NULL : 전기차 충전소명
>   `address` varchar(50) NOT NULL : 전기차 충전소 주소
>   `rapid_charge_count` int NOT NULL : 급속 충전기 개수
>   `slow_charge_count` int NOT NULL : 완속 충전기 개수
>   `car_type` text : 사용가능한 차량모델
>   `lng` float NOT NULL : 경도
>   `lat` float NOT NULL : 위도



- Table6: `electricCarRegitrectionCount`  : 전국 전기차 등록 수 데이터
>   `year` char(4) NOT NULL : 연도
>   `sido` varchar(10) NOT NULL : 시도
>   `count` int NOT NULL : 해당 년도의 시도 내 전기차 등록 대수



- Table7: `electricDemand` : 전국 전기차 전력 수요량 예측 데이터
>   `year` char(4) NOT NULL : 연도
>   `month` char(2) NOT NULL : 월
>   `sido` varchar(10) NOT NULL : 시도
>   `sigungu` varchar(10) NOT NULL : 시군구
>   `demended_amount_kW` int NOT NULL : 연도월별 해당 행정구역내 전기차 전력 수요량



- Table8: `gasStationInfo` : 전국 주유소 주유소 지리 데이터
>   `sido` varchar(10) NOT NULL : 시도
>   `sigungu` varchar(10) NOT NULL : 시군구
>   `station_name` varchar(30) NOT NULL : 주유소 이름
>   `address` varchar(50) NOT NULL : 주유소 주소
>   `company` varchar(20) NOT NULL : 주유소 계열사
>   `phone_number` varchar(20) NOT NULL : 주유소 전화번호
>   `lag` float NOT NULL : 경도
>   `lat` float NOT NULL : 위도



- Table9: `highwayRestStation` : 전국 고속도로 휴게소 지리 데이터
>   `rest_station_name` varchar(30) NOT NULL : 고속도로 휴게소 이름
>   `route_name` varchar(10) DEFAULT NULL : 해당 휴게소의 도로명
>   `lng` float DEFAULT NULL : 위도
>   `lat` float DEFAULT NULL : 경도




- Table10: `popInfo` : 전국 총인구조사 데이터
>   `sido` varchar(10) NOT NULL : 시도
>   `sigungu` varchar(10) NOT NULL : 시군구
>   `address` varchar(50) NOT NULL : 시도 시군구
>   `total_pop` int NOT NULL : 해당 행정구역의 총인구수
>   `total_family` int NOT NULL : 해당 행정구역의 총세대수
>   `pop_per_family` float NOT NULL : 해당 행정구역의 세대수 당 가족구성원 수
