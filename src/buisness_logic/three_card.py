from .chat_gpt_connection import ChatGptConnection
from .card_deck import Deck

class ThreeCardService():
    def __init__(self) -> None:
        self.gpt = ChatGptConnection()
        self.deck = Deck()

    def ask_gpt(self, cards_numb: list[int], context = None):
        answers = {}
        context = {'base_context': context}
        for i in range(3):
            context["iteration"] = i
            card = self.deck.get_card_name(cards_numb[card])
            
            prompt = self.make_prompt(card=card, context=context)
        
            answers ={i: self.gpt.send_question(question=prompt)}
            context["answers"] = answers


    def make_prompt(self, card, context):
        time = ''
        if context["iteration"] == 0:
            time = 'past' 
        elif context["iteration"] == 1:
            time = 'present'
        else:
            time = 'future'

        promt = ''
        
        if context["iteration"] == 1:
            promt += f"Your prediction for past was: {context['answers'][context["iteration"]]}. "        
        if context["iteration"] == 2:
            promt += f"Your prediction for present was: {context['answers'][context["iteration"]]}. "     
        if promt != '':
            promt += 'You can reffer this info in your answer. '

        promt = "We do tarot card reading. Format: Three cards for the past, present and future. " + promt       
        promt += f"I got {card} for {time}. What does it mean? "

        return promt