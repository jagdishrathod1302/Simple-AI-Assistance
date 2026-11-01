from openai import OpenAI
from dotenv import load_dotenv
import os
from tools import TOOLS, FUNCTION_NAME_TO_FUNCTION_MAP
import json 

load_dotenv() #by default look .env file 

client = OpenAI(
    base_url=os.getenv("BASE_URL"),
    api_key=os.getenv("API_KEY"),
)

messages = []

messages.append(
    {
    "role":"system",
    "content":"Act like a very humble agent and respond always unders 20 words."
    }
)

#safety limit of toll calling 5 time model only able to call the tools 
MAX_STEPS = 5

#chat user loop 
while True:
    user_input = input("\nJagdish: ")
    if user_input.lower() in ["exit", "quit", "bye", "goodbye"]:
        break

    messages.append({"role": "user", "content": user_input})

    response = client.chat.completions.create(
        model=os.getenv("MODEL"),
        messages=messages,
        tools=TOOLS,
    )

    #print("Assitant: " + str(response))

    msg = response.choices[0].message

    # Tool call chainned
    for steps in range(MAX_STEPS):
        response = client.chat.completions.create(
                model=os.getenv("MODEL"),
                messages=messages,
                tools=TOOLS,
        )

        msg = response.choices[0].message

        if not msg.tool_calls:
            break

        messages.append(msg)

        for tool_call in msg.tool_calls:
            func_name = tool_call.function.name
            func_args = {}
            try:
                func_args = json.loads(tool_call.function.arguments)
                fn = FUNCTION_NAME_TO_FUNCTION_MAP[func_name]
                result = fn(**func_args)
            except Exception as e:
                result = f"Error calling function {func_name}: {e}"

            messages.append({
                "role": "tool",
                "tool_call_id": tool_call.id,
                "content": str(result),
            })

    else:
        #Ran out of steps The model never gave the final answer 
        fallback = "Sorry, I clould not finish this with in the step limit."
        messages.append({
            "role": "assistant",
            "content": fallback
        })
        print("Assistant: "+fallback)
        continue 
    # these two must be inside the while loop
    messages.append(
        {"role": "assistant", 
         "content": msg.content})
    print("Assistant: " + msg.content)