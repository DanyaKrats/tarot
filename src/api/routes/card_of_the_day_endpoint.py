from fastapi import APIRouter
from src.buisness_logic.cotd import COTDService


cotd_router = APIRouter(prefix="/card-of-the-day")

@cotd_router.get("/{card_numb}")
def get_cotd(card_numb: int):
    if card_numb > 77 or card_numb < 0:
        return {"Incorrect Input": card_numb}
    prof_class = COTDService()
    return {"your_result": prof_class.ask_gpt(card_numb)}

