from memory import initialize_memory,save_conversation
from llm import generate_response

print("loading conversation")
conversation = initialize_memory()

while True:
    user_input = str(input("\n You : "))
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
