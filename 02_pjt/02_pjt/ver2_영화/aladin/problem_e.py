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







# 아래의 코드는 수정하지 않습니다.
if __name__ == '__main__':

    pprint(ebook_list('베니스의 상인'))

    pprint(ebook_list('*'))
