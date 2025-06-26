import pandas as pd
import plotly.express as px
import streamlit as st

def display_health_analytics():
    st.subheader("📊 Health Analytics")
    file = st.file_uploader("health_metrics_large", type=["csv"])
    
    if file:
        try:
            df = pd.read_csv(file)
            st.write("Preview of Data:", df.head())

            numeric_cols = df.select_dtypes(include=["int64", "float64"]).columns
            if len(numeric_cols) == 0:
                st.warning("No numeric columns to plot.")
                return

            metric = st.selectbox("Select metric to plot:", numeric_cols)
            fig = px.line(df, y=metric, title=f"{metric} over time")
            st.plotly_chart(fig)

            st.info("🧠 Example Insight: Health metric looks stable. Continue regular checkups.")
        except Exception as e:
            st.error(f"Error reading file: {e}")