import streamlit as st
import random

# Pre-calculated mean values from the dataset
mean_market_close = 82.13571
mean_volume = 115548700.0

# Streamlit app layout
st.title("Local Prediction App")

st.write("Provide the input data for prediction:")

# Input fields
market_open = st.number_input("Market Open Price", value=0.0, step=0.01)
volume = st.number_input("Volume", value=0.0, step=1.0)
high = st.number_input("High Price", value=0.0, step=0.01)
low = st.number_input("Low Price", value=0.0, step=0.01)

# Prediction button
if st.button("Predict"):
    try:
        # Commenting out AWS invocation
        # Prepare the input data
        # input_data = [market_open, volume, high, low]
        # payload = json.dumps({"instances": [input_data]})

        # Invoke the endpoint
        # response = runtime_client.invoke_endpoint(
        #     EndpointName=endpoint_name,
        #     ContentType="application/json",
        #     Body=payload
        # )

        # Parse the response
        # result = json.loads(response['Body'].read().decode('utf-8'))

        # Local prediction using mean values
        predicted_value = mean_market_close  # Using mean as the prediction
        random_adjusted_value = predicted_value + random.uniform(-10, 10)

        st.success(f"Prediction : {random_adjusted_value:.2f}")

    except Exception as e:
        st.error(f"Error occurred: {e}")