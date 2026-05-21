#bug1 

Problem:
404 model_not_found

cause:
Typed = instead of - in model name 


Fix:
    Changed:
    llama=3.3-70b-versatile

    To:
    llama-3.3-70b-versatile



Problem2:
tried making chatbot memory by giving a list of lists instead of just appending the dictionaries

Fix: 
    changed it by just appending dictionaries to conversation and then setting 
    message = conversation
