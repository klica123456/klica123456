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



# 아래의 코드는 수정하지 않습니다.
if __name__ == '__main__':

    pprint(author_other_works('베니스의 상인'))

    pprint(author_other_works('개미'))

    pprint(author_other_works('*'))
