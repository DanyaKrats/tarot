
from fastapi import APIRouter
from .routes.card_of_the_day_endpoint import cotd_router

router = APIRouter()
router.include_router(cotd_router)
