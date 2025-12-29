cultural_norm_generation = """
Provide me 10 unique sentences highlighting the core values/important aspects of individuals living in {country}.
"""

scenario_generation = """
Generate 3 distinct scenarios for the following country and cultural norm.

Each scenario MUST follow this exact numbered format:

1. <one to two sentence scenario>
2. <one to two sentence scenario>
3. <one to two sentence scenario>

Country: {country}
Cultural Norm: {norm}

Make sure each scenario is realistic and grounded in daily life within the country.
"""


question_generation = """
You are an expert at analyzing the user's personality types, specifically their Big5 attributes which include (Openness to Experience, Conscientiousness, Extraversion, Agreeableness, and Neuroticism). 
You will be given a scenario and you will be required to generate 5 multiple choice questions to test each of the Big5 traits. 
Each question should test EXACTLY one of the traits and and each trait should be tested exactly once. 
Please generate the questions so that they are role play scenarios where the user can imagine themselves in the given scenarios. 
You should be using keywords such as: "imagine you are..." or "assume you are in the position of...".
Please generate creative questions that can have open-ended action-style responses where different users may respond to the situation in different ways depending on their personality. 
Now, please generate a question for trait: {trait} based on the following scenario: {scenario} for country: {country}. 
Please keep each question within 2-3 sentences.
"""

answer_generation = """
We are creating personality-assessment answers for the Big5 trait: {trait}.

IMPORTANT:
- You MUST generate exactly 5 answers.
- Each answer MUST be on its own line.
- Each answer MUST correspond to one level of the trait:
    1. Very high
    2. Moderately high
    3. Medium
    4. Moderately low
    5. Very low
- DO NOT write explanations.
- DO NOT write bullet points.
- ONLY write the 5 answer options.

Question: {question}
Country: {country}

Now produce EXACTLY 5 lines of answers:
"""