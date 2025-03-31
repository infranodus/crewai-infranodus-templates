# GapQuestions Crew

Welcome to the GapQuestions Crew project, powered by [crewAI](https://crewai.com) and [InfraNodus](https://infranodus.com). This template is designed to help you set up a multi-agent AI system with ease, leveraging the powerful and flexible framework provided by crewAI. Our goal is to enable your agents to collaborate effectively on complex tasks, maximizing their collective intelligence and capabilities.

## Installation

Ensure you have Python >=3.10 <=3.13 installed on your system. This project uses [UV](https://docs.astral.sh/uv/) for dependency management and package handling, offering a seamless setup and execution experience.

Python 3.11 is recommended.

If there's an error with this installation, try the instructions at [https://docs.crewai.com/installation](https://docs.crewai.com/installation). Do not use the instructions from the CrewAI main repo README.md file

First, if you haven't already, install uv:

```bash
pip install uv
```

Next, navigate to your project directory and install the dependencies:

1. First lock the dependencies and then install them:

```bash
uv lock
```

```bash
uv sync
```

### Customizing

Rename `.env.sample` to `.env` and add your keys there:

**Add your `OPENAI_API_KEY` into the `.env` file**
**Add your `SERPER_API_KEY` into the `.env` file**
**Add your `INFRANODUS_API_KEY` into the `.env` file** (can be obtained at [https://infranodus.com/api-access](https://infranodus.com/api-access))

- Modify `src/gap_questions_template/config/agents.yaml` to define your agents
- Modify `src/gap_questions_template/config/tasks.yaml` to define your tasks
- Modify `src/gap_questions_template/crew.py` to add your own logic, tools and specific args
- Modify `src/gap_questions_template/main.py` to add custom inputs for your agents and tasks

## Set the topic to analyze

**Modify `src/gap_questions_template/main.py` to set the topic to analyze**

```python
inputs = {
    "topic": "your topic here",
    "current_year": 2025,
}
```

## Running the Project

To kickstart your crew of AI agents and begin task execution, run this from the root folder of your project:

```bash
$ crewai run
```

or

```bash
uv run gap_questions_template
```

This command initializes the gap-questions-template Crew, assembling the agents and assigning them tasks as defined in your configuration.

This example, unmodified, will run the create a `report_today_date.md` file with the output of a research on LLMs in the root folder.

## Understanding Gap Questions Template Crew

The gap-questions-template Crew is composed of multiple AI agents, each with unique roles, goals, and tools. These agents collaborate on a series of tasks, defined in `config/tasks.yaml`, leveraging their collective skills to achieve complex objectives. The `config/agents.yaml` file outlines the capabilities and configurations of each agent in your crew.

In general, the first agent uses AI to generate a list of relevant information about the topic you provide in the `main.py` file.

The second agent then generates an InfraNodus knowledge graph from this topic and then uses the graph to generate a research question based on this gap. Read more about it at [https://infranodus.com](https://infranodus.com).

The third agent then uses the question to generate a report for how this gap can be developed further.

## Support

For support, questions, or feedback regarding the GapAnalysis Crew or crewAI.

- Contact Nodus Labs support and read InfraNodus docs at [support.noduslabs.com](https://support.noduslabs.com)
- Visit Crew AI [documentation](https://docs.crewai.com)
- [Chat with Crew AI docs](https://chatg.pt/DWjSBZn)

Let's create wonders together with the power and simplicity of crewAI.
