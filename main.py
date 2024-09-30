import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Carregue o dataset
df = pd.read_csv('./assets/Unicorn_Companies.csv')

# Visualize as primeiras linhas do dataset
print(df.head())

# Verifique as colunas disponíveis
print(df.columns)

# 1. Empresas unicórnios por país
unicornios_por_pais = df['Country'].value_counts()
plt.figure(figsize=(10, 6))
sns.barplot(y=unicornios_por_pais.index, x=unicornios_por_pais.values, palette='viridis')
plt.title('Número de Empresas Unicórnios por País')
plt.xlabel('Número de Unicórnios')
plt.ylabel('País')
plt.show()

# 2. Setores mais comuns entre unicórnios
setores_mais_comuns = df['Industry'].value_counts().head(10)
plt.figure(figsize=(10, 6))
sns.barplot(y=setores_mais_comuns.index, x=setores_mais_comuns.values, palette='coolwarm')
plt.title('Top 10 Setores das Empresas Unicórnios')
plt.xlabel('Número de Empresas')
plt.ylabel('Setor')
plt.show()

# 3. Valor médio dos unicórnios por setor
valor_medio_setor = df.groupby('Industry')['Valuation ($B)'].mean().sort_values(ascending=False).head(10)
plt.figure(figsize=(10, 6))
sns.barplot(y=valor_medio_setor.index, x=valor_medio_setor.values, palette='magma')
plt.title('Top 10 Setores com Maior Valor Médio das Empresas Unicórnios')
plt.xlabel('Valor Médio (em Bilhões)')
plt.ylabel('Setor')
plt.show()
