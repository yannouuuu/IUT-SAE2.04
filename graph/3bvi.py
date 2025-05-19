# Importation des bibliothèques nécessaires
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import io

# Données complètes pour la proportion des femmes parmi les médaillés (1992-2016)
data_femmes_parmi_medailles_str_full = """Année;Japon;France;Allemagne;Russie;États-Unis
1992;0.20;0.19;0.40;0.41;0.45
1994;0.11;0.40;0.35;0.57;0.60
1996;0.38;0.33;0.33;0.29;0.47
1998;0.22;0.20;0.48;0.29;0.79
2000;0.88;0.20;0.50;0.47;0.52
2002;0.50;0.43;0.43;0.23;0.38
2004;0.44;0.38;0.49;0.46;0.58
2006;1.00;0.38;0.53;0.51;0.63
2008;0.56;0.14;0.43;0.57;0.51
2010;0.57;0.55;0.49;0.36;0.42
2012;0.66;0.39;0.28;0.49;0.67
2014;0.20;0.19;0.43;0.37;0.63
2016;0.47;0.30;0.42;0.72;0.55
"""
# Note: La valeur de 1.00 pour le Japon en 2006 est notable.
# Cela signifie que 100% des médaillés japonais cette année-là étaient des femmes.

# Remplacer la virgule par un point pour les décimaux et lire les données
df_femmes_parmi_medailles = pd.read_csv(io.StringIO(data_femmes_parmi_medailles_str_full.replace(',', '.')), sep=';')

# Création du graphique principal
plt.figure(figsize=(12, 7))

for pays in ['Japon', 'France', 'Allemagne', 'Russie', 'États-Unis']:
    plt.plot(df_femmes_parmi_medailles['Année'], df_femmes_parmi_medailles[pays], marker='o', linestyle='-', label=pays)

plt.title('Proportion des femmes parmi les médaillés (1992-2016)', fontsize=16)
plt.xlabel('Année', fontsize=12)
plt.ylabel('Proportion des femmes parmi les médaillés', fontsize=12)
plt.legend(title='Pays', fontsize=10)
plt.grid(True, linestyle='--', alpha=0.7)
plt.xticks(df_femmes_parmi_medailles['Année'], rotation=45)

# Ajuster dynamiquement les graduations de l'axe Y, en s'assurant d'inclure 1.0 si présent
y_max_value = df_femmes_parmi_medailles[['Japon', 'France', 'Allemagne', 'Russie', 'États-Unis']].max().max()
upper_y_limit = max(1.0, y_max_value) # S'assurer que l'axe Y va au moins jusqu'à 1.0
plt.yticks(np.arange(0, upper_y_limit + 0.1, 0.1))

plt.tight_layout()

# Affichage du graphique principal
plt.show()

# --- Graphiques séparés pour Jeux d'Été et d'Hiver ---
# Identification des années de JO d'été et d'hiver
annees_ete = [1992, 1996, 2000, 2004, 2008, 2012, 2016]
annees_hiver = [1994, 1998, 2002, 2006, 2010, 2014]

df_ete = df_femmes_parmi_medailles[df_femmes_parmi_medailles['Année'].isin(annees_ete)]
df_hiver = df_femmes_parmi_medailles[df_femmes_parmi_medailles['Année'].isin(annees_hiver)]

# Graphique pour les Jeux d'Été
plt.figure(figsize=(12, 6))
for pays in ['Japon', 'France', 'Allemagne', 'Russie', 'États-Unis']:
    plt.plot(df_ete['Année'], df_ete[pays], marker='s', linestyle='--', label=pays)

plt.title('Proportion des femmes parmi les médaillés (JO d\'Été 1992-2016)', fontsize=16)
plt.xlabel('Année', fontsize=12)
plt.ylabel('Proportion des femmes parmi les médaillés', fontsize=12)
plt.legend(title='Pays', fontsize=10)
plt.grid(True, linestyle='--', alpha=0.7)
plt.xticks(df_ete['Année'])

# Ajuster dynamiquement les graduations de l'axe Y pour les JO d'été
y_max_value_ete = df_ete[['Japon', 'France', 'Allemagne', 'Russie', 'États-Unis']].max().max()
upper_y_limit_ete = max(1.0, y_max_value_ete)
plt.yticks(np.arange(0, upper_y_limit_ete + 0.1, 0.1))

plt.tight_layout()
plt.show()

# Graphique pour les Jeux d'Hiver
plt.figure(figsize=(12, 6))
for pays in ['Japon', 'France', 'Allemagne', 'Russie', 'États-Unis']:
    plt.plot(df_hiver['Année'], df_hiver[pays], marker='^', linestyle=':', label=pays)

plt.title('Proportion des femmes parmi les médaillés (JO d\'Hiver 1994-2014)', fontsize=16)
plt.xlabel('Année', fontsize=12)
plt.ylabel('Proportion des femmes parmi les médaillés', fontsize=12)
plt.legend(title='Pays', fontsize=10)
plt.grid(True, linestyle='--', alpha=0.7)
plt.xticks(df_hiver['Année'])

# Ajuster dynamiquement les graduations de l'axe Y pour les JO d'hiver
y_max_value_hiver = df_hiver[['Japon', 'France', 'Allemagne', 'Russie', 'États-Unis']].max().max()
upper_y_limit_hiver = max(1.0, y_max_value_hiver)
plt.yticks(np.arange(0, upper_y_limit_hiver + 0.1, 0.1))

plt.tight_layout()
plt.show()
