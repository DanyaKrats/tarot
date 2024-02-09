from fastapi import APIRouter
from starlette.responses import HTMLResponse

main_router = APIRouter(prefix="")

@main_router.get("/", response_class=HTMLResponse)
async def mainpage():
    html_content = """
    <html>
    <head>
        <title>Tarot AI</title>
    </head>
    <body>
        <h1>What do You need</h1>
        <ul>
            <li><a href="/card_of_the_day/">Карта дня</a></li>
            <li><a href="/three_cards/">Три карты</a></li>
        </ul>
    </body>
    </html>
    """
    return HTMLResponse(content=html_content)