"Game module"

class Room:
    "Main game module"

    def __init__(self, name: str) -> None:
        "Does initialization"
        self.name = name
        self.description = ''
        self.linked_rooms = {}
        self.character = None
        self.item = None

    def set_description(self, description: str):
        "Sets description"
        self.description = description

    def link_room(self, room: object, direction: str) -> None:
        'Links room'
        self.linked_rooms.update({room: direction})

    def set_character(self, character) -> None:
        "Sets character"
        self.character = character

    def set_item(self, item) -> None:
        "Sets item"
        self.item = item

    def get_details(self) -> str:
        "Gets details"
        info_str = ''
        for room in list(self.linked_rooms.items()):
            info_str += f"The {room[0].name} is {room[1]}\n"
        print(f"""{self.name}
--------------------
{self.description}
{info_str.rstrip()}""")

    def get_character(self) -> object:
        'Gets character'
        return self.character

    def get_item(self) -> object:
        "Gets item"
        return self.item

    def move(self, direction: str) -> object:
        "Moves"
        for room in (self.linked_rooms.items()):
            if room[1] == direction:
                return room[0]
        return self

class Enemy:
    "Enemy class"
    defeted = 0
    def __init__(self, name: str, descritprion: str) -> None:
        "Does initialization"
        self.name = name
        self.description = descritprion
        self.conversation = ''
        self.weakness = ''

    def set_conversation(self, conversation):
        "Sets conversation"
        self.conversation = conversation

    def set_weakness(self, weakness: str) -> None:
        'Sets weakness'
        self.weakness = weakness

    def fight(self, fight_with: str) -> bool:
        "Fights"
        return self.weakness == fight_with

    def talk(self) -> None:
        "Talks"
        print(f"[{self.name} says]: {self.conversation}")

    def describe(self) -> None:
        "Describes"
        print(f"""{self.name} is here!
{self.description}""")

    def get_defeated(self) -> int:
        "Defeats"
        Enemy.defeted += 1
        return Enemy.defeted

class Item:
    "Item class"

    def __init__(self, name: str) -> None:
        'Does initialization'
        self.name = name
        self.description = ''

    def set_description(self, description: str) -> None:
        'Sets description'
        self.description = description

    def describe(self) -> None:
        "Describes"
        print(f'The [{self.name}] is here - {self.description}')

    def get_name(self) -> str:
        'Gets name'
        return self.name
