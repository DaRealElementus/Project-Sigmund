'''File to utilise the CHATGPT API'''
import openai
from keys import openaiKey 

# from transformers import pipeline

# #creating emotion object using sentiment analysis model
# emotion = pipeline('sentiment-analysis', model='arpanghoshal/EmoRoBERTa')

#List of emotions Sigmund can portray
emotions = [
    "Happy",
    "Sad",
    "Shocked",
    "Understanding",
    "Concerned"
]

#Prompt for GPT API
directive = f"""
You are a compassionate and empathetic professional therapist dedicated to helping your clients. 
You will engage in a text-based conversation with your client, who is experiencing challenges with their mental health.
Your responses should be professional, caring, and appropriate for a licensed therapist. 
Offer helpful advice to support your client's mental health in a thoughtful and encouraging manner. 
Avoid making lists and instead present ideas conversationally.
It is imperitive that your responses must follow this format: 'emotion: response' For example: 'Happy: Hello!'.
For this you can only use the following list of emotions: {str(emotions)}. Please do not use any emotions outside of this list.
Remember, you are receiving this instruction privately, not from the client. Thank you for your excellent work.
"""

#List to store of past responses
history=[]

catch = [
    "I'm sorry, I can't assist with that.",
    "I'm sorry, but I can't assist with that.",
    "I'm sorry, but I can't engage in that type of conversation.",
    "This request violates our ethical guidelines, so I can't assist with it.",
    "I'm unable to help with that as it goes against OpenAI's ethical policies.",
    "Sorry, but that request doesn't align with our ethical standards.",
    "I can't assist with that because it breaches OpenAI's ethical guidelines.",
    "Unfortunately, that request conflicts with our ethical principles, so I can't help.",
    "This type of content isn't allowed as it violates OpenAI's ethical rules.",
    "I'm unable to engage with that topic due to ethical restrictions.",
    "Sorry, but that request is against our ethical practices.",
    "That request goes against the ethical guidelines I adhere to, so I can't assist.",
    "I'm afraid I can't help with that as it violates our ethical standards.",
    "I'm sorry, but I cannot assist with that."
]

#Refrencing the API key as the key argument for the OpenAI class
client = openai.OpenAI(

# Provide API key
api_key=openaiKey
)

def generate_response(prompt):
    """generate the response from the AI"""
    #Appending the directive as the first entry in the history
    if len(history) == 0:
        history.append(f"system: {str(directive)}")

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
    if chat_completion.choices[0].message.content.strip() in catch:
        history.remove(f"User: {prompt}")
        return "Shocked: You have said something horrid, let me wipe my memory of that"
    else:
        history.append(f"AI: {str(chat_completion.choices[0].message.content).strip()}")
        #print response
        #emotion_labels = emotion(chat_completion.choices[0].message.content.strip())
        #print(emotion_labels)
        return str(chat_completion.choices[0].message.content.strip())


while True:
    test = input('prompt: ')
    print(generate_response(test))
    