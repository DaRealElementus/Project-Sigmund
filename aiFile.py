'''File to utilise the CHATGPT API'''
import openai
from keys import openaiKey 


api_key = openaiKey
client = openai.OpenAI(
    # This is the default and can be omitted
    api_key=openaiKey
)

while True:
    chat_completion = client.chat.completions.create(
        messages=[
            {
                "role": "user",
                "content":input(""),
            }
        ],
        model="gpt-4o-mini",
    )
    #ITS ALIVE
    print(str(chat_completion.choices[0].message.content).strip())