from memory import initialize_memory,save_conversation,reset_memory
from llm import generate_response

print("loading conversation")
conversation = initialize_memory()
print(conversation)
while True:
    user_input = str(input("\n You : "))
    if user_input.lower() == "/help":
        print('Available commands:\n/help\n/clear\n/save\n/exit')
    if user_input.lower() == "/save":
        save_conversation(conversation)
    if user_input.lower() == "/clear":
        conversation = reset_memory()
    if user_input.lower() == "exit":
        save_conversation(conversation)
        break
    conversation.append({"role":"user","content":user_input})
    print ("calling model.......")
    print("llm : ")
    response = generate_response(conversation)
    conversation.append(response)

print("saving conversation......")
save_conversation(conversation)
print("conversation saved")


# /help
# /save
# /clear
# cleaner /exit
