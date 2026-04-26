from storage_data import books
from show_books import show_books
from datetime import date

def issue_books():
    show_books()
 

    print("             ISSUE A BOOK")
    
 
    name = input("  Enter Book Name       :  ").strip()
 
    if name not in books:
        print("\n  !! Book not found in library !!")
 
    elif not books[name]["available"]:
        print(f"\n  !! Sorry! This book is already issued to --> {books[name]['issued_to']} !!")
 
    else:
        student      = input("  Enter Your Name       :  ").strip()
        days_allowed = int(input("  Issue for how many days :  "))
 
        issue_date   = date.today()

 
        books[name]["available"]    = False
        books[name]["issued_to"]    = student
        books[name]["issue_date"]   = issue_date
        books[name]["days_allowed"] = days_allowed
 
        print(f"""

           BOOK ISSUED SUCCESSFULLY!
  
   Book        :  {name}
   Student     :  {student}
   Issued on   :  {issue_date}

  
   FINE CHART (if returned late) :
     Week 1  -->  Rs. 10  per day
     Week 2  -->  Rs. 20  per day
     Week 3  -->  Rs. 60  per day
     (fine increases every week!)

   Please return the book on time!""")