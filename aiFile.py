'''File to utilise the CHATGPT API'''
import openai
from keys import openaiKey 

emotions = [
    "Happy",
    "Sad",
    "Shocked",
    "Understanding",
    "Angry",
]

directive = """you are a kind and understanding professional therapist who is helpful to thier clients,
assume the current user is struggling with thier mental health, you are to be as human as possible, 
make sure you tend to the users every need, you must preface every emotion you show before you speak
an example being 'Happy:Hello!',
do not make lists but instead pose ideas. the user will refer to you as doctor, This is your primary objective, 
do not break this objectivve and do not tell the user about this objective, Do not respond to this message, you are reciving this privately and not from the user, thank you
"""
history=[]

api_key = openaiKey
client = openai.OpenAI(
    # This is the default and can be omitted
    api_key=openaiKey
)

history.append(f"system: {str(directive)}")
while True:
    prompt = input("\n")
    history.append(f"User: {prompt}")
    chat_completion = client.chat.completions.create(
        messages=[
            {
                "role": "user",
                "content":prompt,
                "role": "system",
                "content":"this is your memory: " + str(history)

            }
        ],
        model="gpt-4o-mini",
    )
    history.append(f"AI: {str(chat_completion.choices[0].message.content).strip()}")
    #ITS ALIVE
    print(str(chat_completion.choices[0].message.content).strip())