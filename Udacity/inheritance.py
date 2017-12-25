class Parent():

    def __init__(self, last_name, eye_color):
        print('parent constructor class')
        self.last_name = last_name
        self.eye_color = eye_color

    def show_info(self):
        print('Last Name: {}'.format(self.last_name))
        print('Eye color: {}'.format(self.eye_color))


class Child(Parent):

    def __init__(self,last_name, eye_color, number_of_toys):
        print('This is child init method')
        Parent.__init__(self, last_name, eye_color)
        self.number_of_toys = number_of_toys



# output

#Devidas = Parent('Kale', 'Blue')
#Devidas.show_info()
#print(Devidas.eye_color)

Aniket = Child('Kale', 'black', 5)
print(Aniket.number_of_toys)
Aniket.show_info()


