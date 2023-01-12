from random import randint


def attack(char_name, char_class):
    if char_class == 'warrior':
        return (f'{char_name} damage to the enemy {5 + randint(3, 5)}')
    if char_class == 'magician':
        return (f'{char_name} damage to the enemy {5 + randint(5, 10)}')
    if char_class == 'healer':
        return (f'{char_name} damage to the enemy {5 + randint(-3, -1)}')
def defense(char_name, char_class):
    if char_class == 'warrior':
        return (f'{char_name} blocked {10 + randint(5, 10)} damage')
    if char_class == 'magician':
        return (f'{char_name} blocked {10 + randint(-2, 2)} damage')
    if char_class == 'healer':
        return (f'{char_name} blocked {10 + randint(2, 5)} damage')
def special(char_name, char_class):
    if char_class == 'warrior': 
        return (f'{char_name} used a special skill "Stamina {80 + 25}"')
    if char_class == 'magician':
        return (f'{char_name} used a special skill "Attack {5 + 40}"')
    if char_class == 'healer':
        return (f'{char_name} used a special skill "Defense {10 + 30}"')




def start_training(char_name, char_class):
    if char_class == 'warrior':
        print(f'{char_name}, you are a Warrior, proficient in melee combat.')
    if char_class == 'magician':
        print(f'{char_name}, you are a Magician, masterfully taming the elements.')
    if char_class == 'healer':
        print(f'{char_name}, you are a Healer, a sorcerer who heals wounds.')
    print('Train your skills.')
    print('Enter one of these commands: attack — to attack an enemy, defense — to block an enemy attack, or special — to use your special power.')
    print('If you don\'t want to train, enter skip.')
    cmd = None
    while cmd != 'skip':
        cmd = input('Enter a command: ')
        if cmd == 'attack':
            print(attack(char_name, char_class))
        if cmd == 'defense':
            print(defense(char_name, char_class))
        if cmd == 'special':
            print(special(char_name, char_class))
    return 'The training is over.'

def choice_char_class():
    approve_choice = None
    char_class = None
    while approve_choice != 'y':
        char_class = input('Enter the class of your character: Warrior — warrior, Magician — magician, Healer — healer: ')
        if char_class == 'warrior':
            print('Warrior — a fierce melee fighter. Strong, resilient, and brave.')
        if char_class == 'magician':
            print('Magician — a brilliant long-range fighter. Master of magical powers.')
        if char_class == 'healer':
            print('Healer — a powerful shaman. Draws strength from nature, faith, and spirits.')
        approve_choice = input('Press (Y) to confirm or any other button to select another class').lower()
    return char_class


def main():
    print('Greetings, adventurer!')
    print('Before you start playing...')
    char_name = input('... state your name: ')
    print(f'Welcome, {char_name}! '
          'You have 80 stamina points, 5 attack points, and 10 defense points.')
    print(('You can choose one of the three ways of the Force:')
    print('Warrior, Magician, Healer')
    char_class = choice_char_class()
    print(start_training(char_name, char_class))
    

main()
