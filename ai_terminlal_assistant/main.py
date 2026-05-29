from memory import initialize_memory,update_memory
from llm import generate_response

conversation = initialize_memory()

while True:
    user_input = str(input("\n You : "))
    if user_input.lower() == "exit":
        break
    conversation.append({"role":"user","content":user_input})
    print("llm : ")
    response = generate_response(conversation)
    conversation.append(response)

update_memory(conversation)
print("memory updated")
