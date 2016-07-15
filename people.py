
#Krutarth Rao
class Person:
    #Represents a person.
    population = 0
 
    def __init__(self, name):
        #Initializes the person's data.
        self.name = name
        print ('Initializing' ,self.name)
 
        # When this person is created, he/she
        # adds to the population
        Person.population += 1
 
    def __del__(self):
        #I am dying.
        print (self.name,"says bye.")
 
        Person.population -= 1
 
        if Person.population == 0:
            print ('I was the last one.')
        else:
            print ('There are still',Person.population ,'people left.') 
    def sayHi(self):
        #Greeting by the person.
                #Should print "Hi, my name is Ben" for example if the name is Ben.
                print('Hi, my name is ',self.name)
 
 
 
    def howMany(self):
        #Prints the current population.
        #If there is only 1 person then it should print "I am the only one"
                #If there are 2 people for example , then print "We have 2 people here"
                if Person.population == 1:
                    print('I am the only one')
                elif Person.population > 1:
                    print('We have ',Person.population,' people here.')
 
 
def main():
 
      # Step 1: Ask for names of 2 people
      name1 = input('Name of Person 1? ')
      name2 = input('Name of Person 2? ')
      # Step 2: Initialize Person 1
      person1 = Person(name1)
      # Step 3: Use function sayHi() for Person 1
      person1.sayHi()
      # Step 4: Use howMany() for Person 1
      person1.howMany()
      # Step 5: Initialize Person 2
      person2 = Person(name2)
      # Step 6: Use function sayHi() for Person 2
      person2.sayHi()
      # Step 7: Use howMany() for Person 2
      person2.howMany()
      # Step 8: Say Hi to Person 1
      person1.sayHi()
      # Step 9: Use howMany() to Person 1
      person1.howMany()
      # Step 10: Terminate Person 1
      # Step 11: Terminate Person 2
 
main()
