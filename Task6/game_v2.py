"My own game module"

from typing import List

class Item:
    "Item class"

    def __init__(self, name: str, description: str) -> None:
        self.name = name
        self.description = description

    def describe(self) -> None:
        "Describes"
        print(f"{self.name.title()} is here - {self.description}")

    def get_name(self) -> str:
        "Gets name of item"
        return self.name

class Weapon(Item):
    "Weapon class"

    def __init__(self, name: str, description: str, damage: int) -> None:
        "Does initialization"
        self.damage = damage
        super().__init__(name, description)

    def get_damage(self) -> int:
        "returns damage"
        return self.damage

class Player:
    "Main character class"

    def __init__(self, health: int, current_weapon: Weapon, backpack: List[Item],
                 equipment: List[Weapon]) -> None:
        "Does initialization"
        self.max_hp = health
        self.health = health
        self.current_weapon = current_weapon
        self.backpack = backpack
        self.equipment = equipment

    def drop_hp(self, damage: int) -> int:
        "Drops hp"
        self.health -= damage
        if self.health < 0:
            self.health = 0
        return self.health

    def get_weapon(self) -> Weapon:
        "Gets weapon"
        return self.current_weapon

    def add_to_backpack(self, item: Item) -> None:
        "Adds item to backpack"
        self.backpack.append(item)
        print(f"\nYou have put {item.name.title()} to your backpack")

    def del_from_backpack(self, item: Item) -> None:
        "Removes item from backpack"
        self.backpack.remove(item)

    def add_weapon(self, weapon: Weapon) -> None:
        "Adds weapon"
        self.equipment.append(weapon)
        print(f"\nYou recived new weapon - {weapon.name.title()}!")
        print(f"Damage - {weapon.damage}")

    def view_weapons(self) -> str:
        "Views weapons"
        info_str = "List of your weapons:\n"
        for weapon in self.equipment:
            info_str += f"{weapon.name.title()} - {weapon.description}. Damage: {weapon.damage}\n"
        return info_str.rstrip()

    def view_items(self) -> str:
        "Views all items"
        if len(self.backpack) == 0:
            return "You have no items"
        info_str = "List of your items:\n"
        for item in self.backpack:
            info_str += f"{item.name.title()} - {item.description}\n"
        return info_str.rstrip()

    def recover(self) -> None:
        "Recovers player"
        self.health = self.max_hp

    def attack(self) -> int:
        "Returns damage player is dealing"
        return self.current_weapon.damage

    def get_backpack(self) -> List[Item]:
        "Gets player backpack"
        return self.backpack

    def get_weapons(self) -> List[Weapon]:
        'Gets list of weapon'
        return self.equipment

    def set_weapon(self, new_weapon: Weapon) -> None:
        "Sets weapon"
        self.current_weapon = new_weapon
        print(f"\nWeapon changed to {new_weapon.name.title()}")

class Character:
    "Character class"

    def __init__(self, name: str, description: str, conversation: str) -> None:
        "Does initialization"
        self.name = name
        self.description = description
        self.conversation = conversation

    def talk(self) -> str:
        "Talks"
        return f"{self.name} says: {self.conversation}"

    def describe(self) -> None:
        "Describes"
        print(f"""{self.name} is here!
{self.description}""")

    def get_name(self) -> str:
        "Gets name"
        return self.name

class Enemy(Character):
    "Enemy class"

    def __init__(self, name: str, description: str, conversation: str, health: int, damage: int,
        hold_item: Item = None) -> None:
        "Does initialization"
        self.health = health
        self.damage = damage
        self.hold_item = hold_item
        super().__init__(name, description, conversation)

    def deal_damage(self) -> int:
        "Returns damage from enemy"
        return self.damage

    def loose_hp(self, damage: int) -> None:
        "Reduces HP of enemy"
        self.health -= damage
        if self.health < 0:
            self.health = 0
        return self.health

    def get_item(self) -> Item:
        "Returns holding item"
        return self.hold_item

    def get_hp(self) -> int:
        "Gets hp of character"
        return self.health

class Friend(Character):
    "Friend class"

    def __init__(self, name: str, description: str, conversation: str,
                 wanted_item: str, advice: str, reward: Item) -> None:
        "Does initialization"
        self.wanted_item = wanted_item
        self.advice = advice
        self.reward = reward
        super().__init__(name, description, conversation)

    def compare_item(self, item: Item) -> bool:
        "Compares if it's needed item"
        return item.name == self.wanted_item

    def happier(self) -> None:
        "Sets happy status and changes conversation for new"
        self.conversation = self.advice
        self.wanted_item = None

    def get_item(self) -> Item:
        "Gets holding item"
        return self.reward

    def get_wanted(self) -> Item:
        "Gets wanted item"
        return self.wanted_item

class Location:
    "Location class"

    def __init__(self, name: str, description: str,
        character: Character = None, item: Item = None, available: bool = True,
        key: Item = None, access_message: str = None) -> None:
        "Does initialization"
        self.name = name
        self.description = description
        self.linked_locs = {}
        self.character = character
        self.item = item
        self.available = available
        self.key = key
        self.access_message = access_message

    def get_details(self) -> str:
        "Gets details"
        info_str = ''
        for room in list(self.linked_locs.items()):
            info_str += f"The {room[0].name} is {room[1]} - {room[0].description}\n"
        print(f"""{self.name}
--------------------
{self.description}\n
{info_str}""")

    def get_character(self) -> Character:
        'Gets character'
        return self.character

    def get_item(self) -> Item:
        "Gets item"
        return self.item

    def move(self, direction: str) -> object:
        "Moves"
        for room in (self.linked_locs.items()):
            if room[1] == direction:
                return room[0]
        return self

    def link_room(self, room: object, direction: str) -> None:
        'Links room'
        self.linked_locs.update({room: direction})

    def get_access_message(self) -> str:
        "Gets message"
        return self.access_message

    def get_aviability(self) -> bool:
        "Gets aviability"
        return self.available

    def get_key(self) -> Item:
        "Gets key to location"
        return self.key

    def set_aviability(self, status: bool) -> None:
        "Sets aviability"
        self.available = status

    def set_item(self, item: Item) -> None:
        "Sets item"
        self.item = item

    def set_character(self, character: Character) -> None:
        "Sets new character"
        self.character = character
