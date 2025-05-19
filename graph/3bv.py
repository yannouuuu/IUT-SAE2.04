# Importation des bibliothèques nécessaires
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import io

# Données complètes pour la proportion des médaillées parmi les femmes (1992-2016)
data_prop_med_femmes_str_full = """Année;Japon;France;Allemagne;Russie;États-Unis
1992;0.11;0.10;0.41;0.46;0.37
1994;0.06;0.13;0.33;0.42;0.17
1996;0.11;0.15;0.19;0.18;0.39
1998;0.03;0.10;0.34;0.30;0.32
2000;0.33;0.10;0.29;0.41;0.43
2002;0.02;0.22;0.29;0.12;0.34
2004;0.22;0.16;0.36;0.41;0.49
2006;0.02;0.16;0.33;0.24;0.33
2008;0.16;0.08;0.22;0.35;0.47
2010;0.09;0.16;0.38;0.10;0.38
2012;0.32;0.20;0.14;0.28;0.50
2014;0.03;0.08;0.16;0.20;0.38
2016;0.16;0.17;0.32;0.52;0.40
"""

# Remplacer la virgule par un point pour les décimaux et lire les données
df_prop_med_femmes = pd.read_csv(io.StringIO(data_prop_med_femmes_str_full.replace(',', '.')), sep=';')

# Création du graphique principal
plt.figure(figsize=(12, 7))

for pays in ['Japon', 'France', 'Allemagne', 'Russie', 'États-Unis']:
    plt.plot(df_prop_med_femmes['Année'], df_prop_med_femmes[pays], marker='o', linestyle='-', label=pays)

plt.title('Proportion des médaillées parmi les femmes participantes (1992-2016)', fontsize=16)
plt.xlabel('Année', fontsize=12)
plt.ylabel('Proportion des médaillées femmes', fontsize=12)
plt.legend(title='Pays', fontsize=10)
plt.grid(True, linestyle='--', alpha=0.7)
plt.xticks(df_prop_med_femmes['Année'], rotation=45)

# Ajuster dynamiquement les graduations de l'axe Y
y_max_value = df_prop_med_femmes[['Japon', 'France', 'Allemagne', 'Russie', 'États-Unis']].max().max()
plt.yticks(np.arange(0, y_max_value + 0.05, 0.05)) # Pas de 0.05

plt.tight_layout()

# Affichage du graphique principal
plt.show()

# --- Graphiques séparés pour Jeux d'Été et d'Hiver ---
# Identification des années de JO d'été et d'hiver
annees_ete = [1992, 1996, 2000, 2004, 2008, 2012, 2016]
annees_hiver = [1994, 1998, 2002, 2006, 2010, 2014]

df_ete = df_prop_med_femmes[df_prop_med_femmes['Année'].isin(annees_ete)]
df_hiver = df_prop_med_femmes[df_prop_med_femmes['Année'].isin(annees_hiver)]

# Graphique pour les Jeux d'Été
plt.figure(figsize=(12, 6))
for pays in ['Japon', 'France', 'Allemagne', 'Russie', 'États-Unis']:
    plt.plot(df_ete['Année'], df_ete[pays], marker='s', linestyle='--', label=pays)

plt.title('Proportion des médaillées parmi les femmes participantes (JO d\'Été 1992-2016)', fontsize=16)
plt.xlabel('Année', fontsize=12)
plt.ylabel('Proportion des médaillées femmes', fontsize=12)
plt.legend(title='Pays', fontsize=10)
plt.grid(True, linestyle='--', alpha=0.7)
plt.xticks(df_ete['Année'])

# Ajuster dynamiquement les graduations de l'axe Y pour les JO d'été
y_max_value_ete = df_ete[['Japon', 'France', 'Allemagne', 'Russie', 'États-Unis']].max().max()
plt.yticks(np.arange(0, y_max_value_ete + 0.05, 0.05)) # Pas de 0.05

plt.tight_layout()
plt.show()

# Graphique pour les Jeux d'Hiver
plt.figure(figsize=(12, 6))
for pays in ['Japon', 'France', 'Allemagne', 'Russie', 'États-Unis']:
    plt.plot(df_hiver['Année'], df_hiver[pays], marker='^', linestyle=':', label=pays)

plt.title('Proportion des médaillées parmi les femmes participantes (JO d\'Hiver 1994-2014)', fontsize=16)
plt.xlabel('Année', fontsize=12)
plt.ylabel('Proportion des médaillées femmes', fontsize=12)
plt.legend(title='Pays', fontsize=10)
plt.grid(True, linestyle='--', alpha=0.7)
plt.xticks(df_hiver['Année'])

# Ajuster dynamiquement les graduations de l'axe Y pour les JO d'hiver
y_max_value_hiver = df_hiver[['Japon', 'France', 'Allemagne', 'Russie', 'États-Unis']].max().max()
plt.yticks(np.arange(0, y_max_value_hiver + 0.05, 0.05)) # Pas de 0.05

plt.tight_layout()
plt.show()
