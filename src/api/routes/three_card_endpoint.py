from fastapi import APIRouter
from src.buisness_logic.three_card import ThreeCardService
import random
from src.buisness_logic.card_deck import Deck
from fastapi import Form
from starlette.responses import HTMLResponse

three_card_router = APIRouter(prefix="/three-card")

html_form = """
<form method="post">
  <input type="text" name="text_input" placeholder="Введите текст">
  <input type="text" name="question" placeholder="Введите вопрос">
  <button type="submit">Отправить</button>
</form>
<div id="response"></div>
<script>
  document.querySelector('form').addEventListener('submit', async function(event) {
    event.preventDefault();
    const formData = new FormData(event.target);
    const responseData = await fetch('/', {
      method: 'POST',
      body: formData
    }).then(response => response.json());
    const responseDiv = document.getElementById('response');
    responseDiv.innerHTML = '';
    responseData.forEach(item => {
      const p = document.createElement('p');
      p.innerHTML = `Card: ${item.card}, Answer: ${item.answer}`;
      responseDiv.appendChild(p);
    });
  });
</script>
"""

@three_card_router.get("/", response_class=HTMLResponse)
async def get_root():
    return html_form


@three_card_router.post("/")
def get_tree_card_prediction(question: str = Form(...)):
    deck = Deck()
    cards = deck.shuffle()[0:3]

    # card_numb = random.randint(1, 77)
    prof_class = ThreeCardService()
    answers = prof_class.ask_gpt
    return [{"card": cards[i], "answer": [i]} for i in range(3)]
