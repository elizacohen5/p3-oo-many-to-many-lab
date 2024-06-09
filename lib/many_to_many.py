class Author:

    all = []

    def __init__(self, name):
        self.name = name
        Author.all.append(self)
    
    def __repr__(self):
        return f"Author: {self.name}"
    
    def contracts(self):
        contract_list = []
        for contract in Contract.all:
            if contract.author is self:
                contract_list.append(contract)
        return contract_list
    
    def books(self):
        related_books = []
        for contract in Contract.all:
            if contract.author is self:
                related_books.append(contract.book)
        return related_books
    
    def sign_contract(self, book, date, royalties):
        new_contract = Contract(self, book, date, royalties)
        return new_contract
    
    def total_royalties(self):
        total_royalties = 0
        for contract in Contract.all:
            if contract.author is self:
                total_royalties += contract.royalties
        return total_royalties




class Book:

    all = []

    def __init__(self, title):
        self.title = title
        Book.all.append(self)

    def contracts(self):
        book_contracts = []
        for contract in Contract.all:
            if contract.book is self:
                book_contracts.append(contract)
        return book_contracts
    
    def authors(self):
        book_authors = []
        for contract in Contract.all:
            if contract.book is self:
                book_authors.append(contract.author)
        return book_authors
    
    def __repr__(self):
        return f"Book: {self.title}"


class Contract:

    all = []

    def __init__(self, author, book, date, royalties):
        self.author = author
        self.book = book
        self.date = date
        self.royalties = royalties
        Contract.all.append(self)
    
    @classmethod
    def contracts_by_date(cls, date):
        contract_match = []
        for contract in cls.all:
            if contract.date == date:
                contract_match.append(contract)
        return contract_match
    
    @property
    def author(self):
        return self._author
    
    @author.setter
    def author(self, author):
        if not isinstance(author, Author):
            raise Exception
        self._author = author
    
    @property
    def book(self):
        return self._book

    @book.setter 
    def book(self, book):
        if not isinstance(book, Book):
            raise Exception
        self._book = book
    
    @property
    def date(self):
        return self._date
    
    @date.setter
    def date(self, date):
        if not isinstance(date, str):
            raise Exception
        self._date = date
    
    @property
    def royalties(self):
        return self._royalties 
    
    @royalties.setter
    def royalties(self, royalty):
        if not isinstance(royalty, int):
            raise Exception
        self._royalties = royalty
        

    def __repr__(self):
        return f"Contract -> {self.author} {self.book} {self.date} {self.royalties}"

author = Author("stephen king")
book = Book("the shining")
contract = Contract(author, book, "May 12,1977", 1234432)
author.sign_contract(book, "June 9, 2024", 100000)
print(book.contracts())