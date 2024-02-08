from .chat_gpt_connection import ChatGptConnection
from .card_deck import Deck

class COTDService():
    def __init__(self) -> None:
        self.gpt = ChatGptConnection()
        self.deck = Deck()

    def ask_gpt(self, card_numb, context = None):
        card = self.deck.get_card_name(card_numb)

        prompt = self.make_prompt(card=card, context=context)
        return self.gpt.send_question(question=prompt)
    
    def make_prompt(self, card, context):
        print(card)
        return f"We do tarot card reading. Format: Card of the day. I got {card}. What kind of day will I have?"
        # return f"Мы занимаемся гаданием на картах таро. Формат: Карта дня. У меня выпал {card}.Что это значит? Какой у меня будет день?"
    