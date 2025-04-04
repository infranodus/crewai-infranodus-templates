# Examples of using InfraNodus for CrewAI agent workflows

## Introduction

[crewAI](https://crewai.com) is designed to facilitate the collaboration of role-playing AI agents.
[InfraNodus](https://infranodus.com) is a text network analysis tool that can generate an underlying knowledge graph for any text.

The main speciality of InfraNodus is its ability detect the topical clusters inside any text and then generate a topical gap that identifies which topics should be better connected.

Its advantage to using a standard LLM for this same purpose is that it uses graph theory and network analysis to generate the gaps, which are more objective and less biased than a standard LLM. You also get an additional advantage by getting the underlying graph structure, so it is akin to having a portable GraphRAG on your LLM calls without the need to set up complex infrastructure.

Below we provide some examples of how you can integrate InfraNodus into your CrewAI workflows.

Learn more about these workflows on our support portal: [https://support.noduslabs.com/hc/en-us/articles/19311397123996-InfraNodus-Crew-AI-Enhancing-AI-Agent-Workflows-with-Content-Gap-Detection-Research-Questions](https://support.noduslabs.com/hc/en-us/articles/19311397123996-InfraNodus-Crew-AI-Enhancing-AI-Agent-Workflows-with-Content-Gap-Detection-Research-Questions)

## Examples

- [Gap Analysis](https://github.com/infranodus/crewai-infranodus-templates/tree/master/crewai_gap_analysis) — this workflow is built on top of the default CrewAI workflow that creates an outline of any topic using LLM and then provides InfraNodus as a gap research tool to the researcher agent enabling it to generate a gap analysis report.

  ![CrewAI InfraNodus Gap Analysis Flow](images/crewai-infranodus-gap-finder-diagram.png)

- [Gap Questions](https://github.com/infranodus/crewai-infranodus-templates/tree/master/crewai_gap_questions) — this workflow is built on top of the default CrewAI workflow that creates an outline of any topic using LLM and then provides InfraNodus as a gap research tool to the question generator agent enabling it to generate a research question based on the gap identified and then use another agent to propose how this research could be developed.

  ![CrewAI InfraNodus Question Generator Flow](images/crewai-infranodus-question-diagram.png)

## Installation

Every example has an installation guide that will help you get started. In order to use InfraNodus, you will need to have a valid API key which can be obtained at [https://infranodus.com/api-access](https://infranodus.com/api-access). You need a valid InfraNodus account (any tier) to be able to use the API.

## Support

If you have any questions or need support, please contact [InfraNodus Support](https://support.noduslabs.com).
