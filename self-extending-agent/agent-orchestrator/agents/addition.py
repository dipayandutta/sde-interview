from agents.base import BaseAgent

class AdditionAgent(BaseAgent):
    name = "add"

    def run(self,a,b):
        return a+b