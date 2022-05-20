# python-shopping-cart
Shopping cart program in python, my first OOP project. Command line interface project to explore the use of OOP. The challenge was to use as much OOP principles as possible and certain data structures, and to overload some operators.

## USER MANUAL
Welcome to the shopping cart system. To access it you need to run the python code. You will be 
presented with a menu with 6 options:
1. Create a customer
2. List Products
3. Add or Remove a product from the cart
4. See current shopping cart
5. Checkout
6. Quit Program
To access the options, you must input a number between 1 and 6. Option 1 must be done first 
before you move onto any of the rest of the options. If you try to move on, you will be unable to do 
so.

1. Create a customer
This requires you to fill in your details such as your name, CustomerID, address and phone number. 
If you would like to sign up to our loyalty scheme you may do so for only €10 a year. This enables 
you to access many offers for our shop.
2. List Products
If you signed up as a loyal customer, three different selections of products will be offered to you: 
exclusive, bargain and all. Select what type of product you would like to view (1-3)
If you are a bargain hunter customer, only the bargain products will be displayed to you when you 
select this option, priced low to high.
3. Add or remove product from the cart
Add – you will be prompted for a productID and a quantity to add. If you select an erroneous 
productID it will not add.
Remove – you will be prompted for a productID and a quantity to remove. If you select an erroneous 
productID it will not remove. If your cart is empty you will not be allowed into this option. If you 
select a quantity greater than what you have it will delete the product from your cart.
4. See current cart
This will show you the customer details, products in the cart, along with qtys, and the subtotal at the 
bottom.
5. Checkout
The checkout function will take the customer through a few options depending on what type of 
customer they are.
6. Exit
This will exit the program.

## CLASSES
class Customer(object):

This is the SuperClass of Loyal_Customers(customer) and Bargain_Hunters(customer). It takes in the 
following attributes: name = str, customerId=int, address=str and phone=str. Address and phone are 
private.

Methods

Methods of this class are __str__, which prints the customer details and get/set for phone, card 
number and address.

def view_bargain_bin(bargain_bin):

This method views the bargain_bin. It is available to all customers, so is a method of the Customer 
class. It is very simply done by appending the products in the bargain_bin to a list and printing this as 
a string. The > operator was overloaded in the product class and the .sort function is used to sort the 
products from low price to high.

class Loyal_Customers(Customer):
This is a sub-class of the Customer class. This class takes in all the attributes of the Customer 
SuperClass.
Methods of this class are __str__, which prints the customer details. It overwrites the 
__str__method of the Customer class.
def view_exclusive_product_dict(exclusive_dict):
This is a method to sort the exclusive products by ID. First the products are added to a list. It does 
this by using the .sort function, where key=lambda x: getattr(x, “productId”). This accesses the 
attribute “productID” and sorts the list with this attribute. Lambda is an anonymous function that 
can take any number of arguments. Getattr can access any attribute of an object.
https://www.w3schools.com/python/python_lambda.asp
https://www.programiz.com/python-programming/methods/built-in/getattr
def view_product_dict(product_dict):
This method is completed in the same manner as above.

class Bargain_Hunters(Customer):
This is a sub-class of the Customer class. This class takes in all the attributes of the Customer 
SuperClass.
Methods of this class are __str__, which prints the customer details. It overwrites the 
__str__method of the Customer class.

class Shopping_Cart(object):
This class is for the shopping cart. It uses composition to take in attributes from the Customer Class 
(name, customerId). It has additional attributes shopping_cart and subtotal. The default value of 
subtotal = 0, as an empty cart has a subtotal of 0.
shopping_cart is a dictionary. It is in the format {productID : quantity}
subtotal is updated in a method when there are contents in the cart.
Methods of this class:
def __str__(self):
This method prints the entire shopping cart. It does this by going between the keys of the 
shopping_cart dictionary and the product_dictionary. The relevant details of the cart are printed in 
this method. They are the Customer name, ID, productID, productName, quantity of product, and 
the Subtotal. All the details are appended to a list and then converted to a string. They are appended 
to a list using the + operator which is overloaded to concatenate strings and the product details in 
the Product Class.
def add_to_cart(self):
This method adds products to the shopping_cart. The user is prompted for a productID and quantity 
to add to cart. It does this by accessing both the product_dictionary and self.shopping_cart. It 
accesses the information via the keys. If a product key does not match (KeyError) or there is a 
ValueError, nothing is added to the dictionary and the user is prompted again. If the keys match and 
the product is not in the dictionary, the quantity is set as the value. If the key is already in the 
dictionary, then the quantity is added to the value. This is in the format {productID : quantity}
def add_to_cart_bargain(self):
This method is nearly exactly the same as above, only it uses the bargain_bin to check if a product 
exists. This method is for the bargain customers.
def remove_from_cart(self):
This method removes products from the shopping cart. The user is prompted for a productID and 
quantity to remove from the cart. It does this by accessing both the product_dictionary and 
self.shopping_cart. It accesses the information via the keys. If a product key does not match 
(KeyError) or there is a ValueError, nothing removed from the dictionary and the user is prompted 
again. If the amount of products to remove is greater than or equal to what is in the dictionary, the 
product is deleted. Otherwise the quantity is reduced by the desired amount. 
def get_subtotal(self):
This method calculates the subtotal of the Shopping Cart. It does this by accessing the information 
via the keys of the product_dictionary and the shopping_cart. When the keys match, the values are 
multiplied and the result is appended to a list. The * operator was overloaded in the Product class to 
multiply Product.price to any integer. The sum(list) function is then used to add up all the values and 
self.subtotal is updated and returned. 

class Product(object):
This is the class for the Product objects. It is made up of the attributes name=str, productId=int, 
price=int and exclusive=bool. Exclusive is expressed as a Boolean.
Methods of this class:
def __str__(self):
This method prints the product details.
def __lt__(self, other):
This method overloads the operator < for sorting the products in the bargain_bin dictionary. It sorts 
by the self.price attribute.
def __mul__(self, other):
This method overloads the operator * for calculating the subtotal in the get_subtotal method. It 
multiplies self.price to any integer.
def __add__(self, other):
This method overloads the operator + for concatenating the string in the view_cart (__str__) method 
of the shopping cart. It accesses self.productId, self.name and self.price.

## FUNCTIONS
def create_product_dict():
This function creates the product dictionary from a file. It does this by reading the file, stripping “\n” 
and appending each line to a list. Each attribute of the list_element is then inserted into the product 
dictionary using indices to access the elements. This is done in the format
product_dict[ProductID] = Name, ProductID, Price, Exclusive/Non Exclusive.
The types are applied to the elements as they are added.
ProductID = int
Name = str
Price = int
Exclusive/Non Exclusive is expressed as a Boolean. This is done using the eval() function. I found this 
function here: https://realpython.com/python-eval-function/
The main warning with this function is to not use it with untrusted input, which is not the case here 
as I created the product_file and could ensure it would be only evaluating “True” or “False”.

def create_bargain_bin(product_dict):
This function creates the bargain_bin using the product_dictionary. It accesses the values using a for 
loop and if value.exclusive == False, then it is added to the bargain_bin.
def create_exclusive_product_dict(product_dict):
This function creates the exclusive_product_dict using the product_dictionary. It accesses the values 
using a for loop and if value.exclusive == True, then it is added to the exclusive_product_dict.
def main_menu():
used a global statement at the top for new_customer, shopping_cart and current_cart as all these 
parameters were being used a lot in the menu if/else statements. 
def create_customer():, def payment():
Both these functions used recursion to force the customer to enter their details correctly.
Below are the rest of the functions used, none of them use any methods not described above. They 
are all functions to create dictionaries, customers or menu functions.
def list_products_submenu(new_customer):
def add_or_remove_submenu(new_customer, current_cart):
def checkout():
