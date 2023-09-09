import math

class Quadratic:
    
    def get_equation(self, equation: str) -> None:
        self.equation = equation
    
    # Get a, b, c values
    def __get_a_b_c(self) -> dict:
        self.equation = self.equation.replace(" ", "")
        
        index_a = self.equation.index("x**2")
        index_b = self.equation.rindex("x")
        index_c = self.equation.index("=") 
        
        a = self.equation[:index_a]
        b = self.equation[index_a+4:index_b]
        c = self.equation[index_b+1:index_c]
        
        values = {
            "a" : int(a),
            "b" : int(b),
            "c" : int(c)
        }
        
        return values
    
    # Calculate the discriminant
    @staticmethod
    def __calculate_discriminant(a: int,b: int,c: int) -> int|float:
        discriminant = (b**2) - (4*(a*c))
        
        return math.sqrt(discriminant)
    
    # Calculate x1 and x2
    def calculate_x(self) -> dict:
        values = self.__get_a_b_c()
        discriminant_val = self.__calculate_discriminant(values["a"] , values["b"], values["c"])
        
        x1 = ((-1*(values["b"])) + discriminant_val) / (2 * values["a"])
        x2 = ((-1*(values["b"])) - discriminant_val) / (2 * values["a"])
        
        res = {
            "x1": x1,
            "x2": x2
        }
        
        return res
    
    
if __name__ == "__main__":
    ques = ["-15x**2 +11x -2 = 0", "-4x**2 -27x +7 = 0", "8x**2 -10x -3 = 0", "2x**2 +5x -3 = 0"]
    eq = Quadratic()
    for i in ques:
        eq.get_equation(i)
        res = eq.calculate_x()
        print(f'x1 = {res["x1"]}, x2 = {res["x2"]} \n')
