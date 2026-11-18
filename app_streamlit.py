import streamlit as st
from src.prediction import predict_rice_packets

st.set_page_config(page_title="Rice Yield Prediction", page_icon="🌾")

st.title("🌾 Rice Yield Prediction")
st.write("Simple Linear Regression: predict rice packets from land size.")

land_size = st.number_input(
    "Land size (acres)",
    min_value=0.1,
    max_value=100.0,
    value=3.5,
    step=0.5,
)

if st.button("Predict"):
    packets = predict_rice_packets(land_size)
    st.success(f"Predicted Rice Packets: {packets}")
