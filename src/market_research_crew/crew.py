from crewai import Agent, Crew, Process, Task
from crewai.project import CrewBase, agent, crew, task
from crewai.agents.agent_builder.base_agent import BaseAgent
from crewai_tools import SerperDevTool, ScrapeWebsiteTool, SeleniumScrapingTool
from dotenv import load_dotenv

load_dotenv()

# ========== TOOLS ============
web_search_tool = SerperDevTool()
web_scraping_tool = ScrapeWebsiteTool()
selenium_scraping_tool = SeleniumScrapingTool()

toolkit = [web_search_tool, web_scraping_tool, selenium_scraping_tool]

@CrewBase
class MarketResearchCrew():
    """MarketResearchCrew crew"""

    agents: list[BaseAgent]
    tasks: list[Task]

    # 1. Provide the path for configuration files
    agents_config = "config/agents.yaml"
    tasks_config = "config/tasks.yaml"
    
    # ========================== Agents ==========================
    
    @agent
    def market_research_specialist(self) -> Agent:
        return Agent(
            config=self.agents_config["market_research_specialist"],  # type: ignore[index]
            tools=toolkit
        )
        
    @agent
    def competitive_intelligence_analyst(self) -> Agent:
        return Agent(
            config=self.agents_config["competitive_intelligence_analyst"],  # type: ignore[index]
            tools=toolkit
        )
        
    @agent
    def customer_insights_researcher(self) -> Agent:
        return Agent(
            config=self.agents_config["customer_insights_researcher"],  # type: ignore[index]
            tools=toolkit
        )
        
    @agent
    def product_strategy_advisor(self) -> Agent:
        return Agent(
            config=self.agents_config["product_strategy_advisor"],  # type: ignore[index]
            tools=toolkit
        )
        
    @agent
    def business_analyst(self) -> Agent:
        return Agent(
            config=self.agents_config["business_analyst"],  # type: ignore[index]
            tools=toolkit
        )
        
        
    # ========================== Tasks ==========================
    
    @task
    def market_research_task(self) -> Task:
        return Task(
            config=self.tasks_config["market_research_task"],  # type: ignore[index]
        )
        
    @task
    def competitive_intelligence_task(self) -> Task:
        return Task(
            config=self.tasks_config["competitive_intelligence_task"],  # type: ignore[index]
            context=[self.market_research_task()],
        )
        
    @task
    def customer_insights_task(self) -> Task:
        return Task(
            config=self.tasks_config["customer_insights_task"],  # type: ignore[index]
            context=[self.market_research_task(), self.competitive_intelligence_task()],
        )
        
    @task
    def product_strategy_task(self) -> Task:
        return Task(
            config=self.tasks_config["product_strategy_task"],  # type: ignore[index]
            context=[self.market_research_task(), self.competitive_intelligence_task(), self.customer_insights_task()],
        )
        
    @task
    def business_analyst_task(self) -> Task:
        return Task(
            config=self.tasks_config["business_analyst_task"],  # type: ignore[index]
            context=[self.market_research_task(),
                     self.competitive_intelligence_task(),
                     self.customer_insights_task(),
                     self.product_strategy_task()],
            output_file="reports/report.md"
        )
    
        
    @crew
    def crew(self) -> Crew:
        """Creates the MarketResearchCrew crew"""
        # To learn how to add knowledge sources to your crew, check out the documentation:
        # https://docs.crewai.com/concepts/knowledge#what-is-knowledge

        return Crew(
            agents=self.agents, # Automatically created by the @agent decorator
            tasks=self.tasks, # Automatically created by the @task decorator
            process=Process.sequential,
            verbose=True,
            # process=Process.hierarchical, # In case you wanna use that instead https://docs.crewai.com/how-to/Hierarchical/
        )
