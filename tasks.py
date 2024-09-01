from crewai import Task
from tools import search_tool
from agents import quiz_maker, quiz_researcher

## Research Task
research_task = Task(
  description=(
    "Identify the top blogs and interview preparation sites related to the topic {topic}."
    "Get top 5 blogs and detailed information from each site."
  ),
  expected_output='A comprehensive 3 paragraphs long report based on the {topic} of blog and interview prep content. The information must be relevant to interviews happening in 2024.',
  tools=[search_tool],
  agent=quiz_researcher,
)

# Writing task with language model configuration
write_task = Task(
  description=(
     "Get the info from the top blogs and interview preparation sites on the topic {topic}."
  ),
  expected_output='Summarize the info from the blogs and interview prep sites on the topic {topic} and create the content for the quiz. Make 20 questions with answers and explanations and relevant links to learn more.',
  tools=[search_tool],
  agent=quiz_maker,
  async_execution=False,
  output_file='quiz.md',
)