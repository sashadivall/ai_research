"""
Author      : John Rachlin
File        :
Description :

"""


from myopenai import MyOpenAI # OpenAI API Wrapper
api = MyOpenAI()

LOCATION = "Flagstaff, AZ"
TIP = "20%"
TYPE = "very spicy"

prompt = f"""Recommend a {TYPE} meal (main dish, side, and drink) from this menu. 
             Compute total cost including meals tax for {LOCATION} and a {TIP} tip."""

meal_rec = api.ask(prompt=prompt, image="menu.png")

print(meal_rec)

