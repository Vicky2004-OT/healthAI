import streamlit as st
import os
import requests

# ✅ Load secrets from Streamlit's secrets manager
HF_API_TOKEN = st.secrets["HF_API_TOKEN"]
HF_MODEL_ID = st.secrets["HF_MODEL_ID"]

def query_model(prompt):
    if not HF_API_TOKEN or not HF_MODEL_ID:
        return "❌ Missing Hugging Face credentials or model ID."

    headers = {
        "Authorization": f"Bearer {HF_API_TOKEN}"
    }

    payload = {
        "inputs": prompt,
        "parameters": {
            "max_new_tokens": 300,
            "temperature": 0.7
        }
    }

    try:
        response = requests.post(
            f"https://api-inference.huggingface.co/models/{HF_MODEL_ID}",
            headers=headers,
            json=payload
        )
        if response.ok:
            data = response.json()
            if isinstance(data, list) and 'generated_text' in data[0]:
                return data[0]['generated_text']
            elif isinstance(data, dict) and 'generated_text' in data:
                return data['generated_text']
            else:
                return str(data)
        else:
            return f"❌ API Error: {response.status_code} - {response.text}"
    except Exception as e:
        return f"❌ Exception: {str(e)}"
