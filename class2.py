class Iostring():
    def __init__(self):
        self.str=""
    def get_string(self):
        self.str=input("enter a word")
    def print_string(self):
        print("the result is ",self.str.upper())
str1=Iostring()
str1.get_string()
str1.print_string()