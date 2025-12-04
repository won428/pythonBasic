import requests
import json
import xml.etree.ElementTree as ET
import pandas as pd

API_KEY =  "52496643416373773130394d6e7a4444"


def fetch_seoul_library_data():
    BASE_URL = f'http://openapi.seoul.go.kr:8088/{API_KEY}/xml/SebcTourStreetKor/'

    start_index = 1
    batch_size = 1000
    locationList = []


    while True:
        end_index = start_index + batch_size - 1
        print(f'시작 인덱스 : {start_index}, 끝 인덱스 : {end_index}')

        url = BASE_URL + str(start_index) + '/' + str(end_index) + '/'
        print(url)
        response = requests.get(url) # 응답 받은 객체
        print(response.text[:1000])
        if response.status_code != 200: # 성공 못하면
            print(f'데이터 패치 못함, 응답 상태 코드 : {response.status_code}')
            break
        #end if

        try:
            root = ET.fromstring(response.text)
            result_code = root.find('RESULT/CODE')
            if result_code is not None and result_code.text != 'INFO-000' :
                print('API Error : ', root.find('RESULT/MESSAGE'.text))
                break
            #end inner if

            rows = root.findall('row')
            if not rows:
                break # 더 이상 데이터가 없음
            # end if

            # findtext() 함수의 2번째 매개변수는 오류가 발생하지 않도록 기본값을 넣어줍니다.
            for location in rows:
                subdata = [
                    location.findtext('MAIN_KEY','N/A'),
                    location.findtext('NM_DP','N/A'),
                    location.findtext('KOR_ALIAS','N/A'),
                    location.findtext('NAME_KOR','N/A'),
                    location.findtext('LAW_SIDO','N/A'),
                    location.findtext('LAW_SGG','N/A'),
                    location.findtext('H_KOR_CITY','N/A'),
                    location.findtext('H_KOR_GU','N/A'),
                    location.findtext('H_KOR_DONG','N/A'),
                    location.findtext('WGS84_X','N/A'),
                    location.findtext('WGS84_Y','N/A')
                ]
                locationList.append(subdata)
            # end for

            start_index += batch_size  # 다음 1000개 조회

        except ET.ParseError as err:
            print(f'XML 파싱 오류 : {err}')
            break
        #end try

        # break # 무한루프 종료

    #end while

    print(f'데이터 갯수 : {len(locationList)}')
    print(f'자료 유형 : {type(locationList)}')

    return locationList
#end def

# file_name이라는 이름으로 리스트 datalist를 csv 파일 형식으로 저장해줌
def save_to_csv(datalist, file_name):
    book_columns = ['키','검색키워드','alias','최종표기명','지번주소','법정시','법정구','행정구','행정동','중심 좌표 X','중심 좌표 Y']
    book_frame = pd.DataFrame(datalist, columns=book_columns)
    book_frame.to_csv(file_name, index=False, encoding='utf-8-sig')
    print(f'파일 저장 : {file_name}')
# end def save_to_csv

data = fetch_seoul_library_data()
print(data[0:3])

dataOut = './../dataOut/'
filename = dataOut + 'test.csv'
save_to_csv(data, filename)