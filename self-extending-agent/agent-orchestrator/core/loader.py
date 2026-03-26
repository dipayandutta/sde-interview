from agents.base import BaseAgent

def load_agent(code,registry):
    local_scope = {}

    exec(code,globals(),local_scope)

    for obj in local_scope.values():
        if isinstance(obj,type) and issubclass(obj,BaseAgent):
            if obj is BaseAgent:
                continue
            agent = obj()
            registry.register(agent)
            return agent 