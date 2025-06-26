from utils.query_engine import query_model

def predict_disease(symptoms, patient_profile=None):
    prompt = f"""
    Symptoms reported: {symptoms}.
    Patient profile: {patient_profile or "not provided"}.
    
    Predict possible diseases or conditions with confidence levels.
    """
    return query_model(prompt)