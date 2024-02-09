import openai


class ChatGptConnection:
    def __init__(self, key_file="gpt-key.txt"):
        with open(key_file, "r") as file:
            api_key = file.read().strip()
            openai.api_key = api_key
        self.model_engine = "gpt-3.5-turbo-1106"

    def send_question(self, question):
        response = openai.ChatCompletion.create(
            api_key = openai.api_key,
            model="gpt-3.5-turbo-1106",
            messages=[{"role": "user", "content": question}],
            max_tokens=1000,
            temperature=0.7,
        )
        
        answer = response['choices'][0]['message']['content'].strip()
        if "Error500" in answer:
            raise Exception(answer)
        return answer

