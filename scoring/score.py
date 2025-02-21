import pandas as pd

from myopenai.myopenai import MyOpenAI




def score_theory(data: pd.DataFrame) -> None:
    instructions = """
    You are an expert in AI ethics and curriculum evaluation. 
    You will be given a list of course descriptions for introductory AI and machine learning classes offered at the 
    undergraduate level. For each description, assign it a score from 1 to 5 based on the extent to which the course description emphasizes theory according to the
    following scoring system. If a description is blank, score it a 0. \n\n
    Scoring System:\n
    - **1:** No emphasis on theory - The description provides no indication that any portion of the class will be focused on theory.\n
    - **2:** Limited emphasis on theory - Suggests that the theory of AI and ML will be covered, but the course focuses more on other aspects of AI/ML, such as application .\n
    - **3:** Moderate emphasis on theory - Implies that at least half of the course will be focused on AI/ML theory.\n
    - **4:** Substantial emphasis on theory - Suggests that the majority of the course wil be focused on AI/ML theory.\n
    - **5:** High emphasis on theory - Suggests that almost the entire course will be focused on AI/ML theory and no other topics.\n\n
    For each course description provided, score the description with a floating-point value between 1 and 5.
    Return a string dictionary with a key `values` and containing an array of floats, and a key `justification` with a short justification for each score {"values": [score1, score2, ...], "justification": [justification1, justification2, ...]}.
    **DO NOT FORMAT THE STRING AS JSON**. Return the dictionary as a string
    """
    my_chat = MyOpenAI(instructions = instructions)
    intro_description = list(data["Intro to AI Course Description"])
    results, justifications = my_chat.score_multiple_courses(intro_description)

    data["Theory Score"] = results
    data["Theory Justification"] = justifications


def score_application(data: pd.DataFrame) -> None:
    instructions = """
    You are an expert in AI ethics and curriculum evaluation. 
    You will be given a list of course descriptions for introductory AI and machine learning classes offered at the 
    undergraduate level. For each description, assign it a score from 1 to 5 based on the extent to which the course description emphasizes application according to the
    following scoring system. If a description is blank, score it a 0. \n\n
    Scoring System:\n
    - **1:** No emphasis on application - The description provides no indication that any portion of the class will be focused on application.\n
    - **2:** Limited emphasis on application - Suggests that the application of AI and ML will be covered, but the course focuses more on other aspects of AI/ML, such as theory .\n
    - **3:** Moderate emphasis on application - Implies that at least half of the course will be focused on AI/ML application.\n
    - **4:** Substantial emphasis on application - Suggests that the majority of the course wil be focused on AI/ML application.\n
    - **5:** High emphasis on application - Suggests that almost the entire course will be focused on AI/ML application and no other topics.\n\n
    For each course description provided, score the description with a floating-point value between 1 and 5.
    Return a string dictionary with a key `values` and containing an array of floats, and a key `justification` with a short justification for each score {"values": [score1, score2, ...], "justification": [justification1, justification2, ...]}.
    **DO NOT FORMAT THE STRING AS JSON**. Return the dictionary as a string
    """
    my_chat = MyOpenAI(instructions = instructions)
    intro_description = data["Intro to AI Course Description"]
    results, justifications = my_chat.score_multiple_courses(intro_description)

    data["Application Score"] = results
    data["Application Justification"] = justifications

def score_ethics_intro(data: pd.DataFrame) -> None:
    instructions = """
    You are an expert in AI ethics and curriculum evaluation. 
    You will be given a list of course descriptions for introductory AI and machine learning classes offered at the 
    undergraduate level. For each description, assign it a score from 1 to 5 based on the extent to which the course description emphasizes ethics according to the
    following scoring system. If a description is blank, score it a 0. \n\n
    Scoring System:\n
    - **1:** No emphasis on ethics - The description provides no indication that any portion of the class will be focused on ethics.\n
    - **2:** Limited emphasis on ethics - Suggests that the ethics of AI and ML will be covered, but the course focuses more on other aspects of AI/ML, such as application or theory.\n
    - **3:** Moderate emphasis on ethics - Implies that at least half of the course will be focused on AI/ML ethics.\n
    - **4:** Substantial emphasis on ethics - Suggests that the majority of the course wil be focused on AI/ML ethics.\n
    - **5:** High emphasis on ethics - Suggests that almost the entire course will be focused on AI/ML ethics and no other topics.\n\n
    For each course description provided, score the description with a floating-point value between 1 and 5.
    Return a string dictionary with a key `values` and containing an array of floats, and a key `justification` with a short justification for each score {"values": [score1, score2, ...], "justification": [justification1, justification2, ...]}.
    **DO NOT FORMAT THE STRING AS JSON**. Return the dictionary as a string
    """
    my_chat = MyOpenAI(instructions = instructions)
    intro_description = data["Intro to AI Course Description"]
    results, justifications = my_chat.score_multiple_courses(intro_description)


    data["Ethics Score (Intro Course Description)"] = results
    data["Ethics (Intro) Justification"] = justifications

def score_ethics_breadth(data: pd.DataFrame) -> None:
    instructions = """
    You are an expert in AI ethics and curriculum evaluation. 
    You will analyze a course description for an Ethics in AI course and assign it a score from 1 to 5 
    based on the breadth of ethical topics it covers. Use the scoring system below. If the description is blank, give it a 0.\n\n
    Scoring System:\n
    - **1:** Very Narrow - The course covers only one or two broad ethical concerns (e.g., “AI bias” or “ethics in AI” without further elaboration).\n
    - **2:** Limited Breadth - Covers a few topics but lacks coverage of key areas such as privacy, fairness, accountability, or regulatory considerations.\n
    - **3:** Moderate Breadth - Mentions a reasonable number of topics (e.g., bias, privacy, explainability, social impact) but may omit key dimensions such as legal frameworks or governance.\n
    - **4:** Substantial Breadth - Covers a wide range of ethical concerns, including technical, legal, and societal aspects. May mention frameworks, case studies, or interdisciplinary perspectives.\n
    - **5:** Very Comprehensive - The course description includes an extensive range of AI ethics topics across multiple dimensions, including fairness, transparency, accountability, legal regulations, algorithmic bias, environmental impacts, labor concerns, and more.\n\n
    For each course description provided, score the description with a floating-point value between 1 and 5.
    Return a string dictionary with a key `values` and containing an array of floats, and a key `justification` with a short justification for each score {"values": [score1, score2, ...], "justification": [justification1, justification2, ...]}.
    **DO NOT FORMAT THE STRING AS JSON**. Return the dictionary as a string
    """
    my_chat = MyOpenAI(instructions = instructions)
    intro_description = data["Ethics in AI Course Description"]
    results, justifications = my_chat.score_multiple_courses(intro_description)


    data["Ethics Course Breadth Score"] = results
    data["Ethics Course Breadth Justification"] = justifications

def score_ethics_depth(data: pd.DataFrame) -> None:
    # TODO - modify prompt to score breadth and depth
    instructions = """
    You are an expert in AI ethics and curriculum evaluation. 
    You will analyze a course description for an Ethics in AI course and assign it a score from 1 to 5 
    based on the depth of ethical topics it covers. Use the scoring system below. If the description is blank, give it a 0.\n\n
    Scoring System:\n
    - **1:** Very high-level - The description provides only a broad or superficial overview of AI ethics without covering specific ethical issues in detail.\n
    - **2:** Limited depth - Mentions some ethical concerns but lacks depth or specificity.\n
    - **3:** Moderate depth - Covers a reasonable range of AI ethics topics but does not go into much technical or theoretical detail.\n
    - **4:** Substantial depth - Discusses multiple ethical issues in AI with a fair amount of detail, possibly including case studies or frameworks.\n
    - **5:** Very in-depth - Provides a highly detailed description of AI ethics, including specific ethical frameworks, technical considerations, and real-world applications.\n\n
    For each course description provided, score the description with a floating-point value between 1 and 5.
    Return a string dictionary with a key `values` and containing an array of floats, and a key `justification` with a short justification for each score {"values": [score1, score2, ...], "justification": [justification1, justification2, ...]}.
    **DO NOT FORMAT THE STRING AS JSON**. Return the dictionary as a string
    """
    my_chat = MyOpenAI(instructions = instructions)
    intro_description = data["Ethics in AI Course Description"]
    results, justifications = my_chat.score_multiple_courses(intro_description)


    data["Ethics Course Depth Score"] = results
    data["Ethics Course Depth Justification"] = justifications

    
