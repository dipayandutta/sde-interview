from agents.base import BaseAgent

class MultiplicationAgent(BaseAgent):
    name = "multiply"

    def run(self,a,b):
        return a*b