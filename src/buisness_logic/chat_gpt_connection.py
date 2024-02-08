import openai


class ChatGptConnection:
    def __init__(self, api_key:str ="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"):
        openai.api_key = api_key
        self.model_engine = "gpt-3.5-turbo-1106"

    def send_question(self, question):
    # def send_question_to_ChatGPT(question):
        openai.api_key = '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'  # Замените 'your_api_key' на ваш API ключ

        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo-1106",  # Модель GPT, которую вы хотите использовать
            messages=[{"role": "user", "content": question}],
            max_tokens=100,  # Максимальное количество токенов в ответе
            temperature=0.7,  # Параметр температуры, регулирующий разнообразие ответов
        )

        if response:
            return response['choices'][0]['message']['content'].strip()
        else:
            return "Error sending request to ChatGPT API"

