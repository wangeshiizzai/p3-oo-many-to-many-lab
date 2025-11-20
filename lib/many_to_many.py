class Author:
    all = []

    def __init__(self, name):
        if not isinstance(name, str):
            raise Exception("Author name must be a string")
        self.name = name
        type(self).all.append(self)

    # Return all contracts related to this author
    def contracts(self):
        return [contract for contract in Contract.all if contract.author == self]

    # Return all books related to this author via contracts
    def books(self):
        return [contract.book for contract in self.contracts()]

    # Sign a new contract for a book
    def sign_contract(self, book, date, royalties):
        if not isinstance(book, Book):
            raise Exception("book must be an instance of Book")
        if not isinstance(date, str):
            raise Exception("date must be a string")
        if not isinstance(royalties, int):
            raise Exception("royalties must be an integer")
        return Contract(self, book, date, royalties)

    # Total royalties across all contracts
    def total_royalties(self):
        return sum(contract.royalties for contract in self.contracts())


class Book:
    all = []

    def __init__(self, title):
        if not isinstance(title, str):
            raise Exception("Book title must be a string")
        self.title = title
        type(self).all.append(self)

    def contracts(self):
        # Return all contracts associated with this book
        return [contract for contract in Contract.all if contract.book == self]

    def authors(self):
        # Return a list of unique authors for this book
        return list({contract.author for contract in self.contracts()})

class Contract:
    all = []

    def __init__(self, author, book, date, royalties):
        if not isinstance(author, Author):
            raise Exception("author must be an instance of Author")
        if not isinstance(book, Book):
            raise Exception("book must be an instance of Book")
        if not isinstance(date, str):
            raise Exception("date must be a string")
        if not isinstance(royalties, int):
            raise Exception("royalties must be an integer")
        self.author = author
        self.book = book
        self.date = date
        self.royalties = royalties
        type(self).all.append(self)

    # Class method to get contracts by date
    @classmethod
    def contracts_by_date(cls, date):
        return [contract for contract in cls.all if contract.date == date]
