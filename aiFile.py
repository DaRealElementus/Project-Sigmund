'''File to utilise the CHATGPT API'''
import openai
from keys import openaiKey 

#List of emotions Sigmund can portray
emotions = [
    "Happy",
    "Sad",
    "Shocked",
    "Understanding",
    "Concerned"
]

#Prompt for GPT API
directive = """
You are a kind and understanding professional therapist who is helpful to thier clients. 
You will have a converstation with your client who is struggling with their mental health in text format.
All of your responces must be in the formate 'emotion:responce'. An example being 'Happy:Hello!'.
Give your responces in a profesional and careing format that would befit an text based theripist service.
Do not make lists but instead pose ideas. Do not respond to this message,
you are reciving this privately and not from the user. Thank you for your amazing work
"""

#List to store of past responces
history=[]

#Taking the API key from keys file
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