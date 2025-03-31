import datetime
import json
import os
from typing import Any, Optional, Type

import requests
from pydantic import BaseModel, Field

from crewai_tools import BaseTool


def _save_results_to_file(content: str) -> None:
    """Saves the search results to a file."""
    filename = f"infranodus_question_generator_{datetime.datetime.now().strftime('%Y-%m-%d_%H-%M-%S')}.txt"
    with open(filename, "w") as file:
        file.write(content)
    print(f"Results saved to {filename}")


class InfranodusQuestionGeneratorToolSchema(BaseModel):
    """Input for InfranodusQuestionGeneratorTool."""

    text: str = Field(
        ..., description="Mandatory text you want to analyze using this tool."
    )


class InfranodusQuestionGeneratorTool(BaseTool):
    name: str = "Infranodus Question Generator"
    description: str = (
        "A tool that can be used to generate research questions from text."
    )
    args_schema: Type[BaseModel] = InfranodusQuestionGeneratorToolSchema

    # remove gapDepth from the URL below to generate a random gap
    # by default gapDepth=0 finds the gap with the furthest distance in the knowledge graph

    search_url: str = "https://infranodus.com/api/v1/graphAndAdvice?doNotSave=true&addStats=true&optimize=gap&includeGraph=false&includeGraphSummary=true&gapDepth=0"
    save_file: bool = False

    def _run(
        self,
        **kwargs: Any,
    ) -> Any:

        text = kwargs.get("text") # or kwargs.get("query")

          
        # If text is not provided in kwargs, check if it's in the schema
        if not text and hasattr(self.args_schema, 'text'):
            # This is a fallback if text wasn't passed directly
            text = getattr(self.args_schema, 'text', None)
           
        save_file = kwargs.get("save_file", self.save_file)

        payload = {"name": 'random_text_name', "text": text, "aiTopics": True, "modelToUse": "gpt-4", "requestMode": "question"}


        payload = json.dumps(payload)

        headers = {
            "Authorization": f"Bearer {os.environ['INFRANODUS_API_KEY']}",
            "content-type": "application/json",
        }

        response = requests.request(
            "POST", self.search_url, headers=headers, data=payload
        )
        results = response.json()

        if "aiAdvice" in results:
            advice_texts = []
            for advice in results["aiAdvice"]:
                if "text" in advice:
                    advice_texts.append(advice["text"])
            
            combined_text = "\n---\n".join(advice_texts)
                
            final_output = f"\nGap questions:\n\n{combined_text}\n\n"

            if "graphSummary" in results:
                final_output += f"\nGraph summary:\n\n{results['graphSummary']}\n\n"

            if save_file:
                _save_results_to_file(final_output)
                
            return final_output
        else:
            return results
