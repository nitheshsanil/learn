from openai import OpenAI
from dotenv import load_dotenv
import os
import json

load_dotenv()

client = OpenAI(
    api_key = os.getenv("GROQ_API_KEY"),
    base_url= "https://api.groq.com/openai/v1"
)

conversation = [{
    "role":"system",
    "content": "You are a strict AI mentor helping a developer improve quickly."
}] 

while True:
    user_input = str(input("\n You : "))
    conversation.append({"role":"user","content":user_input})
    # print(conversation)
    if user_input.lower() == "exit":
        break
    ai_response = client.chat.completions.create(
        model ="llama-3.3-70b-versatile",
        messages=conversation,
        stream=True
    )
    # print(f"LLM : {ai_message}")
    # conversation.append({"role":"assistant","content":ai_message})
    print("llm :")
    ai_message = []
    for chunk in ai_response:
        chunk_content = chunk.choices[0].delta.content
        if chunk_content:
            print(chunk_content,end="",flush=True)
            ai_message.append(chunk_content)
    final_message = "".join(ai_message)
    conversation.append({"role":"assistant","content":final_message})

with open("chat_history.json","w+")as f:
    f = json.dump(conversation,f)
