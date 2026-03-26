from core.parser import parse_intent
from core.generator import generate_agent_code
from core.loader import load_agent
import time 

class Orechstrator:
    def __init__(self,registry):
        self.registry = registry

    def handle(self,user_input):
        operation, numbers = parse_intent(user_input)
        if not operation:
            return "Could Not understand request"
        agent = self.registry.get(operation)

        if agent:
            return agent.run(*numbers)
        
        print(f"[INFO] Agent '{operation}' not found . Generating the Agent ....")
        time.sleep(5)
        code = generate_agent_code(operation)

        if not code:
            return "Cannot Generate Code"
        
        agent = load_agent(code,self.registry)

        return agent.run(*numbers)