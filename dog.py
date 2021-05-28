class Dog:
      def __init__(self,name,color,breed,age):
          self.name=name
          self.color=color
          self.breed=breed
          self.age=age

      def bark(self):
          return "My pet's name is {} and it is {} in colour.".format(self.name,self.color)

      def run(self):
        return "{} is a {}.He is a very cute dog.".format(self.name,self.breed)