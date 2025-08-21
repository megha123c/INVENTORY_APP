from dao.ProductDaoImple import ProductDaoImplementation
from dao.AbstractProdutDao import ProductDaoService
from datetime import datetime
from models.product import Product

class ProductManagementLib:
    'handles CRUD logic'

    dao_service:ProductDaoService = ProductDaoImplementation()

    @staticmethod
    def display_all():
        products = ProductManagementLib.dao_service.display_all_products()
        for product in products:
            print(product)

    @staticmethod
    def add_product():
        product = Product()
        productname = input("Enter the product name:")
        product.set_product_name(productname)
        unitprice = float(input("Enter the unit price:"))
        product.set_unitprice(unitprice)
        categoryid = int(input("Enter the category id:"))
        product.set_categoryid(categoryid)
        m_date = input("Enter manufacture Date(dd/MM/yyyy):")
        util_date = datetime.strptime(m_date,"%d/%m/%Y")
        conv_m_date = util_date.date()
        product.set_manufacture_date(conv_m_date)
        product.set_is_active(is_active="Y")

        if ProductManagementLib.dao_service.insert_products(product):
            print("inserted successfully....") 
        else:
            print("Something went wrong.......")      

    @staticmethod
    def update_product():
        searchid = int(input("Enter the product ID:"))
        #create a method in DAO
        product = ProductManagementLib.dao_service.find_by_product_id(searchid)
        if not product:
            print("Product not found")
            return
        print(product)
        confirm = input("Do you want to edit this data?(y/n)")
        if confirm.lower()=='y':
            product.set_product_name(input("Enter new product name:"))
            product.set_unitprice(float(input("Enter new unit price:")))
            #pass the object to dao update
            if ProductManagementLib.dao_service.update_product(product,searchid):
               print("Updated successfully........")
            else:
                print("Something went wrong....")

    @staticmethod
    def disable_product():
        searchid = int(input("Enter the product ID:"))
        product = ProductManagementLib.dao_service.find_by_product_id(searchid)
        if not product:
            print("Product not found")
            return
        print(product)
        confirm = input("Do you want to disable this data?(y/n)")
        if confirm.lower()=='y':
            if ProductManagementLib.dao_service.disable_product(product,searchid):
               print("Disabled successfully........")
            else:
                print("Something went wrong....")
   
    @staticmethod
    def apply_gst_to_percent():
        product_id = int(input("Enter the product ID to apply GST:"))
        gst_percent = float(input("enter GST percentage to apply:"))
        if ProductManagementLib.dao_service.apply_gst(product_id,gst_percent):
            print(f"GST of {gst_percent} applied to product ID {product_id}")
        else:
            print("failed to apply GST")





