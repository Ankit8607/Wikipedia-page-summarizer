from openai import OpenAI
from dotenv import load_dotenv, find_dotenv  # to load environment variables
import os

_ = load_dotenv(find_dotenv())  # read local .env file

OpenAI.api_key = os.environ['OPENAI_API_KEY']  # set openai_api key
client = OpenAI()

# function for paraphrasing
def paraphraser(s):
    response = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": "You are a helpful assistant. You will paraphrase the given text"},
            {"role": "user", "content": s}
        ]
    )
    return response.choices[0].message.content