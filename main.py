from add_books import add_books
from show_books import show_books
from issue_books import issue_books
from return_books import return_books

while True:
    
  print("MINI LIBRARY")
  print("ENTER YOUR CHOICE")
  print(""" 1.  Add Book
   2.  Show All Books
   3.  Issue Book
   4.  Return Book
   5.  Exit""")

 
  choice = input("  Enter your choice (1-5)  :  ").strip()
 
  if   choice == "1":
        add_books()
  elif choice == "2":
        show_books()
  elif choice == "3":
        issue_books()
  elif choice == "4":
        return_books()
  elif choice == "5":
     print(f"\n  Thank you for using Mini Library! Goodbye!\n")
     break
else:
    print("\n  !! Invalid choice! Please enter between 1 to 5 !!")