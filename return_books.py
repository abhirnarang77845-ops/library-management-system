from storage_data import books
from datetime import date
from calculate_fine import calculate_fine
def return_books():
    
    print("             RETURN A BOOK")
    
 
    name = input("  Enter Book Name  :  ").strip()
 
    if name not in books:
        print("\n  !! Book not found in library !!")
 
    elif books[name]["available"]:
        print("\n  !! This book was not issued !!")
 
    else:
        today        = date.today()
        issue_date   = books[name]["issue_date"]
        days_allowed = books[name]["days_allowed"]
        
        days_used    = (today - issue_date).days
        days_late    = days_used - days_allowed
 
        print(f"""
  
            BOOK RETURN DETAILS
  
   Book         :  {name}
   Issued to    :  {books[name]['issued_to']}
   Issue Date   :  {issue_date}
   
   Return Date  :  {today}
   Days Used    :  {days_used} days""")
 
        if days_late > 0:
            fine = calculate_fine(days_late)
            print("""!! FINE APPLIED  :  Rs. {fine} !!
   Please pay the fine at the counter.""")
  
   
        else:
           print("BOOK RETURNED AT TIME")
  

 
        books[name]["available"]    = True
        books[name]["issued_to"]    = None
        books[name]["issue_date"]   = None
        books[name]["days_allowed"] = None
 
        print(f"\n  ✔  Book '{name}' returned successfully!")