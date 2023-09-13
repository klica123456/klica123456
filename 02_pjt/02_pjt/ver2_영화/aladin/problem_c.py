import requests
from pprint import pprint


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

     # 여기에 코드를 작성합니다.  




# 아래의 코드는 수정하지 않습니다.
if __name__ == '__main__':

    pprint(bestseller_book())

