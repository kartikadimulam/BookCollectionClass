from BookCollectionNode import BookCollectionNode
from Book import Book

class BookCollection:

    def __init__(self):
        self.head = None

    def isEmpty(self):
        return self.head == []

    def getNumberOfBooks(self):
        
        count = 0
        current = self.head
        
        while current != None:
            count = count +1
            current = current.getNext()

        return count
        

    def insertBook(self, book):

        current = self.head
        previous = None
        stop = False
        
        while current != None and not stop:

            if current.getData() > book:
                stop = True

            else:
                previous = current
                current = current.getNext()

        temp = BookCollectionNode(book)

        if previous == None:
            self.head = temp
            temp.setNext(current)

        else:
            previous.setNext(temp)
            temp.setNext(current)

    def getBooksByAuthor(self, author):

        current = self.head
        s = ''
        
        while current != None:

            if current.getData().author.upper() == author.upper():
                s = s+ current.getData().getBookDetails() + '\n'
                
            current = current.getNext()
            

        return s

    def getAllBooksInCollection(self):

        current = self.head
        s = ''

        while current != None:
            s += current.getData().getBookDetails()+'\n'
            current = current.getNext()

        return s


    def removeAuthor(self, author):

        current = self.head
        previous = None
        
        while current != None:
            if current.getData().author.upper()==author.upper():
                if previous == None:
                    self.head = current.getNext()
                else:
                    previous.setNext(current.getNext())
                current = current.getNext()
            else:
                previous = current
                current = current.getNext()

    def recursiveSearchTitle(self, title, bookNode):

        if bookNode is None:
            return False
        
        previous = None

        if bookNode.getData().title.upper() == title.upper():
            return True
        else:
            previous = bookNode
            return self.recursiveSearchTitle(title, bookNode.getNext())
                
        
b0 = Book("Cujo", "King, Stephen", 1981)
b1 = Book("The Shining", "King, Stephen", 1977)
b2 = Book("Ready Player One", "Cline, Ernest", 2011)
b3 = Book("Rage", "King, Stephen", 1977)

bc = BookCollection()
bc.insertBook(b0)
bc.insertBook(b1)
bc.insertBook(b2)
bc.insertBook(b3)



        
