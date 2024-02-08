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

