"""
COMP.CS.100 Product
Creator: Ishan Malu
Student id number: 154138420
"""

class Product:
    """
    This class defines a simplified product for sale in a store.
    """

    # TODO: Define all the methods here.  You can see what they are,
    #       what parameters they take, and what their return value is
    #       by examining the main-function carefully.
    #
    #       You also need to consider which attributes the class needs.
    #
    #       You are allowed to modify the main function, but your
    #       methods have to stay compatible with the original
    #       since the automatic tests assume that.

    def __init__(self,name,price):
        self.__name=name
        self.__price=price
        self.__percentage= 0.00
        self.__newPrice= price

    def printout(self):
        print(self.__name)
        print(f"  price: {self.__price:.2f}")
        print(f"  sale%: {self.__percentage:.2f}")

    def get_price(self):
        return self.__newPrice

    def set_sale_percentage(self,percent):
        self.__percentage= percent
        discount= self.__price*(percent/100)
        self.__newPrice = self.__price - discount


def main():
    ################################################################
    #                                                              #
    #  You can use the main-function to test your Product class.   #
    #  The automatic tests will not use the main you submitted.    #
    #                                                              #
    #  Voit käyttää main-funktiota Product-luokkasi testaamiseen.  #
    #  Automaattiset testit eivät käytä palauttamaasi mainia.      #
    #                                                              #
    ################################################################

    test_products = {
        "milk":   1.00,
        "sushi": 12.95,
    }

if __name__ == "__main__":
    main()