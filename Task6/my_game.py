"My version of game"

import sys
import game_v2

blinkroot = game_v2.Item('Blinkroot', "Dark plant which blinks in the dark")
spell_book = game_v2.Item('Spell Book', 'Mysterious book once stolen in wizard')
talisman = game_v2.Item('Holy Talisman', 'Magic talisman given by witch')
axe = game_v2.Item('Axe', 'Axe lost by lumberjack')
gold_sack = game_v2.Item('Money Sack', 'Sack with golden coins, probably lost by someone')
treasury_key = game_v2.Item("Golden Key", "Key to Dragon's treasure, where he stores stolen wealth")
lantern = game_v2.Item("Lantern", 'Lantern which can light up dark places')
sheep = game_v2.Item("Sheep", "Sheep, probably lost by villagers")

dagger = game_v2.Weapon('Dagger', 'Simple, cheap weapon', 20)
battle_club = game_v2.Weapon('Heavy Club', 'Heavy club made by lumberjack from dark oak wood', 40)
footman_sword = game_v2.Weapon('Footman Sword', 'Sword, used by royal knights', 80)
dragon_slayer = game_v2.Weapon('Dragon Slayer',
'Sword known for special ability of killing dragons', 150)

goblin = game_v2.Enemy("Goblin", "Goblin, who got lost in the forest",
"Wow, lost traveler! Or, should i call you 'a dinner'?", 50, 20, axe)
swamp_monster = game_v2.Enemy("Swamp Monter", "Revived piece of dirt powered by dark magic",
"Burb-burb-burb!", 80, 30, gold_sack)
troll = game_v2.Enemy("Giant Troll", "Stinky cave monster, which terrorizes kingdom",
"HOW DARE YOU ENETER MY HOME WITHOUT PERMISSION???!", 100, 40, spell_book)
dragon = game_v2.Enemy("Diablo", "Ancient dragon unbeatable by legends",
"Do you really think you can cope with me! I will destroy you, \
pathetic human", 500, 20, treasury_key)

lumberjack = game_v2.Friend("Lumberjack", "Reclusive man living in the forest house",
"Hello, traveller. If you want to get better weapon, you need to find my axe, \
which I left in the forest", "Axe", "This club is made of dark oak. \
It is believed to be efficient against dark magic!", battle_club)
wizard = game_v2.Friend("Castle Wizard", "Royal wizard, which used to help king himself!",
"Welcome traveller. I heard legends about you. You need to know, that \
our kingdom sank into darkness after Diablo stolen our wealth and king. \
I want to trust you with a sword known as 'Dragon Slayer', but I need my \
spell book to unleash it's full power. It was stollen by evil troll. \
Bring it to me, and you will recive the most \
powerful sword in the world!", "Spell Book", "'Dragon slayer is yours \
but Diablo is very powerfull. You will need to collect all possible resourses to \
defeat him, remember that! Good luck!", dragon_slayer)
witch = game_v2.Friend("Swamp Witch", "Lonely witch living in the hut on the edge of swamp",
"Hello traveller! Ralely someones is able to get here. Well as you are here, \
i would be very glad if you bring me blinkroot. It is herb, which can \
be founded in forest. You will recive magical reward for this, don't worry!",
"Blinkroot", "This magical talisman will save you from dark swamp energy. Have a nice way!",
talisman)
merchant = game_v2.Friend("Merchant", "Regular merchant, came from other kingdom to trade",
"Oh God! As soon as I got to the market I realized I lost my money!\n \
Did I lose them in the swamps? If only someone would return them to me, I'd be very grateful...",
'Money Sack', 'Thank God! Here you are \
as I promised. \nSword from heart of our kingdom, carried by knights themself!',
footman_sword)
villager = game_v2.Friend("Villager", "Regular villager living in the kingdom",
"Hello traveller! After Diablo invaded us, dark accidents started \
to happen. Even today my sheep got lost in the field. I wish I could see \
it again", "Sheep", "Thank you much! I'm not rich, so lantern is \
the only I can give to you", lantern)

crossroad = game_v2.Location("Crossroad", "The place where the paths cross")
forest = game_v2.Location("Forest", "Dark forest on the sounth of kingdom", goblin)
dark_thickets = game_v2.Location("Dark Thickets", "Super dark place, \
where sun can barely hit ground", item = blinkroot)
forest_house = game_v2.Location("Forest House", "Mysterious wooden house \
in the middle of forest", lumberjack)
field = game_v2.Location("Field", "Field planted with crops", item = sheep)
witch_hut = game_v2.Location("Witch Hut", "Lonely hut on the edge of swamp", witch)
cave = game_v2.Location("Dark Cave", "Very dark cave with stinky smell", troll, available=False,
key = lantern, accsess_message="It's too dark here!")
village = game_v2.Location("Village", "Quiet peaceful village", character=villager)
castle = game_v2.Location("Royale Castle", "Main castle of kingdom", wizard)
market = game_v2.Location("Market", "Place where people share goods", merchant)
dark_swamps = game_v2.Location("Dark Swamp", "Swamp, swallowed by dark pulsing energy",
swamp_monster, available=False, key=talisman,
accsess_message="Dark energy don't let you in!")
treasure = game_v2.Location("Treasure", "Treasure with all stolen kingdom wealth and king family",
available=False, key=treasury_key, accsess_message="There is huge golden lock hanging")
dragon_mountain = game_v2.Location("Diablo Mountain", "Homee of Diablo - legendary dragon",
dragon)

crossroad.link_room(castle, "North")
crossroad.link_room(forest, "South")
crossroad.link_room(dark_swamps, "West")
crossroad.link_room(village, "East")

forest.link_room(crossroad, "North")
forest.link_room(dark_thickets, "South")
forest.link_room(witch_hut, "West")
forest.link_room(field, "East")

dark_thickets.link_room(forest, "North")
dark_thickets.link_room(cave, "West")
dark_thickets.link_room(forest_house, "East")

forest_house.link_room(field, "North")
forest_house.link_room(dark_thickets, "West")

field.link_room(village, "North")
field.link_room(forest_house, "South")
field.link_room(forest, "West")

witch_hut.link_room(dark_swamps, "North")
witch_hut.link_room(cave, "South")
witch_hut.link_room(forest, "East")

cave.link_room(witch_hut, "North")
cave.link_room(dark_thickets, "East")

village.link_room(market, "North")
village.link_room(field, "South")
village.link_room(crossroad, "West")

castle.link_room(crossroad, "South")
castle.link_room(market, "East")

market.link_room(village, "South")
market.link_room(castle, "West")

dark_swamps.link_room(treasure, "North")
dark_swamps.link_room(witch_hut, "South")
dark_swamps.link_room(dragon_mountain, "West")
dark_swamps.link_room(crossroad, "East")

treasure.link_room(dark_swamps, "South")

dragon_mountain.link_room(dark_swamps, "East")

player = game_v2.Player(100, dagger, [], [dagger])

dead = False
current_loc = crossroad

while not dead:
    print()
    if current_loc == treasure:
        print("\nYou unlocked treasure and free king family\n")
        print("You won!")
        print("\nGame Over!\n")
    current_loc.get_details()
    inhabitant = current_loc.get_character()
    if inhabitant is not None:
        print()
        inhabitant.describe()
        if isinstance(inhabitant, game_v2.Enemy):
            print(f"HP - {inhabitant.health}")
        print()
    item = current_loc.get_item()
    if item is not None:
        print()
        item.describe()
        print()

    choice = input(">>> ", )
    choice = choice.lower()
    if choice in ('north', 'south', 'west', 'east'):
        new_loc = current_loc.move(choice.title())
        if not new_loc.get_aviability():
            flag = False
            print()
            print(new_loc.get_accsess_message())
            print("\nUse item to unlock location")
            print(player.view_items())
            choice = input(">>> ", ).title()
            for item in player.backpack:
                if item.name == choice and item == new_loc.key:
                    flag = True
                    print("Location unlocked!")
                    new_loc.available = True
                    current_loc = new_loc
                    player.del_from_backpack(item)
                    break
            if not flag:
                print(f"\nSeems {choice} did'n help!")
        else:
            current_loc = new_loc
    elif choice == "talk":
        if inhabitant is not None:
            print(inhabitant.talk())
        else:
            print("\nNo one to talk to")
    elif choice == "take":
        if item is not None:
            player.add_to_backpack(item)
            current_loc.item = None
        else:
            print("\nNothing to take")
    elif choice == "items":
        print(player.view_items())
    elif choice == "chweapon":
        flag = False
        print("\nChoose weapon to equip")
        print(player.view_weapons())
        choice = input(">>> ", ).title()
        for weapon in player.equipment:
            if choice == weapon.name:
                flag = True
                player.current_weapon = weapon
                print(f"\nWeapon changed to {weapon.name}")
                break
        if not flag:
            print(f"\nNo such weapon '{choice}'!")
    elif choice == "give":
        if inhabitant is None or not isinstance(inhabitant, game_v2.Friend) or \
        inhabitant.wanted_item is None:
            print("\nNobody here to give something")
        else:
            flag = False
            print("\nChoose what to give")
            print(player.view_items())
            choice = input(">>> ", ).title()
            if inhabitant.wanted_item == choice:
                for item in player.backpack:
                    if item.name == choice:
                        flag = True
                        inhabitant.wanted_item = None
                        inhabitant.happier()
                        print(inhabitant.talk())
                        new_item = inhabitant.get_item()
                        if isinstance(new_item, game_v2.Weapon):
                            player.add_weapon(new_item)
                        else:
                            player.add_to_backpack(new_item)
                        player.del_from_backpack(item)
                        break
                if not flag:
                    print("\nYou don't have this item")
            else:
                print(f"{inhabitant.name} says: I don't need {choice}!")
    elif choice == "fight":
        if not isinstance(inhabitant, game_v2.Enemy):
            print("\nNobody to fight with!")
        else:
            while True:
                print(f"\nYour current HP - {player.health}")
                print(f"Enemy current HP - {inhabitant.health}")
                print("\nEnter to continue")
                choice = input(">>> ", )
                print("\nEnemy attacks")
                player.drop_hp(inhabitant.deal_damage())
                if player.health == 0:
                    print("\nYou died!\n")
                    print("Game Over!")
                    dead = True
                    break
                print("You attack!")
                inhabitant.loose_hp(player.get_weapon().get_damage())
                if inhabitant.health == 0:
                    print("\nYou won!")
                    current_loc.character = None
                    print(f"\n{inhabitant.name} dropped item: {inhabitant.get_item().name}")
                    player.add_to_backpack(inhabitant.get_item())
                    player.recover()
                    break
    elif choice == "exit":
        sys.exit("\nYou have exited the game\n")
    else:
        print(f"\nI don't know how to {choice}")
