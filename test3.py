pet_name = input(f"What's your pet's name? ")  # Get the pet's name from user
species = input(f"What type of animal is this pet? ")  # get the pet's species from user


class Pet:  # Define the Pet class
    def __init__(self, name, animal_type, hunger, happiness):
        self.name = str(name)
        self.animal_type = str(animal_type)
        self.hunger = int(hunger)
        self.happiness = int(happiness)

# Feed pet (Hunger down by 30%)
    def eat(self):
        hunger -= 30
        print(f"You fed {self.name}. It is now {hunger} percent hungry.")
# Play with pet (happiness up by 10%)
    def play(self):
        happiness += 10
        print(
            f"You played with your {self.animal_type} {self.name}. It is now {self.happiness} percent happy."
        )
# Check pet status
    def status(self):
        print(f"{self.name}'s status:")
        print(f"Hunger: {self.hunger}")
        print(f"Happiness: {self.happiness}")
        print(f"Species: {self.animal_type}")


# Create an instance of Pet using the user input
# Assuming you're creating a pet of type "dog", with hunger and happiness at a default level
my_pet = Pet(name=pet_name.capitalize(), animal_type=species, hunger=50, happiness=50)

# Print out the details of the pet
print(
    f"Your pet's name is {my_pet.name}. It's a {my_pet.animal_type} with {my_pet.hunger} percent hunger and happiness level {my_pet.happiness}."
)

while True:
    print(f"Day {max} has begun.")
    
    call1 = input
    call2 = input(f"what would you like to do with {my_pet.name}")

    if call2.lower() == "feed":
        hungry = Pet.eat()