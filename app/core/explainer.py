from langchain_core.prompts import PromptTemplate
from app.core.llm import get_llm




explanation_prompt = PromptTemplate(
    input_variables=["experience_level", "code"],
    template="""
You are a senior software engineer and teacher.

Explain the following code to a {experience_level} developer.

Rules:
- Beginner: use simple language, avoid jargon, explain concepts step by step.
- Intermediate: explain logic and flow, mention patterns when relevant.
- Advanced: focus on design decisions, performance, and edge cases.

Code:
{code}

Explanation:
"""
)


improvements_prompt = PromptTemplate(
    input_variables=["code"],
    template="""
You are performing a constructive code review.

Analyze the following code and provide improvement suggestions.

Rules:
- Focus on readability, maintainability, performance, and best practices
- Use bullet points
- Explain why each suggestion is helpful
- Do not rewrite the code entirely unless necessary

Code:
{code}

Improvement Suggestions:
"""
)

mistakes_prompt = PromptTemplate(
    input_variables=["code"],
    template="""
You are analyzing code to identify possible mistakes or risks.

Rules:
- Identify likely bugs, edge cases, or bad patterns
- Explain why each issue could be a problem
- Use bullet points
- Do not assume the code is wrong, focus on potential issues

Code:
{code}

Potential Mistakes:
"""
)


def explain_code(code: str, experience_level: str) -> str:
    """
    Takes a code snippet and an experience level and returns an explanation.
    """

    # Get the LLM (Ollama for now)
    llm = get_llm()


    explanation_prompt_text = explanation_prompt.format(
        experience_level=experience_level,
        code=code
    )
    improvements_prompt_text = improvements_prompt.format(
        code=code
    )
    mistakes_prompt_text = mistakes_prompt.format(
        code=code
    )

    explanation = llm.invoke(explanation_prompt_text)
    improvements = llm.invoke(improvements_prompt_text)
    common_mistakes = llm.invoke(mistakes_prompt_text)

    # explanation_chain = (
    #     llm
    #     | explanation_prompt
    # )
    # improvements_chain = (
    #     llm
    #     | improvements_prompt
    # )
    # mistakes_chain = (
    #     llm
    #     | mistakes_prompt
    # )

    # explanation = explanation_chain.invoke({
    #     "experience_level": experience_level,
    #     "code": code
    # })

    # improvements = improvements_chain.invoke({
    #     "code": code
    # })

    # common_mistakes = mistakes_chain.invoke({
    #     "code": code
    # })

    return {
        "explanation": explanation.content,
        "improvements": improvements.content,
        "common_mistakes": common_mistakes.content
    }


# def explain_code(code: str, experience_level: str) -> str:
#     """
#     Takes a code snippet and an experience level and returns an explanation.
#     """
#     return {
#         "explanation": "hello",
#         "improvements": "hi",
#         "common_mistakes": "good evening"
#     }

