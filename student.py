class Student:
      def __init__(self,name,school,age,nationality,gender):
            self.name=name
            self.school=school
            self.age=age
            self.nationality=nationality
            self.gender=gender

      def speak(self):
          return "Hello my name is {} and i am {} years old.I am {}".format (self.name,self.age)

      
