import pandas as pd

nom_fichier_csv = 'data/nominees.csv'  # Remplacez ceci par le nom de votre fichier CSV
df_ballon_or = pd.read_csv(nom_fichier_csv)

# Charger le fichier CSV avec pandas
def correct_country_and_club():
    for index, row in df_ballon_or.iterrows():
        année = row['Year']
        if année >= 2019 or année == 1971 or année == 2008 or année == 2002 or année == 1991 or année == 1973:
            df_ballon_or.at[index, 'Nationality'], df_ballon_or.at[index, 'Club'] = (
                df_ballon_or.at[index, 'Club'],
                df_ballon_or.at[index, 'Nationality']
            )
    df_ballon_or.to_csv('data/database_ballon_or.csv', index=False)

#print("correct_country_and_club : Start")
#correct_country_and_club()
#print("correct_country_and_club : Ended")