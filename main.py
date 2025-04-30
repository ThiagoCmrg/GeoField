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


# Marcadores das Médias (Instalações)
marker_cluster_eqps = MarkerCluster().add_to(mapa_brasil)
for _, row in tabela_cidades.iterrows():
    codigo_instalacao = row.get('Código', 'Código Indisponível')
    lat_eq = row.get('Coordenadas.Latitude')
    lon_eq = row.get('Coordenadas.Longitude')
    nome_cidade = row.get('Cidade', 'Instalação')

    if pd.notnull(lat_eq) and pd.notnull(lon_eq):
        folium.CircleMarker(
            location=[lat_eq, lon_eq],
            radius=5,
            color='red',
            fill=True,
            fill_color='red',
            fill_opacity=0.7,
            popup=f"Código da Instalação: {codigo_instalacao}",
        ).add_to(marker_cluster_eqps)