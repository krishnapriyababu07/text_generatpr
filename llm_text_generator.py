import streamlit as st
import cohere

# Set your Cohere API key here
cohere_api_key = 'rAMg0sxMwWAlpBvJ7LffLSCb8rOAl7OByTv6Vtjm'
co = cohere.Client(cohere_api_key)

# Streamlit interface
st.title("Simple LLM Text Generator")
st.subheader("Powered by Cohere")

# User input
prompt = st.text_area("Enter your text prompt here:", "")

# Parameters for the model
max_tokens = st.slider("Max tokens", 50, 500, 100)
temperature = st.slider("Temperature", 0.0, 1.0, 0.7)

if st.button("Generate Text"):
    if prompt:
        with st.spinner("Generating text..."):
            try:
                # Generate text using the Cohere API
                response = co.generate(
                    model='command-xlarge',  # Update to a valid model ID
                    prompt=prompt,
                    max_tokens=max_tokens,
                    temperature=temperature
                )
                generated_text = response.generations[0].text.strip()
                st.subheader("Generated Text:")
                st.write(generated_text)
            except cohere.error.NotFoundError:
                st.error("Model not found. Please check the model ID.")
            except cohere.error.APIError as e:
                st.error(f"API error: {e.message}")
            except Exception as e:
                st.error(f"An unexpected error occurred: {e}")
    else:
        st.error("Please enter a prompt to generate text.")
