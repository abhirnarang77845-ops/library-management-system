from storage_data import books
def add_books():
    
 print( "ADD A NEW BOOK")
    
 
 name = input("  Enter Book Name  :  ").strip()
 
 if name in books:
        print(f"\n  !! '{name}' already exists in the library !!")
 else:
        books[name] = {
            "available"   : True,
            "issued_to"   : None,
            "issue_date"  : None,
            "days_allowed": None
        }
        print(f"\n    Book '{name}' added successfully!")