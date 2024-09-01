from crewai import Agent
from tools import search_tool

from dotenv import load_dotenv

import os

from langchain_google_genai import ChatGoogleGenerativeAI

llm = ChatGoogleGenerativeAI(
	model="gemini-1.5-flash",
	verbose=True,
	temperature=0.5,
	google_api_key=os.getenv("GOOGLE_API_KEY"),
)

# os.environ["OPENAI_API_KEY"] = os.getenv("OPENAI_API_KEY")
# os.environ["OPENAI_MODEL_NAME"]="gpt-4-0125-preview"

quiz_researcher=Agent(
    role='Researches top blogs and interview prep sites',
    goal='Get the relevant information for the topic {topic} from the provided blogs and interview preparation sites.',
    verbose=True,
    memory=True,
    backstory=('Expert in understanding blog posts and interview prep content about the {topic} and extracting relevant information for the interview-based quiz.'),
    tools=[search_tool],
    llm=llm,
    allow_delegation=True,
)

quiz_maker=Agent(
    role='Question/Quiz Maker',
    goal='Extracts compelling information relevant for interview quizzes about the {topic} from blogs and interview prep sites.',
    verbose=True,
    memory=True,
    backstory=(
        "With a flair for simplifying complex topics, you craft"
        "engaging narratives that captivate and educate, bringing new"
        "discoveries to light in an accessible manner."
    ),
    tools=[search_tool],
    llm=llm,
    allow_delegation=False,
)