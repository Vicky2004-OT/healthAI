from utils.query_engine import query_model


def answer_patient_query(query):
    prompt = f"A patient asked: '{query}'. Provide a medically accurate, clear, and empathetic answer."
    return query_model(prompt)
