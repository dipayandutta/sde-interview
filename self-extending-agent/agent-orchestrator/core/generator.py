def generate_agent_code(operation):
    if operation == "divide":
        return '''
from agents.base import BaseAgent

class DivideAgent(BaseAgent):
    name = "divide"

    def run(self,a,b):
        if b == 0:
            return "Error: Not Able to divide by Zero"
        else:
            return a/b
        '''
    return None 