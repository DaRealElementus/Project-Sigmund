'''File to utilise the CHATGPT API'''
import openai
from keys import openaiKey 

#HayBae you need to turn this into functions

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

#List to store of past responses
history=[]

#Refrencing the API key as the key argument for the OpenAI class
client = openai.OpenAI(
    
    # Provide API key
    api_key=openaiKey
)

#Appending the directive as the first entry in the history
history.append(f"system: {str(directive)}")

while True:

    #inputing the users responce
    prompt = input("\n:")

    #appending the users reponce into the history
    history.append(f"User: {prompt}")

    #Creates chat with API
    chat_completion = client.chat.completions.create(

        #package sent to GPT
        messages=[
            {
                "role": "user", 
                "content":prompt, #Generate response based on user prompt
                "role": "system",
                "content":"this is your memory: " + str(history) #Provide past responses

            }
        ],

        #GPT model to use
        model="gpt-4o-mini",
    )
    #add response to history
    history.append(f"AI: {str(chat_completion.choices[0].message.content).strip()}")
    #print response
    print(str(chat_completion.choices[0].message.content).strip())