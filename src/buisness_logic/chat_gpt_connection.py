import openai
import httpx


class ChatGptConnection:
    def __init__(self, api_key:str ="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"):
        openai.api_key = api_key
        self.model_engine = "text-davinci-002"

    def send_question(self, question):
        # Отправляем вопрос в OpenAI API и получаем ответ от модели
        prompt = f"Q: {question}\nA:"
        response = openai.Completion.create(
            engine=self.model_engine,
            prompt=prompt,
            max_tokens=60,
            n=1,
            stop=None,
            temperature=0.7,
        )

        # Обрабатываем ответ и возвращаем текст
        answer = response.choices[0].text.strip()
        return answer