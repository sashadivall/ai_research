"""
Author      : John Rachlin
File        : translate.py
Description : A simple language translation app

"""

from myopenai import MyOpenAI

api = MyOpenAI()


def translate(src="English", targ="Spanish", phrase=None):
    if phrase is not None:
        prompt = f"Translate from {src} to {targ} the following phrase: {phrase}"
        return api.ask(prompt=prompt)
    else:
        return None


def main():

    # The vodka was good, but the meat was rotten.
    translation = translate(phrase="The spirit is willing, but the flesh is weak", targ="Russian")
    print(translation)

    reverse = translate(phrase=translation, src="Russian", targ="English")
    print(reverse)


main()






