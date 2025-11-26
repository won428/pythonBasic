myencoding = 'utf-8'
source = open(file= 'jumsu.txt', mode= 'rt', encoding= myencoding)
destination = open(file= 'result.txt', mode= 'wt', encoding= myencoding)

data = [item.strip() for item in source.readlines()]
print(data)

for bean in data:
    human = bean.split(',')
    name = human[0]
    kor = float(human[1])
    eng = float(human[2])
    math = float(human[3])
    _gender = human[4].upper()

    total = kor + eng + math
    avg = total / 3.0

    gender  = '남자' if _gender == 'M' or _gender == 'm' else '여자'

    # 표시 형식 '이름/성별/총점/평균'
    sentences = f'{name}/{gender}/{total:.1f}/{avg:.2f}\n'
    print(sentences)
    print(sentences, file= destination)


source.close()
destination.close()


