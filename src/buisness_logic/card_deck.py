import random

major_arcanas ={
    0: 'The Fool',
    1: 'The Magician',
    2: 'The High Priestess',
    3: 'The Empress',
    4: 'The Emperor',
    5: 'The Hierophant',
    6: 'The Lovers',
    7: 'The Chariot',
    8: 'Strength',
    9: 'The Hermit',
    10: 'Wheel of Fortune',
    11: 'Justice',
    12: 'The Hanged Man',
    13: 'Death',
    14: 'Temperance',
    15: 'The Devil',
    16: 'The Tower',
    17: 'The Star',
    18: 'The Moon',
    19: 'The Sun',
    20: 'Judgement',
    21: 'The World'
}

minor_arcanas = {
    22: 'Ace of Wands', 23: 'Two of Wands', 24: 'Three of Wands', 25: 'Four of Wands', 26: 'Five of Wands', 27: 'Six of Wands', 28: 'Seven of Wands', 29: 'Eight of Wands', 30: 'Nine of Wands', 31: 'Ten of Wands', 32: 'Page of Wands', 33: 'Knight of Wands', 34: 'Queen of Wands', 35: 'King of Wands', 36: 'Ace of Cups', 37: 'Two of Cups', 38: 'Three of Cups', 39: 'Four of Cups', 40: 'Five of Cups', 41: 'Six of Cups', 42: 'Seven of Cups', 43: 'Eight of Cups', 44: 'Nine of Cups', 45: 'Ten of Cups', 46: 'Page of Cups', 47: 'Knight of Cups', 48: 'Queen of Cups', 49: 'King of Cups', 50: 'Ace of Swords', 51: 'Two of Swords', 52: 'Three of Swords', 53: 'Four of Swords', 54: 'Five of Swords', 55: 'Six of Swords', 56: 'Seven of Swords', 57: 'Eight of Swords', 58: 'Nine of Swords', 59: 'Ten of Swords', 60: 'Page of Swords', 61: 'Knight of Swords', 62: 'Queen of Swords', 63: 'King of Swords', 64: 'Ace of Pentacles', 65: 'Two of Pentacles', 66: 'Three of Pentacles', 67: 'Four of Pentacles', 68: 'Five of Pentacles', 69: 'Six of Pentacles', 70: 'Seven of Pentacles', 71: 'Eight of Pentacles', 72: 'Nine of Pentacles', 73: 'Ten of Pentacles', 74: 'Page of Pentacles', 75: 'Knight of Pentacles', 76: 'Queen of Pentacles', 77: 'King of Pentacles'}


class Card:
    def __init__(self, value:int, rotated:bool = None) -> None:
        self.value:int = value
        self.rotated: bool = self.rand_rotated()
        self.picture:str = value

    def rand_rotated(self):
        obj_id = id(self)
        hex_address = hex(obj_id)
        decimal_address = int(hex_address, 16)
        digit_sum = sum(int(digit) for digit in str(decimal_address))
        return digit_sum % 2 == 0

    def __str__(self) -> str:
        return self.full_name()
    
    def full_name(self):
        arcanas = major_arcanas | minor_arcanas
        
        if self.rotated:
            return "Reversed " + arcanas[self.value]
        
        return "Upright " + arcanas[self.value]

class Deck:
    def  __init__(self, shuffle:bool = True) -> None:
        self.deck = [Card(value = value) for value in range(0, 78)]
        if shuffle:
            random.shuffle(self.deck)
    
    def shuffle(self):
        return self.deck