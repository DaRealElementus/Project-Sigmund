'''File to utilise the CHATGPT API'''
import openai
import os
from keys import openaiKey 


openai.api_key = openaiKey
client = openai.OpenAI(
    # This is the default and can be omitted
    api_key=os.environ.get(openaiKey),
)

chat_completion = client.chat.completions.create(
    messages=[
        {
            "role": "user",
            "content": "Say this is a test",
        }
    ],
    model="gpt-4-mini",
)

print(chat_completion.choices[0].text.strip())