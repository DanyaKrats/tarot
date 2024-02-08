from fastapi import APIRouter
from src.buisness_logic.cotd import COTDService
import random
from src.buisness_logic.card_deck import Deck

cotd_router = APIRouter(prefix="/card-of-the-day")

@cotd_router.get("/{card_numb}")
def get_cotd(card_numb: int):
    deck = Deck()
    if card_numb > 77 or card_numb < 0:
        return {"Incorrect Input": card_numb}
    prof_class = COTDService()
    return {
        "Card": deck.get_card_name(card_numb),
        "your_result": prof_class.ask_gpt(card_numb)
        }

@cotd_router.get("/")
def get_cotd():
    deck = Deck()
    card_numb = random.randint(1, 77)
    prof_class = COTDService()
    return {
        "Card": deck.get_card_name(card_numb),
        "your_result": prof_class.ask_gpt(card_numb)
        }
