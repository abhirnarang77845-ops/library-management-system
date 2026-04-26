from storage_data import books

def show_books():
    
    print("              ALL BOOKS")
    
 
    if len(books) == 0:
        print("      NO BOOKS AVAILABLE IN LIBRARY !!")
    else:
        for book in books:
            if books[book]["available"]:
                print(f"  {book}    Available")
           


              