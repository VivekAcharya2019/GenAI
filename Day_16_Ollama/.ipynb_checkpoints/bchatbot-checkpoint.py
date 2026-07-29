import requests 

#ollama chat api end point 
url = "http://127.0.0.1:11434/api/chat"


# conversation histroy for chat 
# each message will be a dictionary with two keys role : system/user/ai/assistant "conntent"
history = [
        {
            "role" : "system",
            "content" : "You are a helpfull assistant"
        },
    ]


# Usr can communicate as long as he wants 
while True:

    # take user message 
    user_query = input("\n User : ")

    # break the loops if user says q 
    if user_query == "q":
        break

    # as ollama message strcture create human message
    user_msg = {
                    "role" : "user",
                    "content" : user_query
                }

    # add user message to history 
    history.append(user_msg)

    # call api end point 
    payload = {
        "model" : "llama3.2:1b",
        "messages" : history,
        "stream" : False
    }
    response = requests.post(url,json=payload)
    jdata = response.json()

    # add ai message to history 
    history.append(jdata["message"])

    # show ai message 
    print("\n Bot : ",jdata["message"]["content"])