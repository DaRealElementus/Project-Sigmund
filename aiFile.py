'''File to utilise the CHATGPT API'''
from openai import OpenAI
from keys import openaiKey 


api_key = openaiKey
client = OpenAI(
    # This is the default and can be omitted
    api_key=openaiKey
)

chat_completion = client.chat.completions.create(
    messages=[
        {
            "role": "user",
            "content": "Say this is a test",
        }
    ],
    model="gpt-4o-mini"
)
#Apparently this works....
print(str(chat_completion.choices[0].text).strip())