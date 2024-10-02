import pandas as pd

url_ratings = "https://raw.githubusercontent.com/alura-cursos/data-science-analise-exploratoria/main/Aula_0/ml-latest-small/ratings.csv"

df = pd.read_csv(url_ratings)

df.shape

df.columns = ["uruarioId", "filmeId", "nota", "momento"]
df.head()

df["nota"].unique()

df["nota"].value_counts()

df["nota"].median()
df["nota"].mean()
