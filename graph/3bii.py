# Importation des bibliothèques nécessaires
import matplotlib.pyplot as plt
import pandas as pd
import io
import numpy as np

# Données complètes pour le nombre de médaillés (1992-2016)
data_medailles_str_full = """Année;Japon;France;Allemagne;Russie;États-Unis
1992;56;68;205;235;197
1994;9;10;31;28;15
1996;42;45;108;97;227
1998;9;15;33;45;33
2000;41;61;106;168;213
2002;2;14;47;35;80
2004;84;48;139;177;214
2006;1;13;38;35;46
2008;48;70;92;134;263
2010;7;11;43;22;84
2012;76;74;87;129;201
2014;10;16;28;49;60
2016;57;93;150;103;211
"""

# Lecture des données
df_medailles = pd.read_csv(io.StringIO(data_medailles_str_full), sep=';')

# --- Graphique combiné (similaire au précédent) ---
plt.figure(figsize=(12, 7))
for pays in ['Japon', 'France', 'Allemagne', 'Russie', 'États-Unis']:
    plt.plot(df_medailles['Année'], df_medailles[pays], marker='o', linestyle='-', label=pays)

plt.title('Évolution du nombre de médaillés par pays (1992-2016) - Combiné', fontsize=16)
plt.xlabel('Année', fontsize=12)
plt.ylabel('Nombre de médaillés', fontsize=12)
plt.legend(title='Pays', fontsize=10)
plt.grid(True, linestyle='--', alpha=0.7)
plt.xticks(df_medailles['Année'], rotation=45)
plt.tight_layout()
plt.show()

# --- Graphiques séparés pour Jeux d'Été et d'Hiver ---
# Identification des années de JO d'été et d'hiver
annees_ete = [1992, 1996, 2000, 2004, 2008, 2012, 2016]
annees_hiver = [1994, 1998, 2002, 2006, 2010, 2014]

df_medailles_ete = df_medailles[df_medailles['Année'].isin(annees_ete)]
df_medailles_hiver = df_medailles[df_medailles['Année'].isin(annees_hiver)]

# Graphique pour les Jeux d'Été
if not df_medailles_ete.empty:
    plt.figure(figsize=(10, 6))
    for pays in ['Japon', 'France', 'Allemagne', 'Russie', 'États-Unis']:
        plt.plot(df_medailles_ete['Année'], df_medailles_ete[pays], marker='s', linestyle='--', label=pays) # 's' pour carré
    plt.title('Nombre de médaillés par pays (Jeux d\'Été 1992-2016)', fontsize=14)
    plt.xlabel('Année', fontsize=12)
    plt.ylabel('Nombre de médaillés', fontsize=12)
    plt.legend(title='Pays', fontsize=10)
    plt.grid(True, linestyle='--', alpha=0.6)
    plt.xticks(df_medailles_ete['Année'])
    plt.tight_layout()
    plt.show()
else:
    print("Aucune donnée pour les Jeux d'Été dans la plage spécifiée.")

# Graphique pour les Jeux d'Hiver
if not df_medailles_hiver.empty:
    plt.figure(figsize=(10, 6))
    for pays in ['Japon', 'France', 'Allemagne', 'Russie', 'États-Unis']:
        plt.plot(df_medailles_hiver['Année'], df_medailles_hiver[pays], marker='^', linestyle=':', label=pays) # '^' pour triangle
    plt.title('Nombre de médaillés par pays (Jeux d\'Hiver 1994-2014)', fontsize=14)
    plt.xlabel('Année', fontsize=12)
    plt.ylabel('Nombre de médaillés', fontsize=12)
    plt.legend(title='Pays', fontsize=10)
    plt.grid(True, linestyle='--', alpha=0.6)
    plt.xticks(df_medailles_hiver['Année'])
    plt.tight_layout()
    plt.show()
else:
    print("Aucune donnée pour les Jeux d'Hiver dans la plage spécifiée.")