from crewai import Crew, Process
from agents import quiz_maker, quiz_researcher
from tasks import research_task, write_task

crew = Crew(
    agents=[quiz_researcher, quiz_maker],
    tasks=[research_task, write_task],
    process=Process.sequential,
    max_rpm=15,
)

def run(inputs):
    """Run the crew."""
    result=crew.kickoff(inputs=inputs)
    print(result)