from memory import initialize_memory,save_conversation,reset_memory
from llm import generate_response

print("loading conversation")
conversation = initialize_memory()
# print(conversation)

def show_help():
    print('Available commands:\n/help\n/clear\n/save\n/exit')

def save(conversation):
    save_conversation(conversation)

def clear():
    return reset_memory()

def exit_chat():
    print("exiting from chat....See ya again!!")

def handle_chat(user_input):
    conversation.append({"role":"user","content":user_input})
    print ("calling model.......")
    print("llm : ")
    response = generate_response(conversation)
    conversation.append(response)
    save_conversation(conversation)

while True:
    user_input = str(input("\n You : "))
    if user_input.lower() == "/help":
        show_help()
    
    elif user_input.lower() == "/exit":
        save_conversation(conversation)
        exit_chat()
        break
    
    elif user_input.lower() == "/save":
        print("saving conversation.....")
        save(conversation)
    
    elif user_input.lower() == "/clear":
       print("clearing previous convesations....")
       conversation = clear() 
    
    else:
        handle_chat(user_input)

print("saving conversation......")
save_conversation(conversation)
print("conversation saved")