# -*- coding: utf-8 -*-
"""
Created on Tue Aug  1 22:32:29 2017

@author: KJH
"""

import requests

from bs4 import BeautifulSoup as bs
from urllib.request import Request, urlopen
from urllib.error import HTTPError
import re

# 로그인할 유저정보를 넣어줍시다. (모두 문자열입니다!)
LOGIN_INFO = {
    'user_id': 'aa',
    'password': 'aa'
}


    
    #html = first_page.text
    #soup = bs(html, 'html.parser')
    #csrf = soup.find('input', {'name':'_csrf'})
    #print(csrf['value'])
    
    #LOGIN_INFO = {**LOGIN_INFO, **{'_csrf' : csrf['value']}}
    #print (LOGIN_INFO)
    
    
try:
    url_request = Request('https://coinmarketcap.com/currencies/neo/#markets', headers = {'User-Agent' : 'Mozilla/5.0'})
    html = urlopen(url_request)
except HTTPError as e:
    print (e)
else:
    source = html.read()
    html.close()
    

    soup = bs(source, "lxml")
    #hot = soup.find("div").find("pop-post-list")
    #hot = soup.find_all("div",{"class" : "bx-viewport"})
    #hot = soup.find_all("div","bx-viewport")
    #hot = soup.find_all("div","pop-post-list")
    #hot = soup.find_all("li")#,"a",{"class" : "title"})
    #print (soup)
    count=1
    #,"a",{"class" : "title"}):
    
    #for lines in soup.find_all("div", id="post-tab2"):

    
    price = soup.find_all('span', 'price')
    print (price)
    
    for lines in price:
        try:
            #print(lines)
            print(lines.text)
        except:
            print("error occured")

    
    
    """
    for lines in soup.select('#rowChart > div.col-md-4.col-sm-12 > div.market-stats > div.wrapper > div.title'):#> div.base-market-subtitle > i > span'):
       # print(count)
        try:
            #print(lines)
            print(lines.text)
        except:
            print("error occured")

        count=count+1
        
   """
    #print(hot)

  #  print(count)
    
   # for link in hot:
   #     print(link.get('href'))
  

    
        
   # body > div > div.contents > div.container.main > div.right > div.board-preview.board-ppomppu > div > a:nth-child(1)
"""
    login_req = s.post('https://www.ppomppu.co.kr/zboard/login_check.php', data=LOGIN_INFO)
    

    print(login_req.status_code)
    # 로그인이 되지 않으면 경고를 띄워줍시다.
    if login_req.status_code != 200:
        raise Exception('로그인이 되지 않았어요! 아이디와 비밀번호를 다시한번 확인해 주세요.')


    # -- 여기서부터는 로그인이 된 세션이 유지됩니다 --
    # 이제 장터의 게시글 하나를 가져와 봅시다. 아래 예제 링크는 중고장터 공지글입니다.
    post_one = s.get('http://www.ppomppu.co.kr/')
    soup = bs(post_one.text, ') # Soup으로 만들어 줍시다.
    print(soup)
    # 아래 CSS Selector는 공지글 제목을 콕 하고 집어줍니다.
    title = soup.select('body > div > div.contents > div.container.main > div.bottom > div.comment-preview.list-container > div.wrap > div > div.bx-viewport > div > ul:nth-child(1) > li:nth-child(1) > a')

    contents = soup.select('#div_content > div.post.box > div.post-content > div.post-article.fr-view')
    # HTML을 제대로 파싱한 뒤에는 .text속성을 이용합니다.
    print(title[0].text) # 글제목의 문자만을 가져와봅시다.
    # [0]을 하는 이유는 select로 하나만 가져와도 title자체는 리스트이기 때문입니다.
    # 즉, 제목 글자는 title이라는 리스트의 0번(첫번째)에 들어가 있습니다.
    print(contents[0].text) # 글내용도 마찬가지겠지요?
"""#