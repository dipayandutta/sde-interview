from core.registry import AgentRegistry
from core.orchestrator import Orechstrator

from agents.addition import AdditionAgent
from agents.subtraction import SubtractionAgent
from agents.multiplication import MultiplicationAgent

def main():
    registry = AgentRegistry()

    registry.register(AdditionAgent())
    registry.register(SubtractionAgent())
    registry.register(MultiplicationAgent())

    orch = Orechstrator(registry)

    print(f"Available Agents: ", registry.list_agents())

    print(f"--------AVAILABLE AGENTS-------")
    for agent in registry.list_agents():
        print(f"{agent}")
    print(f"--------------------------------")
    while True:
        user_input = input("Enter Command : ")
        if user_input.lower() in ["exit","quit"]:
            break

        result = orch.handle(user_input)
        print("Result: ", result)

if __name__ == '__main__':
    main()