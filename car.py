class Car:
      def __init__(self,make,model,color,registration):
          self.make=make
          self.model=model
          self.color=color
          self.registration=registration

      def start(self):
          return "I bought a {} {} {} whose registration number is {} .It has no trouble moving".format(self.color,self.make,self.model,self.registration)

      def speed(self):
          mileage=5000
          return "A {} has a mileage of {} and it goes at a very high speed.".format(self.make,mileage)