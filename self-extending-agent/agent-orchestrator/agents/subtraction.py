from agents.base import BaseAgent


class SubtractionAgent(BaseAgent):
    name = "subtract"

    def run(self,a,b):
        return a - b