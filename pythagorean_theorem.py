import math as mt

# For finding the hypotenuse
class Hypotenuse:
    
    def __init__(self, short_side_1 : int|float = 0, short_side_2 : int|float = 0):
        self.short_side_1 = short_side_1
        self.short_side_2 = short_side_2
        
    def find_hypotenuse(self) -> int|float:
        try:
            if(self.short_side_1 < 1 or self.short_side_2 < 1):
                return "Enter number that is positive"
            
            hypotenuse = mt.sqrt(self.short_side_1**2 + self.short_side_2**2)
            return hypotenuse
        except:
            return "Error"
    
# Finding either of the short side
class Short_side:
    
    def __init__(self, hypotenuse : int|float = 0, short_side_given : int|float = 0):
        self.hypotenuse = hypotenuse
        self.short_side_given = short_side_given
        
    def find_short_side(self) -> int|float:
        try:
            if(self.hypotenuse < 1 or self.short_side_given < 1):
                return "Enter number that is positive"
            
            if(self.hypotenuse <= self.short_side_given):
                return "Hypotenuse must be greater than the short side"
            
            short_side = mt.sqrt(self.hypotenuse**2 - self.short_side_given**2)
            return short_side
        except:
            return "Error"
    
    
hypo = Hypotenuse(short_side_1=5, short_side_2=5)
hypothenuse = hypo.find_hypotenuse()
print (hypothenuse)

short = Short_side()
short_side = short.find_short_side()
print(short_side)