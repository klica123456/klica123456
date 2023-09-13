import json
from pprint import pprint


def books_info(books, categories):
    book_list = []
    for p in range(len(books)):
        new_data = {}
        new_data = {
            'id' : books[p].get('id'),
            'name' : books[p].get('title'),
            'author' : books[p].get('author'),
            'priceSales' : books[p].get('priceSales'),
            'description' : books[p].get('description'),
            'cover' : books[p].get('cover'),
            'categoryId' : books[p].get('categoryId')
        }

        x = []
        for j in range(len(categories)):
            for i in [categories[j]['id']]:
                for f in range(len(books[p]['categoryId'])):
                    for k in [books[p]['categoryId'][f]]:
                        if i == k:
                            x.append(categories[j]['name'])
                            new_data['categoryName'] = x
        book_list.append(new_data)
    return book_list






                        

        



# 아래의 코드는 수정하지 않습니다.
if __name__ == '__main__':
    books_json = open('data/books.json', encoding='utf-8')
    books = json.load(books_json)

    categories_json = open('data/categories.json', encoding='utf-8')
    categories_list = json.load(categories_json)

    pprint(books_info(books, categories_list))