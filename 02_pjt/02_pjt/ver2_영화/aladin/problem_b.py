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
