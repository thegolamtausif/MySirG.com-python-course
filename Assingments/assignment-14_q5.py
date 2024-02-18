class book:
    def __init__(self):
        self.bookid=int(input("Enter the book ID - "))
        self.titel=(input("Enter the name of the book - "))
        self.price=int(input("Enter the price - "))
        self.author=(input("Who is the author of the book - "))
        self.publisher=(input("Who is the published of this book - "))
    def show_book_details(self):
        print("Name of the book is  - ",self.titel)
        print("Book id  is - ",self.bookid,end="     ")
        print("Price  - ",self.price)
        print("Author  - ",self.author,end="     ")
        print("Publisher  - ",self.publisher)
    def chgprc(self):
        print("book id - ",self.bookid)
        self.price=int(input("Enter the updated  price -" ))
        print("Updated.")

python=book()
python.show_book_details()
python.chgprc()