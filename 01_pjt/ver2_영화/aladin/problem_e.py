import json


def new_books(books):
    n = []
    k = []
    for book in books:
        book_id = book["id"]
        new_book = open(f"data/books/{book_id}.json" , encoding="utf-8")
        new_book = json.load(new_book)
        n.append(new_book["pubDate"])
        k.append(new_book["title"])
    p = 0
    c = []

    for i in n:
   
        if i[:4] == '2023':
            c.append(k[p])
        p += 1

    return c


    #     for i in new_book:

    
    # print(new_book)
    #     print(i)
    #     new_books.append(i["pubDate"])
    #     if i["pubDate"][:4] == '2023':
    #         new_books.append(i["title"])
    # return new_books
    # 여기에 코드를 작성합니다.  





# 아래의 코드는 수정하지 않습니다.
if __name__ == '__main__':
    books_json = open('data/books.json', encoding='utf-8')
    books_list = json.load(books_json)
    
    print(new_books(books_list))
