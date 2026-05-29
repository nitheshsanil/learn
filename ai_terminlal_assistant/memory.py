import os 
import json


system_prompt = [{"role":"system",
                "content": "You are a strict AI mentor helping a developer improve quickly."}] 

def initialize_memory():
    if os.path.isfile("chat_history.json"):
        conversation = load_memory()
    else:
        conversation = create_memory()
    return conversation 

def create_memory():
    with open("chat_history.json", "w", encoding="utf-8") as file:
        conversation = system_prompt
        json.dump(conversation,file,indent = 4)
    return conversation

def load_memory():
    print("chat history.json found || Continuing from memory.......")
    with open('chat_history.json','r', encoding = 'utf8') as file:
        conversation = json.load(file)
        recent_prompts=conversation[-10:]
        conversation=[*system_prompt,*recent_prompts] 
    return conversation

def save_conversation(conversation):
    with open("chat_history.json","w",encoding='utf8')as f:
        json.dump(conversation,f,indent = 4)

def reset_memory():
    with open("chat_history.json", "w", encoding="utf-8") as file:
        conversation = system_prompt
        json.dump(conversation,file,indent = 4)
    return conversation

