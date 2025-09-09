import gradio as gr
from langflow.load import run_flow_from_json

# Run the Langflow JSON flow
def run_agent(message, history: list[dict[str, str]], system_message):
    # Feed user input into the flow
    result = run_flow_from_json(
        "Business agent.json",
        inputs={"user_input": message}
    )
    # Get the response from the flow output
    return result["output"]

# Gradio ChatInterface
chatbot = gr.ChatInterface(
    fn=run_agent,
    type="messages",
    additional_inputs=[
        gr.Textbox(value="You are a business assistant.", label="System message"),
    ],
)

with gr.Blocks() as demo:
    chatbot.render()

if __name__ == "__main__":
    demo.launch()
