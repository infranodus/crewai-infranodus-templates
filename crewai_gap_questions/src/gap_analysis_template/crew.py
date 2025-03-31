from crewai_tools import ScrapeWebsiteTool, SerperDevTool

from crewai import Agent, Crew, Process, Task
from crewai.project import CrewBase, agent, crew, task

import datetime

from .tools.infranodus_gap_finder_tool import InfranodusGapFinderTool

@CrewBase
class GapAnalysisTemplateCrew:
    """GapAnalysisTemplate crew"""

  # Learn more about YAML configuration files here:
    # Agents: https://docs.crewai.com/concepts/agents#yaml-configuration-recommended
    # Tasks: https://docs.crewai.com/concepts/tasks#yaml-configuration-recommended
  
    agents_config = "config/agents.yaml"
    tasks_config = "config/tasks.yaml"

    # If you would like to add tools to your agents, you can learn more about it here:
    # https://docs.crewai.com/concepts/agents#agent-tools
    @agent
    def researcher(self) -> Agent:
        return Agent(
            config=self.agents_config['researcher'],
            verbose=True
        )

    @agent
    def gap_finder(self) -> Agent:
        return Agent(
            config=self.agents_config['gap_finder'],
            tools=[InfranodusGapFinderTool(save_file=True)],
            verbose=True
        )

    @agent
    def reporting_analyst(self) -> Agent:
        return Agent(
            config=self.agents_config['reporting_analyst'],
            verbose=True
        )

    # Example of an agent that uses specific tools with no delegation allowed

    # @agent
    # def company_analyst(self) -> Agent:
    #     return Agent(
    #         config=self.agents_config["company_analyst"],
    #         tools=[SerperDevTool(), ScrapeWebsiteTool()],
    #         allow_delegation=False,
    #         verbose=True,
    #     )


    # To learn more about structured task outputs,
    # task dependencies, and task callbacks, check out the documentation:
    # https://docs.crewai.com/concepts/tasks#overview-of-a-task

    @task
    def research_task(self) -> Task:
        return Task(
            config=self.tasks_config['research_task'],
        )

    @task
    def gap_finder_task(self) -> Task:
        return Task(
            config=self.tasks_config['gap_finder_task'],
            agent=self.gap_finder()
        )


    @task
    def reporting_task(self) -> Task:
        return Task(
            config=self.tasks_config['reporting_task'],
            output_file=f'report_{datetime.datetime.now().strftime("%Y-%m-%d_%H-%M-%S")}.md'
        )


   # Example of a task that can only be assigned to a specific agent

    # @task
    # def analyze_target_company_task(self) -> Task:
    #     return Task(
    #         config=self.tasks_config["analyze_target_company_task"],
    #         agent=self.company_analyst(),
    #     )



    @crew
    def crew(self) -> Crew:
        """Creates the SimilarCompanyFinderTemplate crew"""
        return Crew(
            agents=self.agents,  # Automatically created by the @agent decorator
            tasks=self.tasks,  # Automatically created by the @task decorator
            process=Process.sequential,
            verbose=True,
            # process=Process.hierarchical, # In case you wanna use that instead https://docs.crewai.com/how-to/Hierarchical/
        )
