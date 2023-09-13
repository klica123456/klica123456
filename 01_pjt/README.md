# 01_pjt1_영화_aladin

## 1번 문제
    a = {}
    def book_info(book):
        new_data = {
            'id' : book.get('id'),
            'name' : book.get('title'),
            'author' : book.get('author'),
            'priceSales' : book.get('priceSales'),
            'description' : book.get('description'),
            'cover' : book.get('cover'),
            'categoryId' : book.get('categoryId')

        }
        return new_data

- 코드는 book파일을 읽어서 각 dict에 대한 id, title, author, priceSales, description, cover, categoryId를 읽어서 새로운 dict를 만드는 코드이다.
    - 1번은 쉬웠다.


## 2번 문제
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
- 2번은 1번에서 만든 dict에 대해 categoryId를 읽어 categories에 있는 ID와 비교해서 있으면 dict에 ID에 해당하는 NAME을 넣는 코드이다. 
    - 구현 과정에서 어려웠던 점: 두개의 dict.value에 대한 비교가 어려웠다. 하지만 이번 문제를 통해 완벽히 익혔다.

## 3번 문제
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

- 2번에서 한것을 많은 책들에 대해 한 코드이다.
    - 아주 쉬웠다.


## 4번 문제
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

- 처음 books data의 파싱을 통해 data를 읽어오고 data와 관련된 파일을 읽어서 평점을 추출하고 가장 높은 평점을 가진 책이름을 출력시키는 코드이다.
    - 구현과정에서 가장 큰 평점을 갖는게 몇번째에 있는지 확인하는 코드를 짜는 것이 힘들었다. 또한, list는 index가 0번째 부터 시작하므로 출력할때 -1해줘야 되는 detail까지 배울 수 있었다.

- 내가 어렵게 구현한 코드
        
        d = []
        for i in range(len(books)):
            for j in [books[i]["id"]]:
                c = f"data/books/{j}.json"
                a = open(c, encoding='utf-8')
                b = json.load(a)
                d.append(b)

- 마지막으로 짠 코드와 똑같이 동작하지만 훨씬 어렵게 짠것을 확인할 수 있다. 역시 알고리즘 공부와 많은 시간을 투자해서 시행착오를 겪어야 성장할 수 있는 것 같다.

## 5번 문제
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

- 처음 books data의 파싱을 통해 data를 읽어오고 data와 관련된 파일을 읽어서 출판 날짜를 출력하고 연도가 2023인 책의 제목을 출력하는 코드이다.
    - 4번을 풀어서 쉬웠다.

## 느낀점
- 알고리즘 공부, 수많은 시행착오 등 많은 시간을 투자해야 코딩실력을 향상시킬 수 있다는 것을 깨달았다. 열심히 하자




