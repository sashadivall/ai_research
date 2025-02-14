
# import MyOpenAI
from myopenai import MyOpenAI


# Create the api
api = MyOpenAI()


# Assign some variables


topic = "College life"

# Create your prompt
myprompt = f"Write a haiku about {topic}."


# Call the api "ask" function
answer = api.ask(prompt=myprompt)



# print the result
print(answer)

