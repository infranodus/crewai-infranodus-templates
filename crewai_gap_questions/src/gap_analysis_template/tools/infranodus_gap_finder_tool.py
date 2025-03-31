import datetime
import json
import os
from typing import Any, Optional, Type

import requests
from pydantic import BaseModel, Field

from crewai_tools import BaseTool


def _save_results_to_file(content: str) -> None:
    """Saves the search results to a file."""
    filename = f"infranodus_graph_gap_{datetime.datetime.now().strftime('%Y-%m-%d_%H-%M-%S')}.txt"
    with open(filename, "w") as file:
        file.write(content)
    print(f"Results saved to {filename}")


class InfranodusGapFinderToolSchema(BaseModel):
    """Input for InfranodusGapFinderTool."""

    text: str = Field(
        ..., description="Mandatory text you want to analyze using this tool."
    )


class InfranodusGapFinderTool(BaseTool):
    name: str = "Infranodus Gap Finder"
    description: str = (
        "A tool that can be used to identify content gaps in a text based on the underlying knowledge graph."
    )
    args_schema: Type[BaseModel] = InfranodusGapFinderToolSchema

    # remove gapDepth from the URL below to generate a random gap
    # by default gapDepth=0 finds the gap with the furthest distance in the knowledge graph

    search_url: str = "https://infranodus.com/api/v1/dotGraphFromText?doNotSave=true&addStats=true&optimize=gap&includeGraph=false&includeGraphSummary=true&gapDepth=0"
    save_file: bool = False

    def _run(
        self,
        **kwargs: Any,
    ) -> Any:

        text = kwargs.get("text") # or kwargs.get("query")
        save_file = kwargs.get("save_file", self.save_file)

        # if you remove text and provide an existing infranodus graph name in the "name" field instead
        # you will generate the gap from the graph and combine it with the previous agent's output
        # this can be interesting for cross-disciplinary research    

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

        cluster_info = "Topical gap found between these topics:\n"
    
        if "clusterAiNames" in results and "dotGraphByCluster" in results:
            cluster_names = results["clusterAiNames"]
            cluster_ids = results["clusterIds"]
            dot_graphs = results["dotGraphByCluster"]
            
            # Combine cluster names with their corresponding graphs
            cluster_sections = []
            for i, cluster_name in enumerate(cluster_names):
                cluster_section = f"Topic {cluster_name}: ("
                
                # Add the dot graph for this cluster if available
                cluster_id = cluster_ids[i]
                if str(cluster_id) in dot_graphs:
                    graph_lines = dot_graphs[str(cluster_id)]
                    graph_text = ", ".join(graph_lines)
                    cluster_section += f"{graph_text})"
                
                cluster_sections.append(cluster_section)
                
            # Add inter-cluster connections if available
            if "inter_cluster" in dot_graphs and dot_graphs["inter_cluster"]:
                inter_cluster_text = ", ".join(dot_graphs["inter_cluster"])
                cluster_sections.append(f"Gap bridges: {inter_cluster_text}")
            
            cluster_info += "\nand\n".join(cluster_sections) 
            

            if save_file:
                _save_results_to_file(cluster_info)
                
            return cluster_info
        else:
            return results
