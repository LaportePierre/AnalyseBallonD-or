import pandas as pd

# Charger le fichier CSV avec pandas
nom_fichier_csv = 'data/database_ballon_or.csv'  # Remplacez ceci par le nom de votre fichier CSV
df_ballon_or = pd.read_csv(nom_fichier_csv)
nom_fichier_csv = 'data/countries_continent.csv'
df_countries_continent = pd.read_csv(nom_fichier_csv)

def getContinentCount():
    # Créer un dictionnaire pour stocker le score par continent
    scores_continent = {'Africa': 0, 'Asia': 0, 'Europe': 0, 'North America': 0, 'Oceania':0, 'South America': 0}

    # Itérer sur chaque ligne du DataFrame
    for index, row in df_ballon_or.iterrows():
        pays = row['Nationality']  
        continent = None
        i = 0
        while i < len(df_countries_continent) and continent is None:
            if df_countries_continent.loc[i, 'Country'] == pays:
                continent = df_countries_continent.loc[i, 'Continent']
            i += 1

        if continent in scores_continent:
            scores_continent[continent] += 1
        else:
            print(row['Year'])
            print(f"Continent non reconnu pour le pays {pays}: {continent}")

    for continent, score in scores_continent.items():
        print(f"Score pour {continent}: {score}")

print(getContinentCount())