import streamlit as st
import pandas as pd
import plotly.express as px
from wordcloud import WordCloud, STOPWORDS
import matplotlib.pyplot as plt
import string
import nltk
from nltk.corpus import stopwords
from collections import Counter

# Baixar stopwords do NLTK
nltk.download("stopwords")
stop_words = set(stopwords.words("portuguese"))

# Carregar dados
df = pd.read_csv("df_sentimentos.csv")

# Configuração da largura do app
st.set_page_config(layout="wide")

# Título
st.title("Análise de Sentimentos dos Depoimentos")

# Busca de depoimentos
st.subheader("Buscar Depoimentos")
search_query = st.text_input("Digite uma palavra-chave para encontrar nos depoimentos:")
if search_query:
    filtered_df = df[df["depoimento"].str.contains(search_query, case=False, na=False)]
    st.write(filtered_df[["data", "depoimento"]])

# Gráfico de Pizza
st.subheader("Distribuição dos Sentimentos")
sentiment_counts = df["sentimento"].value_counts()
fig_pie = px.pie(
    names=sentiment_counts.index,
    values=sentiment_counts.values,
    title="Proporção de Sentimentos",
    width=900,  # Largura maior
    height=600  # Altura maior
)

st.plotly_chart(fig_pie)

# função para gerar a núvem de palavras
def gerar_wordcloud(depoimentos, titulo, background_color):
    st.subheader(titulo)

    # Concatenar todos os depoimentos em um único texto
    text = " ".join(depoimentos)

    # Remover pontuação e stopwords
    words = text.lower().translate(str.maketrans("", "", string.punctuation)).split()
    filtered_words = [word for word in words if word not in stop_words]

    # Contar a frequência das palavras
    word_counts = Counter(filtered_words)
    
    # Selecionar apenas as 10 palavras mais comuns
    top_words = dict(word_counts.most_common(10))

    # Criar a nuvem de palavras com fundo preto e colormap "cool"
    wordcloud = WordCloud(
        background_color="black",
        colormap=background_color
    ).generate_from_frequencies(top_words)

    # Exibir a nuvem de palavras no Streamlit
    fig, ax = plt.subplots(figsize=(6, 3))
    ax.imshow(wordcloud, interpolation="quadric")
    ax.axis("off")
    st.pyplot(fig)

# Criar duas colunas para exibir as nuvens de palavras lado a lado
col1, col2 = st.columns(2)

with col1:
    gerar_wordcloud(df[df["sentimento"] == "positivo"]["depoimento"].dropna(), "Depoimentos Positivos 😃", 'Greens')

with col2:
    gerar_wordcloud(df[df["sentimento"] == "negativo"]["depoimento"].dropna(), "Depoimentos Negativos 😡", 'autumn')
