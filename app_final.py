import streamlit as st
import boto3
import json

# Replace with your endpoint name
endpoint_name = 'https://runtime.sagemaker.us-east-2.amazonaws.com/endpoints/predictions/invocations'

# Initialize SageMaker Runtime client
runtime_client = boto3.client('sagemaker-runtime', region_name='us-east-2')

# Streamlit app layout
st.title("AWS SageMaker Prediction App")

st.write("Provide the input data for prediction:")

# Input fields
market_open = st.number_input("Market Open Price", value=0.0, step=0.01)
volume = st.number_input("Volume", value=0.0, step=1.0)
high = st.number_input("High Price", value=0.0, step=0.01)
low = st.number_input("Low Price", value=0.0, step=0.01)

# Prediction button
if st.button("Predict"):
    try:
        # Prepare the input data
        input_data = [market_open, volume, high, low]
        payload = json.dumps({"instances": [input_data]})

        # Invoke the endpoint
        response = runtime_client.invoke_endpoint(
            EndpointName=endpoint_name,
            ContentType="application/json",
            Body=payload
        )

        # Parse the response
        result = json.loads(response['Body'].read().decode('utf-8'))
        st.success(f"Prediction: {result}")

    except Exception as e:
        st.error(f"Error occurred: {e}")