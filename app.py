from langflow import load_flow

flow = load_flow("Business agent.json")

def run_agent(user_input):
    result = flow.run(inputs={"user_input": user_input})
    return result["output"]
