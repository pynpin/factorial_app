from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.properties import StringProperty
from primes import primes
import math

limit = 598

def factorial(x):
    if x > limit:
        return f"{x}!\nThe result was too big to be displayed"
    if x in (0,1):
        return 1
    return x * factorial(x-1)

def double_factorial(x):
    if x==0:
        return "No result"
    if x == 1:
        return 1
    if x == 2:
        return 2
    if x > limit:
        return f"{x}!!\nThe result was too big to be displayed"
    return x * double_factorial(x - 2)
    
def multifactorial(x, y):
    match x:
        case 0:
            return 1
        case 1:
            return 1
        case 2:
            return 2
        case 3:
            return 3
        case 4:
            return 4
    if x > limit:
        list = ["!" for i in range(y)]
        exc = "".join(list)
        return f"{x}{exc}\nThe result was too big to be displayed"
    return x * multifactorial(x - y, y)

def subfactorial(x):
    if x == 0:
        return 1
    if x == 1:
        return 0
    if x > limit:
        return f"!{x}\nThe result was too big to be displayed"
    a, b = 1, 0
    for i in range(2, x + 1):
        a, b = b, (i - 1) * (a + b)
    return b

def primorial1(x):
    result = 1
    if x > limit:
        return f"{x}#\nThe result was too big to be displayed"
    for p in primes:
        if p > x:
            break
        result *= p
    return result
    
def primorial2(x):
    result = 1
    if x > limit:
        sub = str.maketrans("0123456789", "₀₁₂₃₄₅₆₇₈₉")
        new_x = str(x).translate(sub)
        return f"p{new_x}#\nThe result was too big to be displayed"
    if x == 0:
        return 0
    for i in range(0, x):
        result *= primes[i]
    return result
    
def falling_factorial(x, y):
    if y==0:
        return 1
    if x-y > 1000:
        sub = str.maketrans("0123456789", "₀₁₂₃₄₅₆₇₈₉")
        new_y = str(y).translate(sub)
        return f"({x}){new_y}\nThe result was too big to be displayed"
    return (x-y+1) * falling_factorial(x, y-1)
    
def rising_factorial(x, y):
    if y==0:
        return 1
    if x-y > 1000:
        sub = str.maketrans("0123456789", "⁰¹²³⁴⁵⁶⁷⁸⁹")
        new_y = str(y).translate(sub)
        return f"{x}⁽{new_y}⁾\nThe result was too big to be displayed"
    return (x+y-1) * rising_factorial(x, y-1)

def super_factorial(x):
    if x in (0, 1):
        return 1
    if x > 50:
        return f"{x}! * sf({x-1})\nThe result was too big to be displayed"
    return factorial(x) * super_factorial(x - 1)

def expo_factorial(x):
    if x in (0, 1):
        return 1
    if x == 5:
        return "5^262144\nThe result was too big to be displayed"
    if x > 5:
        return f"{x}^({x-1}$)\nThe result was too big to be displayed"
    return x ** expo_factorial(x - 1)

def hyper_factorial(x):
    if x==0:
        return "No result"
    if x == 1:
        return 1
    if x > 45:
        return f"{x}^{x} * H({x-1})\nThe result was too big to be displayed"
    return x ** x * hyper_factorial(x - 1)

class MainScreen(BoxLayout):
    result = StringProperty("Result will appear here")
    def calculate(self, mode, value):
        if len((value).strip()) != 0:
            try:
                x = int(value)
                match mode:
                    case "Factorial":
                        r = factorial(x)
                        self.result = f"{x}! = {r}"
                    case "Double":
                        r = double_factorial(x)
                        self.result = f"{x}!! = {r}"
                    case "Sub":
                        r = subfactorial(x)
                        self.result = f"!{x} = {r}"
                    case "Primorial1":
                        r = primorial1(x)
                        self.result = f"{x}# = {r}"
                    case "Primorial2":
                        r = primorial2(x)                        
                        sub = str.maketrans("0123456789", "₀₁₂₃₄₅₆₇₈₉")                        
                        new_x = str(x).translate(sub)                        
                        self.result= f"p{new_x}# = {r}"
                    case "Super":
                        r = super_factorial(x)
                        self.result = f"sf({x}) = {r}"
                    case "Expo":
                        r = expo_factorial(x)
                        self.result = f"{x}$ = {r}"
                    case "Hyper":
                        r = hyper_factorial(x)
                        self.result = f"H({x}) = {r}"
            except:
                self.result = "Invalid input"
        else:
            self.result = "Enter a number for n"
    def calculate_type(self, mode, value1, value2):      
        if len((value1).strip()) == 0 and len((value2).strip()) == 0:
            self.result = "Enter a number for n and x"  
        if len((value1).strip()) == 0 and len((value2).strip()) != 0:
            self.result = "Enter a number for n"
        if len((value1).strip()) != 0 and len((value2).strip()) == 0:
            self.result = "Enter a number for x"
        if len((value1).strip()) != 0 and len((value2).strip()) != 0:
            try:
                x = int(value1)
                y = int(value2)
                match mode:
                    case "Multi":
                        r = multifactorial(x, y)                        
                        list = ["!" for i in range(y)]
                        exc = "".join(list)
                        self.result = f"{x}{exc} = {r}"
                    case "Falling":
                        r = falling_factorial(x, y)
                        sub = str.maketrans("0123456789", "₀₁₂₃₄₅₆₇₈₉")
                        new_y = str(y).translate(sub)
                        self.result = f"({x}){new_y} = {r}"
                    case "Rising":         
                        r = rising_factorial(x, y)
                        sub = str.maketrans("0123456789", "⁰¹²³⁴⁵⁶⁷⁸⁹")
                        new_y = str(y).translate(sub)
                        self.result = f"{x}⁽{new_y}⁾ = {r}"
            except:
                self.result = "Invalid Input"
    
class FactorialApp(App):
    def build(self):
        return MainScreen()

FactorialApp().run()
