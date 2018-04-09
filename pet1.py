



class Pet:

    def __init__(self, name, strength):
        self.name = name
        self.strength = strength
        self.x = 0
        self.y = 0
        self.direction = 0
        self.is_alive = True
        self.health = 10
        self.level = 1


    def eat(self):
        if self.is_alive:
            print(self.name + " goes 'Nom Nom Nom...'")
        else:
            print("Dis boi ded.")

    def sleep(self):
        print("zzzzzzzzzzzzzz...")

    def play(self):
        print("Yippee!")

    def rotate_right(self):
        self.direction += 1

        if self.direction == 4:
            self.direction = 0

    def rotate_left(self):
        self.direction -= 1

        if self.direction == -1:
            self.direction = 3

    def move(self):
        if self.direction == 0:
            self.y += 1
        elif self.direction == 1:
            self.x += 1
        elif self.direction == 2:
            self.y -= 1
        elif self.direction == 3:
            self.x -= 1

    def train(self):
        train = input("Would you like to level up " +  self.name + "? (y/n)")

        if train == "y":
            self.level += 1 
            self.strength += 1
            print(self.name + " has reached level " + str(self.level) + ". "\
                  + self.name + " 's attack points have reached " + str(self.strength) + ".")


    def attack(self, other):
        print(self.name + " attacks " + other.name + "!")

        other.health -= self.strength

        print(other.name + "'s health drops to " + str(other.health))

        if other.health > 0:
            attack_back = input("Will " + other.name + " attack back? (y/n) ")

            if attack_back == "y":
                other.attack(self)


        if other.health <= 0:
            print(self.name + " kills " + other.name + "!")
            other.is_alive = False

            
            print(self.name + " has gained 5 attack points!")
            self.strength += 5

  
    def __repr__(self):
        return "Name: " + self.name + \
               " [x=" + str(self.x) + \
               ", y=" + str(self.y) + \
               ", d=" + str(self.direction) + "]"
    

pet1 = Pet("Tic", 2)
pet2 = Pet("Tac", 2)
pet3 = Pet("Toe", 2)




