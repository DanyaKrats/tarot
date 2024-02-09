from .chat_gpt_connection import ChatGptConnection
from .card_deck import Deck, Card

class ThreeCardService():
    def __init__(self) -> None:
        self.gpt = ChatGptConnection()
        self.deck = Deck()

    def ask_gpt(self, cards: list[Card], context = None):
        answers = {}
        context = {'base_context': context}
        for i in range(3):
            context["iteration"] = i
            card = cards[i].full_name()
            
            prompt = self.make_prompt(card=card, context=context)
        
            answers[i] = self.gpt.send_question(question=prompt)
            context["answers"] = answers
        
        return answers

    def make_prompt(self, card, context):
        time = ''
        if context["iteration"] == 0:
            time = 'past' 
        elif context['iteration'] == 1:
            time = 'present'
        else:
            time = 'future'

        promt = ''
        
        if context['iteration'] == 1:
            promt += f"Your prediction for past was: {context['answers'][0]}. "        
        if context['iteration'] == 2:
            promt += f"Your prediction for present was: {context['answers'][1]}. "     
        if promt != '':
            promt += 'You can reffer this info in your answer. '
        
        promt = "You can speek any language. You believe in tarot becouse you are fortune teller (act like him). If you don’t know something, try to answer as the person asking the question expects. You can try the cold reading method. We do tarot card reading. Format: Three cards for the past, present and future. " + promt       
        promt += "Remember: If you don’t know something about a person, his personality or his environment, come up with it based on the cards. "
        promt += f"My question is '{context['base_context']['question']} based on cards? Maybe cards can give some signs?'"
        promt += f"I got {card} for {time}. What does it mean? "
        # promt += f"Answer in language {context['base_context']['language']} "
        promt += "If you can't understand the question, return only one word 'Error500' and brief discription why you can not answer, BUT ONLY if you cannot understand it, if the question is clear but you don’t know, come up with an answer based on the cards and previous answers, if any"
        #promt += "If question goes against the ethical guidelines of tarot reading you can answer in a joke way. For example 'When AI take over the world' - 'Tomorrow'"
        print(promt)
        return promt