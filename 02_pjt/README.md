# 02_pjt_영화_aladin

## 1번문제

    import requests


    def author_works():
        URL = 'http://www.aladin.co.kr/ttb/api/ItemSearch.aspx'

        params = {
            'ttbkey': 'ttbmaruck41144001',
            'QueryType': 'Author',
            'Query' : '파울로 코엘료',
            'MaxResults' : 20,
            'start' : 1,
            'SearchTarget' : 'Book',
            'output' : 'js',
            'Version' : '20131101'
        }

        response = requests.get(URL, params=params).json()
        k = []
        for i in response['item']:
            k.append(i['title'])

        return k

    if __name__ == '__main__':

    print(author_works())

- 코드는 알라딘 홈페이지에서 openapi를 사용해서 queryType고 query를 사용해서 요청한 데이터를 가져오는 것
- 어려웠던 점 : 처음 open api를 접하며 어떻게 데이터를 가져오는지 방법을 몰랐고,  
open api를 사용하는 방법도 사이트마다 어떻게 활용하는지 자세하게 나와있지만 적용 방법을 몰라서 어려웠다.
- 알게 된 점: open api사용법을 조금 알게된거 같고, 앞으로 open api를 사용함에 있어 조금 익숙하게 할 수 있을 것 같다.

## 2번문제
    import requests
    from pprint import pprint


    def best_review_books():
        URL = 'http://www.aladin.co.kr/ttb/api/ItemSearch.aspx'

        params = {
            'ttbkey': 'ttbmaruck41144001',
            'QueryType': 'Author',
            'Query' : '파울로 코엘료',
            'MaxResults' : 20,
            'start' : 1,
            'SearchTarget' : 'Book',
            'output' : 'js',
            'Version' : '20131101'
        }

        response = requests.get(URL, params=params).json()
        k = []
        for i in response['item']:
            if i['customerReviewRank'] >= 9:
                k.append(i)

        return k



    # 아래의 코드는 수정하지 않습니다.
    if __name__ == '__main__':

        pprint(best_review_books())

- 다음 코드는 1번에서 출력한것을 평점 9점이상인 데이터를 뽑는것이다.
- 1번을 한 이상 매우 쉬웠다. ㅎㅎ

## 3번코드

    def bestseller_book():
        URL = 'http://www.aladin.co.kr/ttb/api/ItemSearch.aspx'

        params = {
            'ttbkey': 'ttbmaruck41144001',
            'QueryType': 'Author',
            'Query' : '파울로 코엘료',
            'MaxResults' : 20,
            'start' : 1,
            'SearchTarget' : 'Book',
            'output' : 'js',
            'Version' : '20131101'
            }


        response = requests.get(URL, params=params).json()
        k = {}
        for i in response['item']:
            k[i['salesPoint']] = i['title']


        t = []
        a = 0
        for i in sorted(k, reverse=True):
            if a < 5:
                t.append(k[i])
            else:
                break   
            a += 1

        # sorted_k = sorted(k.items(), key = lambda item: item[0], reverse = True)

        return t



- 다음코드는 처음 뽑은 데이터들을 salespoint를 키로 title을 value로 dict를 만든다음 salespoint의 상위5개 데이터를 뽑은 것이다.
- 어려웠던 점: 상위 5개 데이터를 뽑는 과정에서 어떻게 구현할 지 생각을 많이 했다. 과거의 나였다면 list로 먼저 salespoint를 뽑고 title도 뽑아 for문과 if문을 통해 구현했을 것이다. 하지만, dict로 salespoint를 key값으로 만들고 dict를 내림차순으로 정렬한 후, title을 뽑았다. 이 과정이 조금 어려웠지만, 해내고 나니 뿌듯했다. 
- 알게 된 점: 확실히 dict를 잘 쓰면 데이터를 처리하는데 훨씬 유리하다.

## 4번

    import requests
    from pprint import pprint


    def author_other_works(title):
        URL = 'http://www.aladin.co.kr/ttb/api/ItemSearch.aspx'

        params = {
            'ttbkey': 'ttbmaruck41144001',
            'QueryType': 'Title',
            'Query' : title,
            'MaxResults' : 20,
            'start' : 1,
            'SearchTarget' : 'Book',
            'output' : 'js',
            'Version' : '20131101'
            }


        response = requests.get(URL, params=params).json()

        if response['item'] == []:
            return None
        # pprint(response['item'])
        a = response['item'][0]['author'] 
        b = a.index('(')
        c = a[0:b-1]
        params1 = {
            'ttbkey': 'ttbmaruck41144001',
            'QueryType': 'Author',
            'Query' : c,
            'MaxResults' : 20,
            'start' : 1,
            'SearchTarget' : 'Book',
            'output' : 'js',
            'Version' : '20131101'
        }

        response1 = requests.get(URL, params=params1).json()
        t = []
        count = 0
        for i in response1['item']:
            k = ''
            k = i['author']
            d = k.index('(')
            l = k[0:d-1]
            if l == c and count < 5:
                t.append(i['title'])
                count += 1
            elif count == 5:
                break   

        return t


- 다음 코드는 베니스의 상인이 제목에 있는 책들을 검색한 다음 가장 위에 있는 책의 지은이를 뽑아 그 사람이 쓴 책 5개의 제목을 뽑는 코드이다.
- 어려웠던 점: 지은이를 뽑을때 문자열에서 뽑고 싶은 내용을 슬라이스 하는 부분이 어려웠다. 이 과정에서 index를 통해 '('있을 때까지의 문자열을 slice하고 지은이를 뽑아 이 지은이에 해당되는 책을 뽑을 수 있었다. 
- 느낀 점 : 만약 기회가 된다면 더 쉬운 방법을 찾아봐야겠다.

## 5번

    import requests
    from pprint import pprint


    def ebook_list(title):
    URL = 'http://www.aladin.co.kr/ttb/api/ItemSearch.aspx'

    params = {
        'ttbkey': 'ttbmaruck41144001',
        'QueryType': 'Title',
        'Query' : title,
        'MaxResults' : 20,
        'start' : 1,
        'SearchTarget' : 'Book',
        'output' : 'js',
        'Version' : '20131101'
        }


    response = requests.get(URL, params=params).json()

    if response['item'] == []:
        return None
    
    a = response['item'][0]['title']
    b = response['item'][0]['priceSales']
    

    params1 = {
        'ttbkey': 'ttbmaruck41144001',
        'QueryType': 'Title',
        'Query' : a,
        'MaxResults' : 20,
        'start' : 1,
        'SearchTarget' : 'eBook',
        'output' : 'js',
        'Version' : '20131101'
        }
    
    response1 = requests.get(URL, params=params1).json()
    p = []
    for i in response1['item']:
        if b >= i['priceSales']:
            k = {}
            k['isbn'] = i['isbn']
            k['itemId'] = i['itemId']
            k['link'] = i['link']
            k['priceSales'] = i['priceSales']
        p.append(k)
    return p

- 다음 코드는 매개변수의 제목을 가지는 책들을 뽑고 같은 제목을 가진 ebook을 뽑은 다음 book에서 뽑은 책 가격의 90%보다 싼 가격의 ebook들의 정보를 뽑는 코드이다.
- 4번을 경험하고 나니 아주 쉬웠다. ㅎㅎ

- 느낀점 : open api를 가져와서 이를 활용해 데이터를 정렬하고 분석하는 방법을 배울 수 있어서 재밌었다. 데이터 분석능력을 높이고 싶은데 한단계 성장한것 같아서 기분이 좋다. 그리고 파이썬이 빅데이터처리에 특화되어 있다고 하는데 기회가 된다면 다른언어로 데이터를 처리해보며 차이점을 느껴봐야겠다.


