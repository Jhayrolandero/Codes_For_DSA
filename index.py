import math

class Calculate:
    
    def get_parameters(self, a: int|float, oper1: str, b: int|float, oper2: str, c: int|float) -> None:
        self.a = a
        self.oper1 = oper1
        self.b = b
        self.oper2 = oper2
        self.c = c
        
        
    def calculate_result(self) -> float:
        eq1 = eval("self.a" + self.oper1 + "self.b")        
        res = eval("math.sqrt(eq1)" + self.oper2 + "math.sqrt(self.c)")       
        return res
    
    
num1 = Calculate()
questions = {
    "a": [4355, 2, 2, 1225, 1620, 243, 1150, 2635, 303, 4],
    "oper1": ["/", "*", "*", "-", "/", "+", "/", "/", "+", "*"],
    "b": [5, 146, 241, 755, 4, 245, 2, 5, 606, 70],
    "oper2": ["/", "/", "*", "/", "-", "/", "*", "*", "*", "/"],
    "c": [975, 869, 374, 612, 100, 698, 1150/2, 523, 466, 377]
}
    
for i in range (0, len(questions["a"])):
    num1.get_parameters(a = questions["a"][i],
                        oper1= questions["oper1"][i],
                        b= questions["b"][i],
                        oper2= questions["oper2"][i],
                        c= questions["c"][i])    
    
    res = num1.calculate_result()
    print(f"Question {i+1}: {res}")
        