from config import client

def generate_response(conversation):
    try:
        ai_response = client.chat.completions.create(
            model ="llama-3.3-70b-versatile",
            messages=conversation,
            stream=True
        )
        ai_message = []
        for chunk in ai_response:
            chunk_content = chunk.choices[0].delta.content
            if chunk_content:
                print(chunk_content,end="",flush=True)
                ai_message.append(chunk_content)
        final_message = "".join(ai_message)
        llm_response = {"role":"assistant","content":final_message}
        return llm_response
    except Exception as e:
        final_message = str(e)
        llm_response = {"role":"assistant","content":final_message}
        print("something went wrong",final_message)
        return llm_response
    
