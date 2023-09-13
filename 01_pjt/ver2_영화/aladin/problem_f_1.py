import json


def best_new_books(books):
    n = []
    k = []
    x = []
    for book in books:
        book_id = book["id"]
        new_book = open(f"data/books/{book_id}.json" , encoding="utf-8")
        new_book = json.load(new_book)
        n.append(new_book["pubDate"])
        k.append(new_book["title"])
        x.append(new_book["customerReviewRank"])

    p = 0
    c = []
    d = []

    for i in n:
   
        if i[:4] == '2023':
            c.append(k[p])
            d.append(x[p]) 
        p += 1
    max_n = d[0]
    max_i = 1
    for i in range(1, len(d)):
        if max_n < d[i]:
            max_n = d[i]
            max_i = i+1
    return c[max_i-1]





# 아래의 코드는 수정하지 않습니다.
if __name__ == '__main__':
    books_json = open('data/books.json', encoding='utf-8')
    books_list = json.load(books_json)
    
    print(best_new_books(books_list))
