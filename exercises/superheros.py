# Write your solutions for 1.5 here!
class Superheroes():
    def __init__(self,name,superpower,strength):
        self.name=name
        self.superpower=superpower
        self.strength=strength
    
    def ns(self):
        print (self.superpower + self.strength)

superman = Superheroes(superman,flying,8)