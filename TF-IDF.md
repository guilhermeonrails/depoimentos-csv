# O que é TF-IDF?  

O **TF-IDF (Term Frequency - Inverse Document Frequency)** é uma técnica utilizada para avaliar a importância de uma palavra dentro de um conjunto de textos (corpus). Ele combina dois fatores:  

## 1. TF (Term Frequency) – Frequência do termo no documento  
Mede quantas vezes um termo aparece dentro de um documento em relação ao total de palavras no documento.  

A fórmula é:  

$$
TF(t) = \frac{\text{Número de vezes que a palavra } t \text{ aparece no documento}}{\text{Total de palavras no documento}}
$$

**Exemplo:**  
Se a palavra *"trem"* aparece 3 vezes em um texto de 100 palavras, então:  

$$
TF(\text{"trem"}) = \frac{3}{100} = 0.03
$$  

## 2. IDF (Inverse Document Frequency) – Frequência inversa do documento  
Mede o quão rara ou comum uma palavra é dentro de um conjunto de documentos.  

A fórmula é:  

$$
IDF(t) = \log \left( \frac{N}{n_t} \right)
$$  

Onde:  
- \( N \) = Total de documentos no corpus  
- \( n_t \) = Número de documentos que contêm a palavra \( t \)  

**Exemplo:**  
Se a palavra *"trem"* aparece em apenas 1 de 10 documentos:  

$$
IDF(\text{"trem"}) = \log \left( \frac{10}{1} \right) = \log(10) = 1
$$  

## 3. Cálculo do TF-IDF  
O TF-IDF é simplesmente o produto de TF e IDF:  

$$
TF-IDF(t) = TF(t) \times IDF(t)
$$  

**Exemplo:**  
Considerando os valores anteriores:  

$$
TF-IDF(\text{"trem"}) = 0.03 \times 1 = 0.03
$$  

Ou seja, quanto maior o valor de TF-IDF, mais relevante a palavra é dentro do documento em comparação ao restante do corpus.  

---

Esse conceito é muito utilizado em **Machine Learning**, **Processamento de Linguagem Natural (NLP)** e sistemas de **busca** para determinar palavras importantes dentro de textos. 🚀
