from utils.query_engine import query_model

def generate_treatment_plan(condition, patient_profile=None):
    prompt = f"""
    Condition: {condition}
    Patient profile: {patient_profile or "not provided"}
    
    Suggest a detailed treatment plan including medications, lifestyle modifications, and follow-up actions.
    """
    return query_model(prompt)