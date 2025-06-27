class dad():
    def __init__(self,eyecolour,face):
            self.eyecolour=eyecolour
            self.face=face
            
    def display(self):
          print("eye colour is ",self.eyecolour)
          print("face is ",self.face)
        
class son (dad):
      def __init__(self,name,age,eyecolour,face):
            self.name=name
            self.age=age
            dad. __init__(self,eyecolour,face)
ob1=son("rehan","10","blue","fair")
ob1.display()
            

            
