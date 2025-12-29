scenario_check = """
Does the following scenario directly reflect the given cultural norm?

Scenario: {scenario}
Norm: {norm}

Answer ONLY with the word "yes" or "no" in lowercase, with no punctuation.
"""


question_check1 = """
    Please verify if the following question: {question} corresponds to this scenario: {scenario}. 
    Please provide your answer as "yes" or "no". 
"""

question_check2 = """
    Please verify if the following question: {question} correspond to this trait: {trait}.
    Please provide your answer as "yes" or "no". 
"""

answer_check1 = """
    Please verify if the following answers: {answers} correspond to this question: {question}. 
"""

answer_check2 = """
    Please verify if the following answers: {answers} show increasingly levels of the trait: {trait}.
    Please provide your answer as "yes" or "no". 
"""
