import pandas as pd

from myopenai.myopenai import MyOpenAI

my_chat = MyOpenAI()


def score_theory(data: pd.DataFrame) -> None:
    intro_description = data["Intro to AI Course Description"]
    results = []
    my_chat.ask(
        prompt="""
        I will provide you with a course description from a university catalog
        for an introductory artificial intelligence and machine learning course for undergraduate
        students. Your task will be to rate each description on a scale from 1 to 5 depending on how 
        much the course description emphasizes theory, 1 being the least emphasis on theory and 5 being
        the most emphasis on theory. 
        A perfect 5 would have 100 percent emphasis on theory and 0 percent emphasis on application, and a perfect
        1 would have 100 percent emphasis on application and 0 percent emphasis on theory. Return your score as a floating
        point value between 1 and 5 rounded to 1 decimal point and only this value. 
        """
    )
    for description in intro_description:
        
        result = my_chat.ask(
            prompt = f"""
            The following text is a course description from a university catalog
            for an introductory artificial intelligence and machine learning course for undergraduate
            students. Your task will be to rate each description on a scale from 1 to 5 depending on how 
            much the course description emphasizes theory, 1 being the least emphasis on theory and 5 being
            the most emphasis on theory. 
            A perfect 5 would have 100 percent emphasis on theory and 0 percent emphasis on application, and a perfect
            1 would have 100 percent emphasis on application and 0 percent emphasis on theory. Return your score as a floating
            point value between 1 and 5 rounded to 1 decimal point and only this value. 

            Description: {description}
            """
        )
        print(result)
        results.append(result)

   # data["Theory Score"] = results



def score_application(data: pd.DataFrame) -> None:
    pass

def score_ethics(data: pd.DataFrame) -> None:
    pass
