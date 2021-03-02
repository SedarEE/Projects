class Product():
    """A class representing a general product to be sold in a store."""

    def __init__(self, name, price,):
        """ Initialize the product with a name and a price. Set 
        the number of sold items to 0."""
        self.name = name
        self.price = price
        self.sold = 0
        self.items_sold = 0 
      
        


    def print_description(self):
        """Print a description of the product."""
        print(f"Item {self.name.title()} has a price of " +
              f"{self.price} and has been sold {self.sold} times.")

    def sell(self):
        """Simulate that the product has been sold. Update how often product was sold."""
        print(f"Selling item {self.name.title()} for {self.price}")
        self.sold += 1

     

  

product1 = Product('Lacra', '5')
product2 = Product('Kit-kat', '10')
product3 = Product('Marabou', '25')

product1.sell()
product1.sell()
product1.print_description()
print()

product2.sell()
product2.print_description()
print()

product3.sell()
product3.print_description()
print()