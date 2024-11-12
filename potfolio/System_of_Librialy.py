class book:
    book_id = 0
    def __init__(self, name, author, year):
        self.id = book.book_id
        self.name = name
        self.author = author
        self.year = year
        self.aviable = True
        book.book_id+=1

class Librialy:
    def __init__(self):
        self.books = {}

    def add_book(self, book):
        self.books[book.book_id] = book
        print(f'Книга "{book.name}" добавлена в библиотеку')

    def del_book(self, book_id):
        if book_id in self.books:
            del self.books[book_id]
            print(f'Книга с ID: {book_id} была удалена из библиотеки')
        else:
            print(f'Книга с ID: {book_id} не была найдена')

    def search_books(self, **kwargs):
        result = []
        for book in self.books.values():
            coun = True
            for key, value in kwargs.items():
                if getattr(book, key) != value:
                    coun = False
                    break
            if coun:
                result.append(book)
        if result:
            return result
        return 'По вашему запросу ничего не найдено'

    def lend_book(self, book_id):
        if book_id in self.books:
            book = self.books[book_id]
            if book.aviable:
                book.aviable = False
                print(f'Книга "{book.name}" выдана')
            else:
                print(f'Книга "{book.name}" уже выдана')
        else:
            print(f'Книга с ID: {book_id} не найдена')

    def return_book(self, book_id):
        if book_id in self.books:
            book = self.books[book_id]
            if not book.aviable:
                book.aviable = True
                print(f'Книга "{book.name}" была возвращена')
            else:
                print(f'Книга "{book.name}" уже возвращена')
        else:
            print(f'Книга с ID: {book_id} не найдена')

    def list_aviable_books(self):


