# Importation des bibliothèques nécessaires
import matplotlib.pyplot as plt
import pandas as pd
import io
import numpy as np

# Données complètes pour le nombre de femmes participantes (1992-2016)
data_femmes_str_full = """Année;Japon;France;Allemagne;Russie;États-Unis
1992;100;128;199;208;240
1994;16;30;33;38;52
1996;149;102;187;158;273
1998;64;31;47;43;81
2000;110;125;181;194;253
2002;44;27;69;66;87
2004;167;113;191;202;254
2006;52;32;61;74;87
2008;165;121;183;223;282
2010;43;37;56;81;92
2012;155;142;171;226;268
2014;61;39;75;88;100
2016;164;167;194;142;291
"""

# Lecture des données
df_femmes = pd.read_csv(io.StringIO(data_femmes_str_full), sep=';')

# Création du graphique combiné
plt.figure(figsize=(12, 7))

for pays in ['Japon', 'France', 'Allemagne', 'Russie', 'États-Unis']:
    plt.plot(df_femmes['Année'], df_femmes[pays], marker='o', linestyle='-', label=pays)

plt.title('Évolution du nombre de femmes participantes par pays (1992-2016)', fontsize=16)
plt.xlabel('Année', fontsize=12)
plt.ylabel('Nombre de femmes participantes', fontsize=12)
plt.legend(title='Pays', fontsize=10)
plt.grid(True, linestyle='--', alpha=0.7)
plt.xticks(df_femmes['Année'], rotation=45)
plt.tight_layout()

# Affichage du graphique
plt.show()

# --- Graphiques séparés pour Jeux d'Été et d'Hiver ---
# Identification des années de JO d'été et d'hiver
annees_ete = [1992, 1996, 2000, 2004, 2008, 2012, 2016]
annees_hiver = [1994, 1998, 2002, 2006, 2010, 2014]

df_femmes_ete = df_femmes[df_femmes['Année'].isin(annees_ete)]
df_femmes_hiver = df_femmes[df_femmes['Année'].isin(annees_hiver)]

# Graphique pour les Jeux d'Été
if not df_femmes_ete.empty:
    plt.figure(figsize=(10, 6))
    for pays in ['Japon', 'France', 'Allemagne', 'Russie', 'États-Unis']:
        plt.plot(df_femmes_ete['Année'], df_femmes_ete[pays], marker='s', linestyle='--', label=pays)
    plt.title('Nombre de femmes participantes par pays (Jeux d\'Été 1992-2016)', fontsize=14)
    plt.xlabel('Année', fontsize=12)
    plt.ylabel('Nombre de femmes participantes', fontsize=12)
    plt.legend(title='Pays', fontsize=10)
    plt.grid(True, linestyle='--', alpha=0.6)
    plt.xticks(df_femmes_ete['Année'])
    plt.tight_layout()
    plt.show()

# Graphique pour les Jeux d'Hiver
if not df_femmes_hiver.empty:
    plt.figure(figsize=(10, 6))
    for pays in ['Japon', 'France', 'Allemagne', 'Russie', 'États-Unis']:
        plt.plot(df_femmes_hiver['Année'], df_femmes_hiver[pays], marker='^', linestyle=':', label=pays)
    plt.title('Nombre de femmes participantes par pays (Jeux d\'Hiver 1994-2014)', fontsize=14)
    plt.xlabel('Année', fontsize=12)
    plt.ylabel('Nombre de femmes participantes', fontsize=12)
    plt.legend(title='Pays', fontsize=10)
    plt.grid(True, linestyle='--', alpha=0.6)
    plt.xticks(df_femmes_hiver['Année'])
    plt.tight_layout()
    plt.show()
