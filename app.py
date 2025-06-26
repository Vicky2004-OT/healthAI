import streamlit as st
from utils.chat_handler import answer_patient_query
from utils.disease_predictor import predict_disease
from utils.treatment_planner import generate_treatment_plan
from utils.analytics import display_health_analytics


# ===== UI Components =====

def display_patient_chat():
    st.subheader("💬 Patient Chat")
    query = st.text_input("Ask a health-related question:")
    if st.button("Get Answer", key="chat"):
        response = answer_patient_query(query)
        st.write("🧠 AI Response:", response)

def display_disease_prediction():
    st.subheader("🩺 Disease Prediction")
    symptoms = st.text_area("Enter your symptoms (comma-separated):")
    if st.button("Predict Disease", key="predict"):
        result = predict_disease(symptoms)
        st.write("🧠 Prediction Result:", result)

def display_treatment_plans():
    st.subheader("📝 Treatment Plan Generator")
    disease = st.text_input("Enter your diagnosed disease:")
    if st.button("Generate Plan", key="treatment"):
        plan = generate_treatment_plan(disease)
        st.write("🧠 Suggested Treatment Plan:", plan)

# ===== Main App Entry Point =====

def main():
    st.set_page_config(page_title="HealthAI - Intelligent Healthcare Assistant", layout="wide")
    st.title("🧠 HealthAI - Intelligent Healthcare Assistant")
    st.markdown("Get AI-powered support for medical queries, symptom analysis, and health tracking.")

    st.sidebar.title("📌 Navigation")
    options = ["Patient Chat", "Disease Prediction", "Treatment Plans", "Health Analytics"]
    choice = st.sidebar.radio("Go to", options)

    if choice == "Patient Chat":
        display_patient_chat()
    elif choice == "Disease Prediction":
        display_disease_prediction()
    elif choice == "Treatment Plans":
        display_treatment_plans()
    elif choice == "Health Analytics":
        display_health_analytics()

# ===== Run the App =====

if __name__ == "__main__":
    main()