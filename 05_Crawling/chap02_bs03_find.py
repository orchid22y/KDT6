html_example='''
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>BeautifulSoup 활용</title>
</head>
<body>
    <h1 id="heading">Heading 1</h1>
    <p>Paragraph</p>
    <span class="red">BeautifulSoup Library Examples!</span>
    <div id="link">
        <a class="external_link" href="www.google.com">google</a>

        <div id="class1">
            <p id="first">class1's first paragraph</p>
            <a class="exteranl_link" href="www.naver.com">naver</a>

            <p id="second">class1's second paragraph</p>
            <a class="internal_link" href="/pages/page1.html">Page1</a>
            <p id="third">class1's third paragraph</p>
        </div>
    </div>
    <div id="text_id2">
        Example page
        <p>g</p>
    </div>
    <h1 id="footer">Footer</h1>
</body>
</html>
'''

from bs4 import BeautifulSoup

soup= BeautifulSoup(html_example,'html.parser')
print(soup.find('div'))


print(soup.find('div',{'id':'text_id2'}))

div_text=soup.find('div',{'id':'text_id2'})
print(div_text)

#	'\n	Example	page\n	<p>g</p>\n'
print(div_text.string)	#	None 리턴


href_link=soup.find('a',{'class':'internal_link'}) # 딕셔너리 형태
href_link=soup.find('a',class_='internal_link') # class_사용: class는 파이썬 예약어

print(href_link)                # <a clss="internal_link",...>
print(href_link['href'])        # <a>태그 내부 href 속성의 값 (url)을 추출
print(href_link.get('href'))    # ['href']와 동일 기능
print(href_link.text)           #<a> page1 </a>태그 내부의 텍스트 (Page1) 추출

href_value = soup.find(attrs={'href' : 'www.google.com'})
href_value = soup.find('a', attrs={'href':'www.google.com'})


# find() 함수 활용
#   • href 속성의 값이 'www.google.com'인 항목 검색
#   • 속성: attrs={'속성이름':'속성값'}
print('href_vlue:', href_value)
print(href_value['href'])
print(href_value.string)

#§ find()	함수
#   • span 태그의 속성 가져오기
span_tag=soup.find('span')
print('span tag:', span_tag)
print('attrs:', span_tag.attrs)
print('value:', span_tag.attrs['class'])
print('text:', span_tag.text)  


# find() 함수 활용
#   • class 속성
#       – class 속성은 여러 개의 값을 가질 수 있음 (multi-valued	attribute)
#       – 따라서 list	형태로 리턴함

print('class 속성값:', href_link['class'])



