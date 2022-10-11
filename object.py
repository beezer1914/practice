#OOP
from unicodedata import name


class PlayerCharacter:
    def __init__(self, name, level):
        self.name = name
        self.level = level
    
    def run(self):
        print('run')
        return 'done'


player1 = PlayerCharacter('Goblin', 5)
player2 = PlayerCharacter('Ninja', 10)
player.attack = 50

print(player1.run())
print(player2.level)
