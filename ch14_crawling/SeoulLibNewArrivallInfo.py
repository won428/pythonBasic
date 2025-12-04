# 서울 열린 데이터 광장
# https://data.seoul.go.kr/
# 검색 키워드 : 서울도서관
# 목표 : 서울도서관 새로 들어온 도서정보
# https://data.seoul.go.kr/dataList/OA-15484/S/1/datasetView.do
import requests
import json
import xml.etree.ElementTree as ET
import pandas as pd


API_KEY = "52496643416373773130394d6e7a4444" # 발급받은 API 인증키

def fetch_seoul_library_data():
    BASE_URL = f"http://openapi.seoul.go.kr:8088/{API_KEY}/xml/SeoulLibNewArrivalInfo/" # 1/5/

    start_index = 1 # 최초 시작 인덱스 번호
    batch_size = 1000 # 배치 사이즈
    new_books = [] # 신간 도서 목록


    while True:
        end_index = start_index + batch_size - 1
        print(f'시작 인덱스 : {start_index}, 끝 인덱스 : {end_index}')

        url = BASE_URL + str(start_index) + '/' + str(end_index) + '/'
        print(url)
        response = requests.get(url) # 응답 받은 객체

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
            for onebook in rows:
                subdata = [
                    onebook.findtext('TITLE','N/A'),
                    onebook.findtext('AUTHOR','N/A'),
                    onebook.findtext('PUBLISHER','N/A'),
                    onebook.findtext('PUBLISHER_YEAR','N/A'),
                    onebook.findtext('TYPE','N/A'),
                    onebook.findtext('LOCA','N/A'),
                    onebook.findtext('INDT','N/A')
                ]
                new_books.append(subdata)
            # end for

            start_index += batch_size  # 다음 1000개 조회

        except ET.ParseError as err:
            print(f'XML 파싱 오류 : {err}')
            break
        #end try

        # break # 무한루프 종료

    #end while

    print(f'데이터 갯수 : {len(new_books)}')
    print(f'자료 유형 : {type(new_books)}')

    return new_books
#end def

# file_name이라는 이름으로 리스트 datalist를 csv 파일 형식으로 저장해줌
def save_to_csv(datalist, file_name):
    book_columns = ['도서명','저자','발행처','발행년도','자료유형','소장처','등록일']
    book_frame = pd.DataFrame(datalist, columns=book_columns)
    book_frame.to_csv(file_name, index=False, encoding='UTF-8')
    print(f'파일 저장 : {file_name}')
# end def save_to_csv

data = fetch_seoul_library_data()
print(data[0:3])

dataOut = './../dataOut/'
filename = dataOut + 'seoul_library_newbooks.csv'
save_to_csv(data, filename)