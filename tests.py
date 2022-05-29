# Initially I would just try without the test

# 1st step would be to create a dummy test
# helloworld or whatever
# this will obviously pass, no functionality

# if it is required
# write a more robust, more serious
# for one of the endpoints for the flask app
# /timeseries

"""
I have this input
I do an API passing this payload (input)
You get an output
You validate whether the output is okay


Ex:
payload = 2 + 2
/add/payload
actual output 4
validate whether this is 4
"""


class Square:
    def __init__(self, side):
        """ creates a square having the given side
        """
        self.side = side
  
    def area(self):
        """ returns area of the square
        """
        return self.side**2
  
    def perimeter(self):
        """ returns perimeter of the square
        """
        return 4 * self.side
  
    def __repr__(self):
        """ declares how a Square object should be printed
        """
        s = 'Square with side = ' + str(self.side) + '\n' + \
        'Area = ' + str(self.area()) + '\n' + \
        'Perimeter = ' + str(self.perimeter())
        return s
  
  
if __name__ == '__main__':
    # read input from the user
    # side = int(input('enter the side length to create a Square: '))
    side = 4
      
    # create a square with the provided side
    square = Square(side)
  
    # print the created square
    print(square)