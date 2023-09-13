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
# def author_works():
#     ttbkey = 'ttbmaruck41144001'
#     query_type = 'Author'
#     Query = '파울로 코엘료'
#     max_results = 20
#     start = 1
#     search_target = 'Book'
#     output = 'js'
#     version = 20131101

    # URL = f"http://www.aladin.co.kr/ttb/api/ItemSearch.aspx?ttbkey={ttbkey}&QueryType={query_type}&Query={Query}&MaxResults={max_results}&start={start}&SearchTarget={search_target}&output={output}&Version={version}"

    #request 보내기
    # response = requests.get(URL).json()

    #받은 response를 json 타입으로 바뀌주기
    # response_json = response.json()

    #확인
    # return response['item'][0].get('title')
    # 여기에 코드를 작성합니다.  




# 아래의 코드는 수정하지 않습니다.
if __name__ == '__main__':

    print(author_works())

    