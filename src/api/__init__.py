
from fastapi import APIRouter
from .routes.card_of_the_day_endpoint import cotd_router
from .routes.three_card_endpoint import three_card_router
from .routes.main_page import main_router

router = APIRouter()
router.include_router(cotd_router)
router.include_router(three_card_router)
router.include_router(main_router)