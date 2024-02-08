import logging
from functools import wraps
from typing import Union, TypeVar
from fastapi import APIRouter, Depends, Header, HTTPException, Request, status
from typing import Callable, Union, Optional, Any
from pydantic import BaseModel
from dataclasses import dataclass
from fastapi import Form
from src.buisness_logic.cotd import COTDService


cotd_router = APIRouter(prefix="/card-of-the-day")

@cotd_router.get("/{card_numb}")
def get_cotd(card_numb: int):
    if card_numb > 77 or card_numb < 0:
        return {"Incorrect Input": card_numb}
    prof_class = COTDService()
    return {"your_result": prof_class.ask_gpt(card_numb)}

