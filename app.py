import streamlit as st
import pandas as pd
import plotly.express as px
from wordcloud import WordCloud, STOPWORDS
import matplotlib.pyplot as plt

# Carregar dados
df = pd.read_csv("df_sentimentos.csv")

# Título
st.title("Análise de Sentimentos dos Depoimentos")

# Gráfico de Pizza
st.subheader("Distribuição dos Sentimentos")
sentiment_counts = df["sentimento"].value_counts()
fig_pie = px.pie(names=sentiment_counts.index, values=sentiment_counts.values, title="Proporção de Sentimentos")
st.plotly_chart(fig_pie)

# Últimos 3 depoimentos
st.subheader("Últimos 3 Depoimentos")
for _, row in df.tail(3).iterrows():
    st.write(f"**{row['data']}** - {row['depoimento']}")

# WordCloud
st.subheader("Nuvem de Palavras dos Depoimentos")
stopwords = set(STOPWORDS)
text = " ".join(df["depoimento"].dropna())
wordcloud = WordCloud(stopwords=stopwords, background_color="white", width=1000, height=400).generate(text)
fig, ax = plt.subplots()
ax.imshow(wordcloud, interpolation="bilinear")
ax.axis("off")
st.pyplot(fig)

# Busca de depoimentos
st.subheader("Buscar Depoimentos")
search_query = st.text_input("Digite uma palavra-chave:")
if search_query:
    filtered_df = df[df["depoimento"].str.contains(search_query, case=False, na=False)]
    st.write(filtered_df[["data", "depoimento"]])
