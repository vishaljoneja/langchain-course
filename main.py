from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain_ollama import ChatOllama

load_dotenv()

def main():
    print("Hello from langchain-ollama!")
    information = "John Doe is a software engineer with 10 years of experience in web development. He has worked on various projects involving Python, JavaScript, and cloud technologies. In his free time, he enjoys hiking and photography."

    summary_template = """
    given the information {information} about a person, summarize the information in a few sentences and two interesting facts about the person."""

    summary_prompt_template = PromptTemplate(
        input_variables=["information"],
        template=summary_template,
    )   

    llm = ChatOllama(temperature=0, model="gpt-oss:20b")
    chain = summary_prompt_template | llm

    response = chain.invoke(input={"information": information})
    print(response.content)
if __name__ == "__main__":
    main()
