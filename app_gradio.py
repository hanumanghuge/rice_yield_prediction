import gradio as gr
from src.prediction import predict_rice_packets

def predict(land_size):
    packets = predict_rice_packets(land_size)
    return f"Predicted Rice Packets: {packets}"

demo = gr.Interface(
    fn=predict,
    inputs=gr.Number(label="Land size (acres)", value=3.5),
    outputs=gr.Textbox(label="Result"),
    title="Rice Yield Prediction",
    description="Simple Linear Regression: predict rice packets from land size.",
)

if __name__ == "__main__":
    demo.launch()
