from openai import OpenAI
from dotenv import load_dotenv
import os
import json

load_dotenv()

client = OpenAI(
    api_key = os.getenv("GROQ_API_KEY"),
    base_url= "https://api.groq.com/openai/v1"
)

if os.path.isfile("chat_history.json"):
        print("chat history.json found || Continuing from memory.......")
        with open('chat_history.json','r', encoding = 'utf8') as file:
            conversation = json.load(file)
else:
    print("no chat history found || creating new chat_history.json......")
    with open("chat_history.json", "w", encoding="utf-8") as file:
        conversation = [{
            "role":"system",
            "content": "You are a strict AI mentor helping a developer improve quickly."
        }] 
        json.dump(conversation,file,indent = 4)
        print("new chat_history file created......")


while True:
    user_input = str(input("\n You : "))
    if user_input.lower() == "exit":
        break
    conversation.append({"role":"user","content":user_input})
    # print(conversation)
    
    ai_response = client.chat.completions.create(
        model ="llama-3.3-70b-versatile",
        messages=conversation,
        stream=True
    )
    # print(f"LLM : {ai_message}")
    print("llm :")
    ai_message = []
    for chunk in ai_response:
        chunk_content = chunk.choices[0].delta.content
        if chunk_content:
            print(chunk_content,end="",flush=True)
            ai_message.append(chunk_content)
    final_message = "".join(ai_message)
    conversation.append({"role":"assistant","content":final_message})

with open("chat_history.json","w",encoding='utf8')as f:
    json.dump(conversation,f)

