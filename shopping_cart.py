# ------------------------------------------------ CLASSES ------------------------------------------------------------
class Customer(object):
    """
    This is the Customer Superclass. It is the base class for the sub-classes Loyal Customers and Bargain Hunters.
    """
    # CLASS OBJECT ATTRIBUTES
    def __init__(self, name: str, customerid: int, address=0, phone=0, card_number=0, cvv=0):
        self.name = name
        self.customerid = customerid
        self.__address = address
        self.__phone = phone
        self.__card_number = card_number
        self.__cvv = cvv

    # METHODS
    def __str__(self):
        """This method prints the Customer Object"""
        return "-" * 20 + "\nCustomer Name: {} \nCustomer ID: {}" \
            .format(self.name, self.customerid) + "\n" + "-" * 20

    def set_card_number(self, param):
        """This method is to set the card number details"""
        self.__card_number = param
        return self.__card_number

    def set_cvv(self, param):
        """This method is to set the cvv"""
        self.__cvv = param
        return self.__cvv

    def get_card_number(self):
        """This method is to get the card number"""
        return self.__card_number

    def get_cvv(self):
        """This method is to get the cvv"""
        return self.__cvv

    def set_phone_number(self, new_param):
        """This method is to set the phone number"""
        self.__phone = new_param
        return self.__phone

    def get_phone_number(self):
        """This method is to get the phone number"""
        return self.__phone

    def set_address(self, new_param):
        """This method is to set the address"""
        self.__address = new_param
        return self.__address

    def get_address(self):
        """This method is to get the address"""
        return self.__address

    def view_bargain_bin(self):
        """
        This is a method to view the bargain products by price low to high.
        1. It adds the dictionary values to a list
        2. then uses the .sort method and overloading of the operator > in the product class to organise the
        products by price from low to high
        3. This list is then converted to a string for printing
        """
        product_list = []
        product_list_string = ""
        for key, value in bargain_bin.items():
            product_list.append(value)
            product_list.sort()
            product_list_string = '\n'.join([str(elem) for elem in product_list])
        return print(product_list_string)


class LoyalCustomers(Customer):
    """
    This is the Loyal Customers Class. It is a sub-class of Customer.
    """
    # CLASS OBJECT ATTRIBUTES
    def __init__(self, name, customerid):
        super().__init__(name, customerid)

    # METHODS
    def __str__(self):
        """This method prints the Loyal Customer Object"""
        return "-" * 20 + "\n" \
                          "Customer Name: {}\nCustomer ID: {}\nCustomer Type: Loyal Customer" \
                          "".format(self.name, self.customerid) + "\n" + "-" * 20

    def view_exclusive_prods(self):
        """
        This is a method to view exclusive products by ID low to high
        1. It adds the dictionary values to a list
        2. then uses the .sort method and lambda, getattr to sort by "productId"
        3. This list is then converted to a string for printing
        """
        product_list = []
        product_list_string = ""
        for key, value in exclusive_dict.items():
            product_list.append(value)
            product_list.sort(key=lambda x: getattr(x, 'productid'))
            product_list_string = '\n'.join([str(elem) for elem in product_list])
        return print(product_list_string)

    def view_all_prods(self):
        """
        This is a method to view all products by ID low to high
        1. It adds the dictionary values to a list
        2. then uses the .sort method and lambda, getattr to sort by "productId"
        3. This list is then converted to a string for printing
        """
        product_list = []
        product_list_string = ""
        for key, value in product_dict.items():
            product_list.append(value)
            product_list.sort(key=lambda x: getattr(x, 'productid'))
            product_list_string = '\n'.join([str(elem) for elem in product_list])
        return print(product_list_string)


class BargainHunters(Customer):
    """
    This is the Loyal Customers Class. It is a sub-class of Customer.
    """
    def __init__(self, name, customerid):
        super().__init__(name, customerid)

    def __str__(self):
        """This method prints the Bargain Hunter Customer Object"""
        return "-" * 20 + "\n" \
                          "Customer Name: {}\nCustomer ID: {}\nCustomer Type: Bargain Hunter" \
                          "".format(self.name, self.customerid) + "\n" + "-" * 20


class ShoppingCart(object):
    """
    This is the shopping cart class. It uses composition to take some customer details.
    """
    # CLASS OBJECT ATTRIBUTES
    def __init__(self, shopping_cart, customer, subtotal=0):
        self.shopping_cart = shopping_cart
        self.obj_customer = customer
        self.subtotal = subtotal
    # METHODS

    def __str__(self):
        """This method prints the cart contents, subtotal, customer details."""
        product_list = []
        product_list_string = ""
        for product_key, product_value in product_dict.items():
            for shopping_cart_key, shopping_cart_value in self.shopping_cart.items():
                if product_key == shopping_cart_key:
                    product_list.append(product_value + ", qty: " + str(shopping_cart_value))
                product_list_string = '\n'.join([str(elem) for elem in product_list])

        return "\nSHOPPING CART DETAILS\nCustomer Name: {}\nCustomer ID:{}\n{}\n--------------------"\
               "\n\nSubtotal: €{:.2f}"\
            .format(self.obj_customer.name, self.obj_customer.customerid, product_list_string, self.subtotal)

    def add_to_cart(self):
        """
        This is the add to cart method. It does this by checking if the productID is in the product dictionary.
        If it is not in the product dictionary, the user is prompted to add another product in.
        If the item is already in the cart, the quantity is added to the value. If not, the quantity is the value.
        """
        while True:
            try:
                productid = int(input("Enter the ID of the product you would like to add: "))
                qty = int(input("Enter the quantity you would like to add "))
                if product_dict[productid] is False:
                    print("Invalid ProductID. Please enter again.")
                    current_cart.add_to_cart()
                if qty == 0:
                    print("You cannot add 0 products. Please enter a quantity over 0.")
                    current_cart.add_to_cart_bargain()
            except KeyError:
                print("This product does not exist.")
            except ValueError:
                print("That is not a valid input. All ID's and quantities must be integers. ")
            else:
                if productid in self.shopping_cart and product_dict:
                    self.shopping_cart[productid] += qty
                    print("Item(s) added to cart")
                    return self.shopping_cart
                elif productid not in self.shopping_cart:
                    self.shopping_cart[productid] = qty
                    print("Item(s) added to cart")
                    return self.shopping_cart
                else:
                    print("That is not a valid ProductID.")

    def add_to_cart_bargain(self):
        """
        This is the add to cart method. It does this by checking if the productID is in the product dictionary.
        If it is not in the product dictionary, the user is prompted to add another product in.
        If the item is already in the cart, the quantity is added to the value. If not, the quantity is the value.
        """
        while True:
            try:
                productid = int(input("Enter the ID of the product you would like to add: "))
                qty = int(input("Enter the quantity you would like to add "))
                if bargain_bin[productid] is False:
                    print("Invalid ProductID. Please enter again.")
                    current_cart.add_to_cart_bargain()
                if qty == 0:
                    print("You cannot add 0 products. Please enter a quantity over 0.")
                    current_cart.add_to_cart_bargain()
            except KeyError:
                print("Invalid ProductID. Please enter again.")
            except ValueError:
                print("That is not a valid input. All ID's and quantities must be integers. ")
            else:
                if productid in self.shopping_cart and bargain_bin:
                    self.shopping_cart[productid] += qty
                    print("Item(s) added to cart")
                    return self.shopping_cart
                elif productid not in self.shopping_cart:
                    if productid in bargain_bin:
                        self.shopping_cart[productid] = qty
                        print("Item(s) added to cart")
                        return self.shopping_cart
                else:
                    print("That is not a valid ProductID.")

    def remove_from_cart(self):
        """
        This is the remove from cart method. It does this by checking if the productID is in the cart dictionary.
        If it is not in the product dictionary, a key error is raised, and the user prompted again.
        If the item is already in the cart, the quantity is removed from the value.
        """
        while True:
            try:
                productid = int(input("Enter the ID of the product you would like to remove from your shopping cart "))
                qty = int(input("How many would you like to remove? "))
                if self.shopping_cart[productid] == qty:
                    del self.shopping_cart[productid]
                elif self.shopping_cart[productid] <= qty:
                    print("You do not have that many to remove. Item deleted.")
                    del self.shopping_cart[productid]
                elif self.shopping_cart[productid] >= qty:
                    self.shopping_cart[productid] -= qty
                else:
                    print("Cart empty.")
                print("Item(s) removed.")
                return self.shopping_cart
            except KeyError:
                print("Invalid ProductID number. Please try again. ")
            except ValueError:
                print("That is not a valid input. All ID's and quantities must be integers. ")

    def get_subtotal(self):
        """
        This is the get_subtotal method. It calculates the subtotal of the qty in the cart * product.price.
        This is done by overwriting the * method in Product, appending the values to a list, and sum(list).
        :return: self.subtotal
        """
        product_list = []
        for product_key, product_value in product_dict.items():
            for shopping_cart_key, shopping_cart_value in self.shopping_cart.items():
                if product_key == shopping_cart_key:
                    product_list.append(product_value * shopping_cart_value)
        self.subtotal = sum(product_list)
        return self.subtotal

    def __mul__(self, other):
        if type(other) == float:
            return self.subtotal * other

    def __sub__(self, other):
        if type(other) == int or type(other) == float:
            return other - self.subtotal


class Product(object):
    """
    This is the product class.
    """
    # CLASS OBJECT ATTRIBUTES
    def __init__(self, name, productid, price, exclusive=bool):
        self.name = name
        self.productid = productid
        self.price = price
        self.exclusive = exclusive

    # METHODS
    def __str__(self):
        """This method prints each product and all its relevant details."""
        return "-" * 20 + "\nProduct Name: {}\nProduct ID: {}\nProduct Price: €{:.2f}\nExclusive: {}".format\
            (self.name, self.productid, self.price, self.exclusive) + "\n" + "-" * 20

    def __lt__(self, other):
        """This overloading method overwrites the "<" symbol for sorting the bargain products in the dictionaries."""
        if type(other) == Product:
            return self.price < other.price

    def __mul__(self, other):
        """This overloading method overloads the "*" symbol for calculating the subtotal for the cart."""
        if type(other) == int:
            return self.price * other

    def __add__(self, other):
        """This overloading method overloads the "+" symbol for the print_cart method."""
        if type(other) == str:
            return ("ID: " + str(self.productid) + " " + self.name + ", Price: €" + str(self.price)) + other


# ------------------------------------------------ FUNCTIONS ----------------------------------------------------------
def create_product_dict():
    """
    This is a function that creates the product dictionary from a file. It does this by reading the file, splitting
    to a list, and creating a dictionary from the list using indexes.

    The dictionary is in the format where the keys are the ProductID and the values are the product details. The values
    are made into a tuple and the class "Product" is applied to them.
    """
    my_file = open("product_list.txt", "r")
    product_list = []
    product_dict = {}
    for line in my_file:
        line = line.strip("\n")
        product_list.append(line.split(" "))
    for attribute in product_list:
        product_dict[int(attribute[0])] = Product(str(attribute[1]), int(attribute[2]), int(attribute[3]),
                                                  eval(attribute[4]))
    return product_dict


def create_bargain_bin(product_dict):
    """
    This function creates the bargain products/ non-exclusive products.
    It is made using the boolean .value == False, i.e. if the product is not exclusive, it is added to this dictionary.
    :param product_dict:
    :return: bargain_bin
    """
    bargain_bin = {}
    for key, value in product_dict.items():
        if value.exclusive is False:
            bargain_bin[key] = value
    return bargain_bin


def create_exclusive_product_dict(product_dict):
    """
    This function creates the exclusive products.
    It is made using the boolean .value == True, i.e. if the product is exclusive, it is added to this dictionary.
    """
    exclusive_dict = {}
    for key, value in product_dict.items():
        if value.exclusive is True:
            exclusive_dict[key] = value
    return exclusive_dict


def create_customer():
    """
    This is the function for creating the customer.
    """
    while True:
        try:
            name = str(input("Enter name.\nPlease note that names must contain letters only.\n> "))
            customerid = int(input("Enter ID number.\nID's must only be digits.\n> "))
            address = str(input("Enter address\n> "))
            phone = str(input("Enter phone number.\nPhone numbers must only be digits, and 10 digits long.\n> "))
            name.isalpha()
            if name.isalpha() is False:
                create_customer()
            elif len(phone) != 10:
                create_customer()
            elif phone.isdecimal() is False:
                create_customer()
        except ValueError:
            print("Wrong input. Name must be letters. ID must be digits.")
        else:
            while True:
                try:
                    print(
                        "Would the customer like to become a Loyal Customer?\n"
                        "For only €10 a year, they can receive access to exclusive products, "
                        "deals and FREE DELIVERY in Ireland.\n\n"
                        "Please select option:\n"
                        "1. Loyal Customer\n"
                        "2. Bargain Hunter"
                    )
                    selection = int(input("\n> "))
                    if selection == 1:
                        new_customer = LoyalCustomers(name, customerid)
                        new_customer.set_address(address)
                        new_customer.set_phone_number(phone)
                        print("The customer", name, "has been created. Below are their details:\n", new_customer)
                        return new_customer
                    elif selection == 2:
                        new_customer = BargainHunters(name, customerid)
                        new_customer.set_address(address)
                        new_customer.set_phone_number(phone)
                        print("The customer", name, "has been created. Below are their details:\n", new_customer)
                        return new_customer
                    else:
                        print("Invalid input. Please select a number between 1 and 2.")
                        continue
                except ValueError:
                    print("Wrong input. Please select an option 1 or 2. ")


# ------------------------------------------------ MENUS --------------------------------------------------------------


def list_products_submenu(new_customer):
    """
    This is the submenu for listing products. Depending on what type of customer you are, different products are shown.
    Loyal Customers have options to view all 3 dictionaries, whereas Bargain Hunters are only shown the Bargain Bin
    """
    print("List products selected.\n")
    """Need options for bargain hunters or loyal hunters"""
    if isinstance(new_customer, BargainHunters) is True:
        print("Here is the bargain bin, priced low to high")
        new_customer.view_bargain_bin()
    elif isinstance(new_customer, LoyalCustomers) is True:
        print(
            "What products would the customer like to view?\n"
            "1. Exclusive Products\n"
            "2. All products\n"
            "3. Non-exclusive products priced low-high\n"
            "Alternatively, enter any other number to go back to the main menu.\n> "
        )
        while True:
            try:
                subselection = int(input("\n> "))
                if subselection == 1:
                    print("EXCLUSIVE PRODUCTS:")
                    new_customer.view_exclusive_prods()
                elif subselection == 2:
                    print("ALL PRODUCTS:")
                    new_customer.view_all_prods()
                elif subselection == 3:
                    print("Here is the bargain bin, priced low to high")
                    new_customer.view_bargain_bin()
            except ValueError:
                print("Integers only. Please enter from 1 to 3.\n"
                      "Alternatively, enter any other number to go back to the main menu.")
                continue
            else:
                print("Back to the Main Menu ")
                break
    else:
        print("Back to the Main Menu")


def add_or_remove_submenu(new_customer, current_cart):
    """
    This is the add_or_remove products submenu.
    """
    print("Add or Remove from cart selected.\n"
          "Please select what you would like to do.\n"
          "1. Add a product to your cart\n"
          "2. Remove a product from your cart\n"
          "Alternatively, enter any other number to go back to the main menu.\n> ")
    if isinstance(new_customer, LoyalCustomers) is True:
        while True:
            try:
                subselection = int(input("\n> "))
                if subselection == 1:
                    current_cart.add_to_cart()
                elif subselection == 2:
                    if current_cart.shopping_cart == {}:
                        print("Your cart is empty. You cannot remove from this cart.")
                    else:
                        current_cart.remove_from_cart()
            except ValueError:
                print("This is not a valid input. Please enter a number between 1 and 2.\n"
                      "Alternatively, enter any other number to go back to the main menu.")
            else:
                break
    else:
        while True:
            try:
                subselection = int(input("\n> "))
                if subselection == 1:
                    current_cart.add_to_cart_bargain()
                elif subselection == 2:
                    if current_cart.shopping_cart == {}:
                        print("Your cart is empty. You cannot remove from this cart.")
                    else:
                        current_cart.remove_from_cart()
            except ValueError:
                print("This is not a valid input. Please enter a number between 1 and 2.\n"
                      "Alternatively, enter any other number to go back to the main menu.")
            else:
                break


def payment(new_customer, shopping_cart, current_cart):
    """This is the payment function. It finishes the program."""

    while True:
        try:
            card_number = int(input("Enter the long number on your card (16 digits).\n> "))
            cvv = input("Enter your CVV\n> ")
        except ValueError:
            print("This is not a valid input. Please use numbers.")
        else:
            card_number = str(card_number)
            cvv = str(cvv)
            new_customer.set_card_number(card_number)
            new_customer.set_cvv(cvv)
            if len(card_number) == 16 and len(cvv) == 3:
                print("Thank you for shopping with us and have a good day!")
                exit()
            else:
                print("You have entered you card details incorrectly. Please enter again.")
                payment(new_customer, shopping_cart, current_cart)


def final_checkout(new_customer, shopping_cart, current_cart):
    """
    This is the final checkout submenu. It prompts the user for payment details and then exits the program.
    There are different options depending what user type is handling the program
    """
    if isinstance(new_customer, BargainHunters) is True:
        print("Is the customer sure that they do not want to become a Loyal Customer?\n"
              "There are many benefits. For only €10 a year, they can receive access to exclusive products, "
              "deals and FREE DELIVERY in Ireland.\n\n"
              "We will even give you 10% off your subtotal TODAY if you sign up!\n"
              "Please select option:\n"
              "1. Stay a Bargain Hunter\n"
              "2. Join the Loyalty Customer scheme")
        while True:
            try:
                selection = int(input("\n> "))
            except ValueError:
                print("This is not a valid input. Please enter a number between 1 and 2.")
            else:
                if selection == 1:
                    subtotal = current_cart.get_subtotal()
                    print("That's a shame! You are missing out on a lot! Maybe next time.")
                    print("Your subtotal is: €{:.2f}".format(subtotal))
                    payment(new_customer, shopping_cart, current_cart)
                elif selection == 2:
                    new_customer = LoyalCustomers(new_customer.name, new_customer.customerid)
                    print("Your updated details are:\n", new_customer)
                    old_subtotal = current_cart.get_subtotal()
                    subtotal = (current_cart.subtotal * .9) + 10
                    savings = abs(subtotal - old_subtotal)
                    print("Your old subtotal was: €{:.2f}".format(old_subtotal))
                    print("Your new subtotal (including membership fee) is: €{:.2f}".format(subtotal))
                    print("Your savings today are: €{:.2f}".format(savings))
                    payment(new_customer, shopping_cart, current_cart)
    elif isinstance(new_customer, LoyalCustomers) is True:
        print("Today is your lucky day! We are running a special offer for Loyal Customers only!\n"
              "Today you will receive 20% off. We will also waive your membership fee.\n")
        old_subtotal = current_cart.get_subtotal()
        subtotal = (current_cart.subtotal * .8)
        savings = abs(subtotal - old_subtotal)
        print("Your old subtotal was: €{:.2f}".format(old_subtotal))
        print("Your new subtotal is: €{:.2f}".format(subtotal))
        print("Your savings today are: €{:.2f}\n".format(savings))
        payment(new_customer, shopping_cart, current_cart)


def checkout(new_customer, shopping_cart, current_cart):
    """This is the initial checkout submenu. It directs the end user either back to the main menu or onto the final
    checkout submenu"""
    print(
        "Checkout selected.\n"
        "Here is your current cart and subtotal.\n")
    current_cart.get_subtotal()
    print(current_cart)
    print(""
          "Are you happy to proceed to checkout?\n"
          "1. No\n"
          "2. Yes\n"
          "Alternatively, hit any other number to go back to the main menu.")
    while True:
        try:
            selection = int(input("\n> "))
        except ValueError:
            print("This is not a valid input. Please enter a number between 1 and 2.")
        else:
            if selection == 1:
                return new_customer, shopping_cart, current_cart
            elif selection == 2:
                final_checkout(new_customer, shopping_cart, current_cart)
            else:
                return new_customer, shopping_cart, current_cart


def main_menu():
    """This is the main menu function. """
    global new_customer, current_cart, shopping_cart
    main_menu_options = (
        "\nWhat would you like to do? Enter the number.\n"
        "1. Create a customer\n"
        "2. List Products\n"
        "3. Add or remove a product from the cart\n"
        "4. See current shopping cart\n"
        "5. Checkout\n"
        "6. Quit program"
    )
    print(main_menu_options)
    check_customer_created = 0
    while True:
        try:
            selection = int(input("\n> "))
        except ValueError:
            print("This is not a valid input. Please enter a number between 1 and 6.")
        else:
            if selection == 1:
                print("Create a customer selected.\n")
                new_customer = create_customer()
                shopping_cart = {}
                current_cart = ShoppingCart(shopping_cart, new_customer)
                check_customer_created = 1
            if check_customer_created == 1:
                if selection == 2:
                    list_products_submenu(new_customer)
                    print(main_menu_options)
                elif selection == 3:
                    add_or_remove_submenu(new_customer, current_cart)
                    print(main_menu_options)
                elif selection == 4:
                    print("View current cart selected")
                    if current_cart.shopping_cart == {}:
                        print("The shopping cart is empty.")
                        print(main_menu_options)
                    else:
                        current_cart.get_subtotal()
                        print(current_cart)
                        print(main_menu_options)
                elif selection == 5:
                    if current_cart.shopping_cart == {}:
                        print("The shopping cart is empty. You cannot checkout.")
                        print(main_menu_options)
                    else:
                        checkout(new_customer, shopping_cart, current_cart)
                        print(main_menu_options)
                elif selection == 6:
                    print("Quit program selected")
                    exit()
                else:
                    print(main_menu_options)
            else:
                print("Please create a customer first.\nSelect option 1.")


def test():
    """This is a test function to show the functionality of the program"""
    print("Test 1. Create Customers. ")
    print()

    jenny = LoyalCustomers("Jenny Kelly", 1)
    jenny.set_address("123 Made up street")
    jenny.set_phone_number("5555666666")
    print(jenny)
    print()

    print("Create a bargain hunter")
    johnny = BargainHunters("Johnny Kenna", 2)
    johnny.set_address("237 Made up street")
    johnny.set_phone_number("6565656566")
    print(johnny)
    print()

    print("Test 2. View products")
    print()
    print("if customer = bargain hunter they are only shown one option")
    johnny.view_bargain_bin()
    print()

    print("If the customer is a loyal customer they are shown 3 options:")
    print("Exclusive Products")
    jenny.view_exclusive_prods()
    print("All Products")
    jenny.view_all_prods()
    print("Bargain Bin")
    jenny.view_bargain_bin()
    print()

    print("Test 3. Creating a cart")
    shopping_cart = {}
    current_cart = ShoppingCart(shopping_cart, johnny)
    print(current_cart)
    print()

    print("Test 4. Add Products")  # For both this method I have created parameters within it.
    shopping_cart = {2: 4, 1: 3}  # So I am showing it with a dummy cart dictionary
    current_cart.add_to_cart()
    current_cart = ShoppingCart(shopping_cart, johnny)
    print(current_cart)
    print()

    print("Test 5. Remove Products")  # For both this method I have created parameters within it.
    shopping_cart = {2: 2}  # So I am showing it with a dummy cart dictionary
    current_cart = ShoppingCart(shopping_cart, johnny)
    current_cart.remove_from_cart()
    print(current_cart)
    print()

    print("Test 6. Get subtotal & View cart")
    current_cart.get_subtotal()
    print(current_cart)


# DRIVER CODE


product_dict = create_product_dict()  # creates product dictionary
exclusive_dict = create_exclusive_product_dict(product_dict)  # creates exclusive dictionary
bargain_bin = create_bargain_bin(product_dict)  # creates bargain bin dictionary
#test()  # test function
main_menu()  # Main menu