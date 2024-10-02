import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import streamlit as st
import config as cfg


st.markdown(
    """<style>.block-container{max-width: 86rem !important;}</style>""",
    unsafe_allow_html=True,
)


def run_interface():
    st.markdown("## Alura - Introdução à Ciência de Dados")
    st.write("---")

    df = st.session_state.df_rates.copy()

    st.dataframe(df.head())
    st.write(df["nota"].unique())
    st.write(df["nota"].value_counts())
    st.write(df["nota"].median())
    st.write(df["nota"].mean())

    figure = df["nota"].plot(kind="hist").figure
    st.pyplot(figure)

    st.write(df["nota"].describe())

    fig = plt.figure(figsize=(3, 3))

    sns.boxplot(df["nota"])

    st.pyplot(fig, use_container_width=False)


def init_session():
    if "df_rates" not in st.session_state:
        st.session_state.df_rates = pd.read_csv(cfg.URL_RATINGS)
        st.session_state.df_rates.columns = ["uruarioId", "filmeId", "nota", "momento"]


def main():
    init_session()
    run_interface()


if __name__ == "__main__":
    main()
