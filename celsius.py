#class to convert..
class Temperature:
    def __init__(self,temperature):
        self.temperature=temperature

    def convert_to_fahranheit(self):
        result=float((9*self.temperature)/5 + 32)
        return result
    def convert_to_celsius(self):
        result=float((self.temperature-32) *5/9)
        return result

t=Temperature(27)
print(t.convert_to_fahranheit())
print(t.convert_to_celsius())
        
