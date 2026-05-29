import os 
import json

def initialize_memory():
    if os.path.isfile("chat_history.json"):
        conversation = load_memory()
    else:
        conversation = create_memory()
    return conversation 

def create_memory():
    with open("chat_history.json", "w", encoding="utf-8") as file:
        conversation = [{"role":"system",
                        "content": "You are a strict AI mentor helping a developer improve quickly."}] 
        json.dump(conversation,file,indent = 4)
    return conversation

def load_memory():
    print("chat history.json found || Continuing from memory.......")
    with open('chat_history.json','r', encoding = 'utf8') as file:
        conversation = json.load(file)
    return conversation

def update_memory(conversation):
    with open("chat_history.json","w",encoding='utf8')as f:
        json.dump(conversation,f,indent = 4)


