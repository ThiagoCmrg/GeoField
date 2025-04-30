import pandas as pd
import folium
from folium.plugins import MarkerCluster

tabela_cidades= pd.read_excel('Caminho_Arquivo.xlsx')  ## Substitua pelo caminho do seu arquivo
tabela_tecnicos= pd.read_excel('Caminho_Arquivo.xlsx')   ## Substitua pelo caminho do seu arquivo


mapa_brasil = folium.Map(location=[-14.2350, -51.9253], zoom_start=3) #Zoom inicial do mapa
# Marcador para Técnicos
for _, row in tabela_tecnicos.iterrows():
    lat_tec = row.get('Latitude_Tecnico')
    lon_tec = row.get('Longitude_Tecnico')
    nome_tec = row.get('Nome', 'Técnico')
    cidade_tec = row.get('Cidade', '')
    estado_tec = row.get('Estado', '')

    lat_tec_corrigida = lat_tec
    lon_tec_corrigida = lon_tec

    if cidade_tec == "Vitória" and estado_tec == "ES":  # Corrigindo coordenadas para Vitória, ES. Pois PowerQuery não reconhece.
        lat_tec_corrigida = -20.32
        lon_tec_corrigida = -40.34

    if pd.notnull(lat_tec_corrigida) and pd.notnull(lon_tec_corrigida):
        folium.Marker(
            location=[lat_tec_corrigida, lon_tec_corrigida],
            popup=f"Técnico: {nome_tec}",
            icon=folium.Icon(color='blue', icon='user', prefix='fa')
        ).add_to(mapa_brasil)