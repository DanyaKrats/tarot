from .chat_gpt_connection import ChatGptConnection
from .card_deck import Deck, Card

class COTDService():
    def __init__(self) -> None:
        self.gpt = ChatGptConnection()
        self.deck = Deck()

    def ask_gpt(self, card:Card, context = None):
        card = card.full_name()
        prompt = self.make_prompt(card=card, context=context)
        return self.gpt.send_question(question=prompt)
    
    def make_prompt(self, card, context):
        promt = f"We do tarot card reading. Format: Card of the day. I got {card}. What kind of day will I have? Answer in language {context['language']}"
        print(promt)
        return promt