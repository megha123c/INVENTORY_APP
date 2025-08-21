from db.db_connection import DBConnection
from lib.ProductManagementlib import ProductManagementLib
def main():
    while True:
         print("\n===========PRODUCT MANAGEMENT MENU===========")
         print("1. ADD PRODUCT")
         print("2.DISPLAY ALL PRODUCT ")
         print("3. UPDATE PRODUCT")
         print("4. SEARCH PRODUCT BY ID")
         print("5. DISABLE PRODUCT")
         print("6. APPLY GST ")
         print("7. EXIT")
         choice = input("Enter your choice:")
         if choice == "1":
            ProductManagementLib.add_product()
         elif choice == "2":
            ProductManagementLib.display_all()
         elif choice == "3":
            ProductManagementLib.update_product()
         elif choice == "5":
            ProductManagementLib.disable_product()
         elif choice == "6":
            ProductManagementLib.apply_gst_to_percent()
         elif choice == "7":
             break
         else: 
             print("Invalid choice, try again!!")

        
    
if __name__ == "__main__":
    main()