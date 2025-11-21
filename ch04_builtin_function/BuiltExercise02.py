# 다음 human 데이터를 이용하여 출력 결과와 같이 출력되도록 합니다.
human = ['김철수', '홍길동', '박영희', '심수련', '유재민']
# enumerate() 함수를 사용하여, 인덱스 값이 짝수인 회원들만 따로 추출하여 mylist를 만들어 보세요.
myList = [enum for (idx, enum) in enumerate(human) if idx%2 == 0  ]
print(myList)

# listComprehension 기능을 사용하여, 다음과 같은 데이터를 만들어 보세요.
#newhuman = ['김철수님', '박영희님', '유재민님']

newHuman = [f'{new}님' for new in myList]
print(newHuman)