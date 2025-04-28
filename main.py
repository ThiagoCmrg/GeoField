import pandas as pd
import folium
from folium.plugins import MarkerCluster

tabela_cidades= pd.read_excel('Caminho_Arquivo.xlsx')  ## Substitua pelo caminho do seu arquivo
tabela_tecnicos= pd.read_excel('Caminho_Arquivo.xlsx')   ## Substitua pelo caminho do seu arquivo

print(tabela_cidades)
print(tabela_tecnicos)