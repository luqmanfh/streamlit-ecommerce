import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# judul aplikasi
st.title("Analisis Data E-Commerce")

# membaca dataset
uploaded_file = st.file_uploader("Upload Dataset (CSV)", type=["csv"])
if uploaded_file is not None:
    data = pd.read_csv(uploaded_file)

    # preview dataset
    st.write("Dataset:")
    st.write(data.head())

    # pilih kolom untuk visualisasi
    col1 = st.selectbox("Pilih Kolom Kategori", data.columns)
    col2 = st.selectbox("Pilih Kolom Nilai", data.columns)

    # visualisasi data
    if st.button("Buat Grafik"):
        plt.figure(figsize=(10, 6))
        sns.barplot(x=col2, y=col1, data=data)
        plt.title("Visualisasi Data")
        plt.xlabel(col2)
        plt.ylabel(col1)
        st.pyplot(plt)
