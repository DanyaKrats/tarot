from fastapi import APIRouter
from src.buisness_logic.cotd import COTDService
import random
from src.buisness_logic.card_deck import Deck, Card

cotd_router = APIRouter(prefix="/card_of_the_day")

@cotd_router.get("/{card_numb}")
def get_cotd(card_numb: int):
    if card_numb > 77 or card_numb < 0:
        return {"Incorrect Input": card_numb}
    prof_class = COTDService()
    card = Card(value=card_numb)
    return {
        "Card": card.__str__(),
        "your_result": prof_class.ask_gpt(card)
        }

@cotd_router.get("/")
def get_cotd():
    card_numb = random.randint(1, 77)
    card = Card(card_numb)
    prof_class = COTDService()
    return {
        "Card": card.__str__(),
        "your_result": prof_class.ask_gpt(card)
        }

@cotd_router.get("/rand_card/")
def get_random_card():
    card_numb = random.randint(1, 77)
    a = 0
    for i in range(100):
        card = Card(card_numb)
        if card.rotated:
            a+=1
    print(a)
    return {"Card": card.__str__(),}