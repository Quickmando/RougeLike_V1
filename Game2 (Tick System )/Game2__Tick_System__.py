import random
from time import sleep

r = random
buff = 0

def copies(item, n):
    return [item[:] for _ in range(n)]

def empty_slot():
    return [0,0,0,'','']

# Items
NA = [0,0,0,'','']
Rusty_Sword = [0,3,0,'Rusty Sword']
Old_Bow = [0,3,0,'Old Bow']
Rusty_Helmet = [0,0,3,'Rusty Helmet']
Good_Helmet = [0,0,5,'Good Helmet']
Bandage = [10,0,0,'Bandage']
OldBandage = [5,0,0,'Old Bandage']
Ameulet = [3,0,3,'Amulet']
Necromancer_Staff = [3,7,5,'Necromancer Staff']

# Easy Settings
player_max_hp = 50
player_hp = 10
player_starter_attack = 5
player_starter_defence = 0
enemy = []
enemy_hp = 0
enemy_attack = 0
boss = False
choice = 0
statis_defence = 0
# Loot Pools
Melee_Items = copies(Rusty_Sword, 5) + copies(Rusty_Helmet, 2) + [OldBandage]
Ranged_Items = copies(Old_Bow, 5) + copies(Rusty_Helmet, 2) + [OldBandage]
Boss_Items = [Necromancer_Staff]
Hand_Items = [Rusty_Sword,Old_Bow,Necromancer_Staff]
Armor_Items = [Rusty_Helmet,Good_Helmet]
Heal_Items = copies(Bandage,2) + [OldBandage]
Trinket_Items = [Ameulet]

# Enemy Stats
Zombie = [10,5,0,Melee_Items*5 + Heal_Items,'Zombie']
Skeleton = [10,5,0,Ranged_Items*5 + Heal_Items,'Skeleton']
A_Zombie = [10,3,2,Melee_Items*3 + Armor_Items*2 + Heal_Items, 'Aromored Zombie']
E_Skeleton = [10,3,2,Ranged_Items*3 + Trinket_Items*2 + Heal_Items, 'Enchanted Skeleton']
Necromancer = [10,7,3,Boss_Items,'Necromancer']
Basic_Pool = copies(Zombie,4) + copies(Skeleton,4) + [A_Zombie] + [E_Skeleton]
Advanced_Pool = copies(Zombie,1) + copies(Skeleton,1) + copies(A_Zombie,3) + copies(E_Skeleton,3)
current_pool = Basic_Pool

# Player Stats
player = [player_hp, player_starter_attack, player_starter_defence]
helmet = empty_slot()
trinket = empty_slot()
hand = empty_slot()
potions = [Bandage[:], empty_slot(), empty_slot()]

# -------------------------
# STAT CHECK
# -------------------------
def stat_check():

    global player, helmet, trinket, hand, potions
    global player_max_hp, player_hp
    global player_starter_attack, player_starter_defence

    print()
    sleep(0.3)

    player_max_hp = 50 + helmet[0] + trinket[0] + hand[0]
    player[1] = player_starter_attack + helmet[1] + trinket[1] + hand[1]
    player[2] = player_starter_defence + helmet[2] + trinket[2] + hand[2]

    print('Check stats (y/n)?')
    sleep(0.3)
    statinp = input()

    if statinp == 'y':
        print()
        print('Opening stats menu...')
        sleep(0.4)

        print()
        print('Items or Player (i/p)?')
        sleep(0.3)
        statinp = input()

        if statinp == 'i':
            print()
            print('Loading item categories...')
            sleep(0.4)

            print()
            print('1. Helmet')
            print('2. Hand')
            print('3. Trinket')
            print('4. Potions')
            sleep(0.3)

            statinp = input()

            if statinp == '1':
                print()
                print('Showing Helmet stats...')
                sleep(0.4)
                print(f'1. HPBuff: {helmet[0]}')
                print(f'2. AttackBuff: {helmet[1]}')
                print(f'3. DefenceBuff: {helmet[2]}')

            elif statinp == '2':
                print()
                print('Showing Hand stats...')
                sleep(0.4)
                print(f'1. HPBuff: {hand[0]}')
                print(f'2. AttackBuff: {hand[1]}')
                print(f'3. DefenceBuff: {hand[2]}')

            elif statinp == '3':
                print()
                print('Showing Trinket stats...')
                sleep(0.4)
                print(f'1. HPBuff: {trinket[0]}')
                print(f'2. AttackBuff: {trinket[1]}')
                print(f'3. DefenceBuff: {trinket[2]}')

            elif statinp == '4':
                print()
                print('Listing Heals...')
                sleep(0.4)
                for i in range(len(potions)):
                    if potions[i][3] != '':
                        print(f'{i+1}. {potions[i][3]}, It gives you {potions[i][0]} HP')
                        sleep(0.2)

            else:
                print()
                print('Invalid choice')
                sleep(0.3)

        elif statinp == 'p':
            print()
            print('Showing player stats...')
            sleep(0.4)
            print(f'1. Player HP: {player[0]}')
            print(f'2. Player Attack: {player[1]}')
            print(f'3. Player Defence: {player[2]}')

    print()
    sleep(0.4)
    potions_use()


# -------------------------
# POTION USE
# -------------------------
def potions_use():
    global player, potions, player_max_hp

    print()
    sleep(0.3)

    if player[0] < player_max_hp:
        if potions[0][3] != '' or potions[1][3] != '' or potions[2][3] != '':
            print(f'You have {player[0]}HP.')
            sleep(0.5)
            print('Use heal(y/n)?')
            if input() == 'y':
                print()
                sleep(0.3)
                print('Choose Heal')
                for i in range(len(potions)):
                    if potions[i][3] != '':
                        print(f'{i+1}.{potions[i][3]}, It gives you {potions[i][0]}HP')
                print()
                potchoice = int(input())
                if potchoice in (1,2,3):
                    if potions[potchoice-1][3] != '':
                        player[0] += potions[potchoice-1][0]
                        if player[0] > player_max_hp:
                            player[0] = player_max_hp
                        print()
                        print(f'You used {potions[potchoice-1][3]} and now have {player[0]}HP.')
                        sleep(0.5)
                        potions[potchoice-1] = empty_slot()
                else:
                    print('Invalid choice, you do not use a heal')
                    sleep(0.5)

    get_enemy()

# -------------------------
# ENEMY GENERATION
# -------------------------
def get_enemy():
    global enemy, enemy_hp, enemy_attack, boss, current_pool, buff

    print()
    sleep(0.5)

    enemy = Basic_Pool[r.randint(0, len(Basic_Pool)-1)]
    enemy_hp = int(enemy[0]) + buff * 1.5
    enemy_attack = enemy[1] + buff    

    if buff == 10:
        enemy_hp *= 2
        enemy_attack *= 2
        boss = True
        print(f'You encounter a {enemy[4]} Boss guarding the entrance to the secound floor.')
        current_pool = Advanced_Pool

    else:
        boss = False
        print(f'You encounter a {enemy[4]} with {enemy_hp} HP.')

    print()
    sleep(0.5)

    player_options()

# -------------------------
# PLAYER OPTIONS
# -------------------------
def player_options():
    global choice

    print()
    sleep(0.3)
    print('1.Attack')
    print('2.Defend')
    print('3.Run')
    print()

    choice = int(input('Choose: '))

    if choice == 1:
        choice1()
    elif choice == 2:
        choice2()
    elif choice == 3:
        choice3()
    else:
        print()
        print('Not A Correct Input')
        sleep(0.5)
        player_options()

# -------------------------
# ATTACK
# -------------------------
def choice1():
    global enemy_hp

    print()
    sleep(0.3)

    damage = player[1] - enemy[2]
    if damage < 0:
        damage = 0
    enemy_hp -= damage

    print(f'You dealt {damage} damage to the enemy!')
    if enemy_hp <= 0:
        if enemy_hp < 0:
            enemy_hp = 0
    sleep(0.5)
    print(f'Enemy HP: {enemy_hp}')
    print()

    sleep(0.5)

    if not check_enemy_alive():
        loot()
    else:
        enemy_attack_()

# -------------------------
# DEFEND
# -------------------------
def choice2():
    global statis_defence

    print()
    sleep(0.3)

    player[2] += 5
    print(f'You brace yourself! +5 Defence (Total: {player[2]})')
    sleep(0.5)

    statis_defence = -5
    return enemy_attack_()

# -------------------------
# RUN
# -------------------------
def choice3():
    global helmet, trinket, hand, potions

    print()
    sleep(0.3)
    print("You run away!")
    sleep(0.5)
    print()

    inventory = []

    if helmet[3] != '':
        inventory.append(("helmet", None))
    if trinket[3] != '':
        inventory.append(("trinket", None))
    if hand[3] != '':
        inventory.append(("hand", None))

    for i in range(3):
        if potions[i][3] != '':
            inventory.append(("potion", i))

    if not inventory:
        print("You manage to escape without dropping anything.")
        sleep(0.5)
        statis_defence_check()
        return

    slot, index = random.choice(inventory)

    if slot == "helmet":
        print(f"You drop your {helmet[3]} while running!")
        helmet = empty_slot()
    elif slot == "trinket":
        print(f"You drop your {trinket[3]} while running!")
        trinket = empty_slot()
    elif slot == "hand":
        print(f"You drop your {hand[3]} while running!")
        hand = empty_slot()
    else:
        print(f"You drop your {potions[index][3]} while running!")
        potions[index] = empty_slot()

    sleep(0.5)
    statis_defence_check()

# -------------------------
# ENEMY ALIVE CHECK
# -------------------------
def check_enemy_alive():
    global enemy_hp
    if enemy_hp <= 0:
        if enemy_hp < 0:
            enemy_hp = 0
        return False
    return True

# -------------------------
# ENEMY ATTACK
# -------------------------
def enemy_attack_():
    global player

    print()
    sleep(0.4)

    dmg = enemy_attack - player[2]
    if dmg < 0:
        dmg = 0

    player[0] -= dmg
    print(f'The enemy attacks you for {dmg} damage!')
    sleep(0.5)
    print(f'Your HP: {player[0]}')
    print()

    sleep(0.5)

    if not check_player_alive():
        print('You died!')
        sleep(2)
        exit()
    else:
        player_options()

# -------------------------
# PLAYER ALIVE CHECK
# -------------------------
def check_player_alive():
    if player[0] <= 0:
        if player[0] < 0:
            player[0] = 0
        return False
    return True

# -------------------------
# LOOT SYSTEM
# -------------------------
def loot():
    global helmet, trinket, hand, potions, enemy

    print()
    sleep(0.4)
    print("The enemy collapses...")
    sleep(0.7)

    chosen_item = r.choice(enemy[3])
    print(f'You found a {chosen_item[3]}!')
    print()
    sleep(0.5)

    # Hand items
    if chosen_item in Hand_Items:
        if hand[3] != '':
            print(f'Replace {hand[3]} (y/n)?')
            if input() == 'y':
                hand = chosen_item[:]
                print(f'You equip the {hand[3]}')
        else:
            hand = chosen_item[:]
            print(f'You equip the {hand[3]}')

    # Armor
    elif chosen_item in Armor_Items:
        if helmet[3] != '':
            print(f'Replace {helmet[3]} (y/n)?')
            if input() == 'y':
                helmet = chosen_item[:]
                print(f'You equip the {helmet[3]}')
        else:
            helmet = chosen_item[:]
            print(f'You equip the {helmet[3]}')

    # Healing items
    elif chosen_item in Heal_Items:
        for i in range(len(potions)):
            if potions[i][3] == '':
                potions[i] = chosen_item[:]
                print(f'You put the {chosen_item[3]} in your inventory')
                break
        else:
            print('Your inventory is full!')
            print('Remove a potion (y/n)?')
            if input() == 'y':
                print('Choose a potion to remove:')
                for i in range(len(potions)):
                    if potions[i][3] != '':
                        print(f'{i+1}. {potions[i][3]}')
                removechoice = int(input())
                if removechoice in (1,2,3) and potions[removechoice-1][3] != '':
                    print(f'You removed {potions[removechoice-1][3]}')
                    potions[removechoice-1] = chosen_item[:]
                    print(f'You put the {chosen_item[3]} in your inventory')
                else:
                    print('Invalid choice, you leave the item')
            else:
                print('You leave the item')

    # Trinkets
    elif chosen_item in Trinket_Items:
        if trinket[3] != '':
            print(f'Replace {trinket[3]} (y/n)?')
            if input() == 'y':
                trinket = chosen_item[:]
                print(f'You equip the {trinket[3]}')
        else:
            trinket = chosen_item[:]
            print(f'You equip the {trinket[3]}')

    sleep(0.5)
    statis_defence_check()
    get_enemy()

# -------------------------
# DEFENCE RESET
# -------------------------
def statis_defence_check():
    global statis_defence
    global buff
    if statis_defence == -5:
        player[2] -= 5
        statis_defence = 0
    buff += 1
    if buff == 11:
        print('You enter the lower dungeon')
    stat_check()

# -------------------------
# MAIN GAME LOOP
# -------------------------
while True:
    print()
    print('You enter the dungeon...')
    print()
    sleep(1)
    get_enemy()