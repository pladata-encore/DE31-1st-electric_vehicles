# DE-1st-Electronic Vehicle Charge Station Data Analysis
## Summary

이 토이프로젝트는 [Playdata](https://playdata.io)에서 진행하는 데이터 엔지니어링 프로젝트 31기 부트 캠프에서 진행하는 프로젝트입니다.

프로젝트에 참여하는 인원들은 다음과 같습니다.
- [최성현](https://github.com/S0rrow)
- [유정연](https://github.com/yjyj989812)
- [김승주](https://github.com/tmdwnabc)
- [이충원](https://github.com/cw3714)
- [신소영](https://github.com/soyoungshin1)

해당 프로젝트의 목적은 대한민국에서 전기차를 운용하기 위한 충전소의 수량이 충분히 보급되었는가를 확인하는 것입니다.

---

## Development Condition
해당 프로젝트의 개발 환경은 다음과 같습니다.

1. Python 3.10: 데이터를 시각화하고 실행 코드를 작성하기 위해 Python3를 사용했습니다.   
    - Python Modules: Python의 다양한 외부 패키지의 활용과 개발 환경 보존을 위해 pip와 venv를 사용했습니다.
    - 해당 프로젝트에 사용된 주요 패키지는 다음과 같습니다.
        - Pandas: 대량의 데이터를 처리하기 위해 사용했습니다.
        - requests: 웹과 API를 통해 데이터를 가져오기 위해 사용했습니다.
        - BeautifulSoup: 웹을 통해 가져온 데이터를 파싱하기 위해 사용했습니다.
2. Github: 프로젝트의 개발 과정과 코드를 보존하기 위해 Git과 Github를 사용했습니다.
3. MySQL: 프로젝트의 데이터를 저장하고 다시 끌어오기 위해 MySQL을 사용했습니다.

---

### For Reproduction
본 프로젝트의 개발 환경은 WSL Ubuntu 22.04.4 LTS를 기반으로 구성되었습니다.

모든 명령어는 본 레포지토리의 복제된 로컬 레포지토리에서 실행된다는 가정하에 설명되었습니다.

프로젝트의 환경을 복제해 재현하기 위해서는 [PRESET.md](./PRESET.md) 파일을 참조해 주세요.

24.04.19에 진행된 프로젝트 진행 결과 발표에 대해서는 [Presentation.md](./presentation/Presentation.md) 파일을 참조해 주세요.

---

## API Used
본 프로젝트에 사용된 데이터는 OpenAPI 및 오픈되어 있는 사이트들에서 제공하는 데이터를 사용해 구성되었습니다.

사용된 API 및 사이트들의 목록은 다음과 같습니다.

| Index | API | Details |
|:---|:---|:---|
| 1 | [네이버 Geocoding API](https://api.ncloud-docs.com/docs/ai-naver-mapsgeocoding) | 주소를 좌표값으로 변환하기 위해 사용했습니다.|
| 2 | [행정안전부 도로명주소 사이트](https://www.juso.go.kr/openIndexPage.do) | 지번주소를 도로명주소로 변환하기 위해 사용했습니다. |
| 3 | [전력데이터 개방 포털시스템](https://tinyurl.com/27ej5rbl) | 전기차 충전소 현황에 대한 데이터를 받아오기 위해 사용했습니다. |
| 4 | [ChargeInfo 전기차 등록 현황](https://tinyurl.com/2yeqnkb9) | 전국의 연도별 전기차 등록 현황 및 전기차 충전소 현황에 대한 데이터를 받아오기 위해 사용했습니다. |
| 5 | [네이버 차량 정보 검색 결과](https://search.naver.com/search.naver?where=nexearch&sm=top_hty&fbm=0&ie=utf8&query=%EC%9E%90%EB%8F%99%EC%B0%A8) | 차량 정보를 가져오기 위해 사용했습니다. |
| 6 | [환경빅데이터 플랫폼 전기자동차 월 전력수요량 예측 데이터](https://tinyurl.com/228cgdun) | 전국 시도별 전기자동차 전력수요량을 예측한 데이터를 가져오기 위해 사용했습니다. |
| 7 | [국토교통 통계누리 전국 자동차등록현황보고](https://tinyurl.com/23ha88m4) | 연도별로 전국에 등록된 모든 종류(전기차, 하이브리드, 내연차량)의 차량 정보를 가져오기 위해 사용했습니다. |
