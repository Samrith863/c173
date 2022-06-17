class parent():
    def __init__(self):
        print("This is the parent class")
    def menu(dish):
        if dish=="burger":
            print("You can add the following toppings:")
            print("More cheese| Add jalapeno")
        elif dish=="iced_american":
            print("You can add one of the following toppings:")
            print("chocolate flavor| caramel flavor")
        else:
            print("Please enter a valid dish")
    def final_amount(dish,add_ons):
        if dish=="burger" and add_ons=="cheese":
            print("You need to pay 250 USD")
        elif dish=="burger" and add_ons=="jalapeno":
            print("you need to pay 350 USD")
        elif dish=="iced_american" and add_ons=="chocolate flavor":
            print("you need to pay 350 USD")
        elif dish=="iced_american" and add_ons=="caramel flavor":
            print("you need to pay 450 USD")
class child1(parent):
    def __init__(self,dish):
        self.new_dish=dish
    def get_menu(self):
        parent.menu(self.new_dish)
class child2(parent):
    def __init__(self,dish,add_ons):
        self.new_dish=dish
        self.add=add_ons
    def get_bill(self):
        parent.final_amount(self.new_dish,self.add)
        
obj1=child1("burger")
obj1.get_menu()
obj2=child2("burger","jalapeno")
obj2.get_bill()
