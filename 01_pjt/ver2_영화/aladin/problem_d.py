import json


def best_book(books):
    n = []
    k = []
    for book in books:
        book_id = book["id"]
        new_book = open(f"data/books/{book_id}.json" , encoding="utf-8")
        new_book = json.load(new_book)
        n.append(new_book["customerReviewRank"])
        k.append(new_book["title"])
    max_n = n[0]
    max_i = 1
    for i in range(1, len(n)):
        if max_n < n[i]:
            max_n = n[i]
            max_i = i+1
    return k[max_i-1]



    # d = []
    # for i in range(len(books)):
    #     for j in [books[i]["id"]]:
    #         c = f"data/books/{j}.json"
    #         a = open(c, encoding='utf-8')
    #         b = json.load(a)
    #         d.append(b)
    #         for q, w in d[i]

    


    # return books



        
        
# 아래의 코드는 수정하지 않습니다.
if __name__ == '__main__':
    books_json = open('data/books.json', encoding='utf-8')
    books_list = json.load(books_json)

    print(best_book(books_list))




