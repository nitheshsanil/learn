from openai import OpenAI
from dotenv import load_dotenv
import os

load_dotenv()

client = OpenAI(
    api_key = os.getenv("GROQ_API_KEY"),
    base_url= "https://api.groq.com/openai/v1"
)

conversation = [{
    "role":"System",
    "content": "You are a strict AI mentor helping a developer improve quickly."
}] 
while True:
    user_input = input("You : ")
    conversation.append({"role":"user","content":user_input})
    if user_input.lower() == "exit":
        break
    ai_response = client.chat.completions.create(
        model ="llama-3.3-70b-versatile",
        messages=conversation
    )
    ai_message = ai_response.choices[0].message.content
    print(f"LLM : {ai_message}")
    conversation.append({"role":"assistant","content":ai_message})
   