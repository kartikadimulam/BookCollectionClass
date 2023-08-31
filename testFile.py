
from BookCollection import BookCollection
from Book import Book
from BookCollectionNode import BookCollectionNode


b0 = Book("Cujo", "King, Stephen", 1981)
b1 = Book("The Shining", "King, Stephen", 1977)
b2 = Book("Ready Player One", "Cline, Ernest", 2011)
b3 = Book("Rage", "King, Stephen", 1977)

bc = BookCollection()
bc.insertBook(b0)
bc.insertBook(b1)
bc.insertBook(b2)
bc.insertBook(b3)


def test_isEmpty():
    assert bc.isEmpty() == False

def test_getNumberOfBooks():
    assert bc.getNumberOfBooks() == 4

def test_getBooksByAuthor():
    assert bc.getBooksByAuthor("KING, Stephen") == 'Title: Rage, Author: King, Stephen, Year: 1977\nTitle: The Shining, Author: King, Stephen, Year: 1977\nTitle: Cujo, Author: King, Stephen, Year: 1981\n'

def test_getAllBooksInCollection():
    assert bc.getAllBooksInCollection() == 'Title: Ready Player One, Author: Cline, Ernest, Year: 2011\nTitle: Rage, Author: King, Stephen, Year: 1977\nTitle: The Shining, Author: King, Stephen, Year: 1977\nTitle: Cujo, Author: King, Stephen, Year: 1981\n'

def test_removeAuthor():
    bc.removeAuthor("KING, Stephen")
    assert bc.getAllBooksInCollection() == 'Title: Ready Player One, Author: Cline, Ernest, Year: 2011\n'
    
def test_insertBook():
    b5 = Book("AI Superpowers", "Lee, Kaifu", 2020)
    bc.insertBook(b5)
    assert bc.getBooksByAuthor("LEE, Kaifu") == 'Title: AI Superpowers, Author: Lee, Kaifu, Year: 2020\n'

def test_gettitle():
    assert bc.head.getData().getTitle() == 'Ready Player One'

def test_getAuthor():
    assert b0.getAuthor()=='King, Stephen'

def test_getYear():
    assert b2.getYear()==2011

def test_getBookDetails():
    assert b2.getBookDetails() == 'Title: Ready Player One, Author: Cline, Ernest, Year: 2011'

def test_gt():
    assert (b1 > b2) == True


def test_getData():
    assert bc.head.getData().title == 'Ready Player One'

def test_getNext():
    assert bc.head.getNext().getData().title == 'AI Superpowers'

def test_setdata():
    bc.head.setData(b3)
    assert bc.head.getData().title == 'Rage'
    
def test_setnext():
    bc.head.setNext(b0)
    assert bc.head.getNext().title == 'Cujo'



