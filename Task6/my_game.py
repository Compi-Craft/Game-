"My version of game"

import sys
import game_v2

blinkroot = game_v2.Item('blinkroot', "Dark plant which blinks in the dark")
spell_book = game_v2.Item('spell book', 'Mysterious book once stolen in wizard')
talisman = game_v2.Item('holy talisman', 'Magic talisman given by witch')
axe = game_v2.Item('axe', 'Axe lost by lumberjack')
gold_sack = game_v2.Item('money sack', 'Sack with golden coins, probably lost by someone')
treasury_key = game_v2.Item("golden key", "Key to Dragon's treasure, where he stores stolen wealth")
lantern = game_v2.Item("lantern", 'Lantern which can light up dark places')
sheep = game_v2.Item("sheep", "Sheep, probably lost by villagers")

dagger = game_v2.Weapon('dagger', 'Simple, cheap weapon', 20)
battle_club = game_v2.Weapon('heavy club', 'Heavy club made by lumberjack from dark oak wood', 40)
footman_sword = game_v2.Weapon('footman sword', 'Sword, used by royal knights', 80)
dragon_slayer = game_v2.Weapon('dragon slayer',
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
which I left in the forest", "axe", "This club is made of dark oak. \
It is believed to be efficient against dark magic!", battle_club)
wizard = game_v2.Friend("Castle Wizard", "Royal wizard, which used to help king himself!",
"Welcome traveller. I heard legends about you. You need to know, that \
our kingdom sank into darkness after Diablo stolen our wealth and king. \
I want to trust you with a sword known as 'Dragon Slayer', but I need my \
spell book to unleash it's full power. It was stollen by evil troll. \
Bring it to me, and you will recive the most \
powerful sword in the world!", "spell book", "'Dragon slayer is yours \
but Diablo is very powerfull. You will need to collect all possible resourses to \
defeat him, remember that! Good luck!", dragon_slayer)
witch = game_v2.Friend("Swamp Witch", "Lonely witch living in the hut on the edge of swamp",
"Hello traveller! Ralely someones is able to get here. Well as you are here, \
i would be very glad if you bring me blinkroot. It is herb, which can \
be founded in forest. You will recive magical reward for this, don't worry!",
"blinkroot", "This magical talisman will save you from dark swamp energy. Have a nice way!",
talisman)
merchant = game_v2.Friend("Merchant", "Regular merchant, came from other kingdom to trade",
"Oh God! As soon as I got to the market I realized I lost my money!\n \
Did I lose them in the swamps? If only someone would return them to me, I'd be very grateful...",
'money sack', 'Thank God! Here you are \
as I promised. \nSword from heart of our kingdom, carried by knights themself!',
footman_sword)
villager = game_v2.Friend("Villager", "Regular villager living in the kingdom",
"Hello traveller! After Diablo invaded us, dark accidents started \
to happen. Even today my sheep got lost in the field. I wish I could see \
it again", "sheep", "Thank you much! I'm not rich, so lantern is \
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
key = lantern, access_message="It's too dark here!")
village = game_v2.Location("Village", "Quiet peaceful village", character=villager)
castle = game_v2.Location("Royale Castle", "Main castle of kingdom", wizard)
market = game_v2.Location("Market", "Place where people share goods", merchant)
dark_swamps = game_v2.Location("Dark Swamp", "Swamp, swallowed by dark pulsing energy",
swamp_monster, available=False, key=talisman,
access_message="Dark energy don't let you in!")
treasure = game_v2.Location("Treasure", "Treasure with all stolen kingdom wealth and king family",
available=False, key=treasury_key, access_message="There is huge golden lock hanging")
dragon_mountain = game_v2.Location("Diablo Mountain", "Homee of Diablo - legendary dragon",
dragon)

crossroad.link_room(castle, "north")
crossroad.link_room(forest, "south")
crossroad.link_room(dark_swamps, "west")
crossroad.link_room(village, "east")

forest.link_room(crossroad, "north")
forest.link_room(dark_thickets, "south")
forest.link_room(witch_hut, "west")
forest.link_room(field, "east")

dark_thickets.link_room(forest, "north")
dark_thickets.link_room(cave, "west")
dark_thickets.link_room(forest_house, "east")

forest_house.link_room(field, "north")
forest_house.link_room(dark_thickets, "west")

field.link_room(village, "north")
field.link_room(forest_house, "south")
field.link_room(forest, "west")

witch_hut.link_room(dark_swamps, "north")
witch_hut.link_room(cave, "south")
witch_hut.link_room(forest, "east")

cave.link_room(witch_hut, "north")
cave.link_room(dark_thickets, "east")

village.link_room(market, "north")
village.link_room(field, "south")
village.link_room(crossroad, "west")

castle.link_room(crossroad, "south")
castle.link_room(market, "east")

market.link_room(village, "south")
market.link_room(castle, "west")

dark_swamps.link_room(treasure, "north")
dark_swamps.link_room(witch_hut, "south")
dark_swamps.link_room(dragon_mountain, "west")
dark_swamps.link_room(crossroad, "east")

treasure.link_room(dark_swamps, "south")

dragon_mountain.link_room(dark_swamps, "east")

player = game_v2.Player(100, dagger, [], [dagger])

DEAD = False
current_loc = crossroad

while not DEAD:
    print()
    if current_loc == treasure:
        print("\nYou unlocked treasure and free king family\n")
        print("You won!")
        print("\nGame Over!\n")
        break
    current_loc.get_details()
    inhabitant = current_loc.get_character()
    if inhabitant is not None:
        print()
        inhabitant.describe()
        if isinstance(inhabitant, game_v2.Enemy):
            print(f"HP - {inhabitant.get_hp()}")
            print(f"Damage - {inhabitant.deal_damage()}")
        print()
    item = current_loc.get_item()
    if item is not None:
        print()
        item.describe()
        print()

    choice = input(">>> ", ).lower()

    if choice in ('north', 'south', 'west', 'east'):
        new_loc = current_loc.move(choice)
        if not new_loc.get_aviability():
            FLAG = False
            print()
            print(new_loc.get_access_message())
            print("\nUse item to unlock location")
            print(player.view_items())
            choice = input(">>> ", ).lower()
            for item in player.get_backpack():
                if item.get_name() == choice and item == new_loc.get_key():
                    FLAG = True
                    print("Location unlocked!")
                    new_loc.set_aviability(True)
                    current_loc = new_loc
                    player.del_from_backpack(item)
                    break
            if not FLAG:
                print(f"\nSeems {choice} did'nt help!")
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
            current_loc.set_item(None)
        else:
            print("\nNothing to take")
    elif choice == "items":
        print(player.view_items())
    elif choice == "chweapon":
        FLAG = False
        print("\nChoose weapon to equip")
        print(player.view_weapons())
        choice = input(">>> ", ).lower()
        for weapon in player.get_weapons():
            if choice == weapon.get_name():
                FLAG = True
                player.set_weapon(weapon)
                break
        if not FLAG:
            print(f"\nNo such weapon '{choice.title()}'!")
    elif choice == "give":
        if inhabitant is None or not isinstance(inhabitant, game_v2.Friend) or \
        inhabitant.wanted_item is None:
            print("\nNobody here to give something")
        else:
            FLAG = False
            print("\nChoose what to give")
            print(player.view_items())
            choice = input(">>> ", ).lower()
            if inhabitant.get_wanted() == choice:
                for item in player.get_backpack():
                    if item.get_name() == choice:
                        FLAG = True
                        inhabitant.happier()
                        print(inhabitant.talk())
                        new_item = inhabitant.get_item()
                        if isinstance(new_item, game_v2.Weapon):
                            player.add_weapon(new_item)
                        else:
                            player.add_to_backpack(new_item)
                        player.del_from_backpack(item)
                        break
                if not FLAG:
                    print("\nYou don't have this item")
            else:
                print(f"{inhabitant.get_name()} says: I don't need {choice.title()}!")
    elif choice == "fight":
        if not isinstance(inhabitant, game_v2.Enemy):
            print("\nNobody to fight with!")
        else:
            while True:
                print(f"\nYour current HP - {player.drop_hp(0)}")
                print(f"Enemy current HP - {inhabitant.get_hp()}")
                print("\nEnter to continue")
                choice = input(">>> ", )
                print("\nEnemy attacks")
                player.drop_hp(inhabitant.deal_damage())
                if player.drop_hp(0) == 0:
                    print("\nYou died!\n")
                    print("Game Over!")
                    DEAD = True
                    break
                print("You attack!")
                inhabitant.loose_hp(player.get_weapon().get_damage())
                if inhabitant.get_hp() == 0:
                    print("\nYou won!")
                    current_loc.set_character(None)
                    print(f"\n{inhabitant.get_name()} dropped item: \
{inhabitant.get_item().get_name().title()}")
                    player.add_to_backpack(inhabitant.get_item())
                    player.recover()
                    break
    elif choice == "exit":
        sys.exit("\nYou have exited the game\n")
    else:
        print(f"\nI don't know how to {choice}")
