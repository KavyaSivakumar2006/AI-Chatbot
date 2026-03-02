import os
from dotenv import load_dotenv
from google import genai
load_dotenv()
client=genai.Client(api_key = os.getenv("MY_API_KEY"))
def chat_gemini(prompt):
    response=client.models.generate_content(model="gemini-2.5-flash",contents=prompt)
    return response.text.strip()
while True:
    user_input=input("You:")
    if user_input.lower() in ["quit","bye","exit","thank you"]:
        print("Chatbot: Goodbye!.Happy to help you :).")
        break
    response=chat_gemini(user_input)
    print("Chatbot: ",response)
