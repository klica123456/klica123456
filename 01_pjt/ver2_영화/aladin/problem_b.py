import json
from pprint import pprint


def book_info(book, categories):
    new_data = {
        'id' : book.get('id'),
        'name' : book.get('title'),
        'author' : book.get('author'),
        'priceSales' : book.get('priceSales'),
        'description' : book.get('description'),
        'cover' : book.get('cover')
    }

    x = []

    for j in range(len(categories)):
        for i in [categories[j]['id']]:
            for f in range(len(book['categoryId'])):
                for k in [book['categoryId'][f]]:

                    if i == k:

                        x.append(categories[j]['name'])
                        new_data['categoryName'] = x

    return new_data

    # 여기에 코드를 작성합니다.  

        


# 아래의 코드는 수정하지 않습니다.
if __name__ == '__main__':
    book_json = open('data/book.json', encoding='utf-8')
    book = json.load(book_json)

    categories_json = open('data/categories.json', encoding='utf-8')
    categories_list = json.load(categories_json)

    pprint(book_info(book, categories_list))
