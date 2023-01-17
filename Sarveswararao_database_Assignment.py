import mysql.connector
class ProductManagementTool:
    print("-----Product Management Tool-----")
    options= "Choose the below any one option.\n1.Add Product\n2.Update Product.\n3.Delete Product.\n4.Get Product By Id.\n5.Get All Products.\n"
    option=int(input(options))
    productTable=['productId','productName','productPrice']
    def __init__(self):
         self.mydb=mysql.connector.connect(host="localhost",user="root",passwd="rps@123",database="kpmg")
         self.cursor = self.mydb.cursor()
        # cursor.execute("SELECT * FROM information_schema.tables WHERE table_name = 'productInfo'")
        # print(type(cursor.fetchone()))
        # pr="productinfo"
        # tr = cursor.fetchone()
       
        # if  len(tr)>0:
        #     cursor.close()
        # else:
            # 
        
    def insertProductInfo(self,productTable):
         self.cursor.execute(f"insert into productInfo values({productTable[0]},'{productTable[1]}' ,{productTable[2]})")
         self.mydb.commit()
         self.mydb.close()
         print("Product Added Successfully..")

    def updateProduct(self,productTable):
         self.cursor.execute(f"update productInfo set productPrice={productTable[1]} where productId={productTable[0]}")
         self.mydb.commit()
         self.mydb.close()
         print("Product Updated Successfully..")
    def deleteProduct(self,productTable):
         self.cursor.execute(f"delete from productInfo where productId={productTable[0]}")
         self.mydb.commit()
         self.mydb.close()
         print("Product Deleted Successfully..")
    def getProduct(self,productTable):
         self.cursor.execute(f"select * from productInfo where productId={productTable[0]}")
         print( self.cursor.fetchone())
         self.mydb.close()
    def getAllProduct(self):
          self.cursor.execute(f"select * from productInfo")
          print(self.cursor.fetchall())
          self.mydb.close()
    
product=ProductManagementTool()
if product.option == 1:
    prodcutDetailsMap = []
    prodcutDetailsMap.append(int(input("Enter Prodcut Id: ")))
    prodcutDetailsMap.append(input("Enter Prodcut Name: "))
    prodcutDetailsMap.append(int(input("Enter product Price: ")))
    product.insertProductInfo(prodcutDetailsMap)
if product.option == 2:
    prodcutDetailsMap = []
    prodcutDetailsMap.append(int(input("Enter Prodcut Id: ")))
    prodcutDetailsMap.append(int(input("Enter product Price: ")))
    product.updateProduct(prodcutDetailsMap)
if product.option == 3:
    prodcutDetailsMap = []
    prodcutDetailsMap.append(int(input("Enter Prodcut Id: ")))
    product.deleteProduct(prodcutDetailsMap)
if product.option == 4:
    prodcutDetailsMap = []
    prodcutDetailsMap.append(int(input("Enter Prodcut Id: ")))
    product.getProduct(prodcutDetailsMap)
if product.option == 5:
    product.getAllProduct()
