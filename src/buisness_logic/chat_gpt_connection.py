import openai


class ChatGptConnection:
    def __init__(self, key_file="gpt-key.txt"):
        with open(key_file, "r") as file:
            api_key = file.read().strip()
            openai.api_key = api_key
        self.model_engine = "gpt-3.5-turbo-1106"

    def send_question(self, question):
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo-1106",
            messages=[{"role": "user", "content": question}],
            max_tokens=100,
            temperature=0.7,
        )

        if response:
            return response['choices'][0]['message']['content'].strip()
        else:
            return "Error sending request to ChatGPT API"

