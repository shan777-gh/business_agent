import gradio as gr
from langflow import load_flow

# Load your Langflow flow
flow = load_flow("Business agent.json")

# Function to process user messages
def respond(message, history: list[dict[str, str]], system_message):
    # Run Langflow flow with user input
    result = flow.run(inputs={"user_input": message})

    # Get output from Langflow
    response = result["output"]

    return response

# ChatInterface wrapper
chatbot = gr.ChatInterface(
    respond,
    type="messages",
    additional_inputs=[
        gr.Textbox(value="You are a business assistant.", label="System message"),
    ],
)

with gr.Blocks() as demo:
    chatbot.render()

if __name__ == "__main__":
    demo.launch()
