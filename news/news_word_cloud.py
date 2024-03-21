from konlpy.tag import Okt # 한글 자연어 처리 라이브러리 / Okt : 트위터에서 개발한 형태소 분석기
from collections import Counter # 텍스트 데이터에서 각 단어의 빈도수 계산
from wordcloud import WordCloud # 텍스트 데이터에서 단어의 빈도수를 기반으로 워드클라우드를 생성
import matplotlib.pyplot as plt # 워드클라우드를 시각화하기 위해 사용되는 라이브러리
import pandas as pd # CSV 파일 등의 형태로 저장된 텍스트 데이터를 불러오고 다루기 위해 사용

# csv파일 읽어오기(원하는 크롤링 결과 읽어오기)
newsList = pd.read_csv("news_data.csv", delimiter='|', encoding="utf-8-sig")
 
okt = Okt()
word_list = []

# 각 행의 'title' 열을 개별적으로 처리
for title in newsList['title']:
    # 형태소 분석 작업을 진행
    for word, tag in okt.pos(title):
        # 명사와 형용사만 추출
        if tag in ['Noun', 'Adjective']:
            # 조건을 만족하는 단어들만 word_list 데이터셋에 추가
            word_list.append(word)
            
            
# 각 행의 'content' 열을 개별적으로 처리
for content in newsList['content']:
    # 형태소 분석 작업을 진행
    for word, tag in okt.pos(str(content)):
        # 명사와 형용사만 추출
        if tag in ['Noun', 'Adjective']:
            # 조건을 만족하는 단어들만 word_list 데이터셋에 추가
            word_list.append(word)

# 동일 단어 횟수 추출
word_list_count = Counter(word_list)
total_word_count = sum(word_list_count.values())
print(word_list_count)
print(total_word_count)


# 워드클라우드 객체 선언 및 출력
wc =  WordCloud(font_path = 'malgun', width=400, height=400)
result = wc.generate_from_frequencies(word_list_count)
plt.axis('off') # 그래프 축 제거
plt.imshow(result)
plt.show()
wc.to_file("result.png") # png 파일로 저장