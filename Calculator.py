import math as m

class CalculatorState:
    def add(self, value1,value2):
        return value1+value2

    def subtract(self, value1, value2):
        return value1-value2

    def multiply(self, value1,value2):
        return value1*value2

    def divide(self, value1,value2):
        if isinstance(value2,int) and isinstance(value1,int):
            return value1//value2
        else:
            return value1/value2

    def power(self, value1,value2):
        return m.pow(value1,value2)

    def simpleInterest(self,principle,interest,rate):
        if rate>1:
            rate = rate/100
        return principle*interest*rate

    def compoundInterest