class Attack:
    def __init__(self, name, damage):
        self.name = name
        self.damage = damage

class Defense:
    def __init__(self, name, defense_rating):
        self.name = name
        self.defense_rating = defense_rating

class Robot:
    def __init__(self, name, attack, defense, hp):
        self.name = name
        self.attack = attack
        self.defense = defense
        self.hp = hp

    def attack(self, other_robot):
        damage = self.attack.damage - other_robot.defense.defense_rating
        other_robot.hp -= damage
        print(f"{self.name} attacks {other_robot.name} with {self.attack.name} for {damage} damage.")

    def defend(self, attack):
        damage = attack.damage - self.defense.defense_rating
        self.hp -= damage
        print(f"{self.name} defends against {attack.name} for {damage} damage.")


class Game:
    def __init__(self, robot1, robot2):
        self.robot1 = robot1
        self.robot2 = robot2
        self.round_number = 1

    def run_game(self):
        while self.robot1.hp > 0 and self.robot2.hp > 0:
            print(f"Round {self.round_number}")
            self.robot1_action()
            if self.robot2.hp <= 0:
                break
            self.robot2_action()
            self.round_number += 1

        if self.robot1.hp > 0:
            print(f"{self.robot1.name} wins!")
        else:
            print(f"{self.robot2.name} wins!")

    def robot1_action(self):
        print(f"{self.robot1.name}, pilih aksi:")
        print("1. Serang")
        print("2. Bertahan")
        print("3. Menyerah")
        action = input()

        if action == "1":
            self.robot1.attack(self.robot2)
        elif action == "2":
            self.robot1.defend(self.robot2.attack)
        elif action == "3":
            print(f"{self.robot1.name} gives up.")
            self.robot2.hp = 1

    def robot2_action(self):
        print(f"{self.robot2.name}, pilih aksi:")
        print("1. Serang")
        print("2. Bertahan")
        print("3. Menyerah")
        action = input()

        if action == "1":
            self.robot2.attack(self.robot1)
        elif action == "2":
            self.robot2.defend(self.robot1.attack)
        elif action == "3":
            print(f"{self.robot2.name} gives up.")
            self.robot1.hp = 1

attack1 = Attack("Punch", 10)
attack2 = Attack("Kick", 12)

defense1 = Defense("Block", 5)
defense2 = Defense("Dodge", 4)

robot1 = Robot("Atreus", attack1, defense1, 100)
robot2 = Robot("Daedalus", attack2, defense2, 90)

game = Game(robot1, robot2)
game.run_game()
