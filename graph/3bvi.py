# Importation des bibliothèques nécessaires
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import io

# Données complètes pour la proportion des femmes parmi les médaillés (1992-2006)
data_femmes_parmi_medailles_str_full = """Année;Japon;France;Allemagne;Russie;États-Unis
1992;0.20;0.19;0.40;0.41;0.45
1994;0.11;0.40;0.35;0.57;0.60
1996;0.38;0.33;0.33;0.29;0.47
1998;0.22;0.20;0.48;0.29;0.79
2000;0.88;0.20;0.50;0.47;0.52
2002;0.50;0.43;0.43;0.23;0.38
2004;0.44;0.38;0.49;0.46;0.58
2006;1.00;0.38;0.53;0.51;0.63
"""
# Note: La valeur de 1.00 pour le Japon en 2006 est notable.
# Cela signifie que 100% des médaillés japonais cette année-là étaient des femmes.

# Remplacer la virgule par un point pour les décimaux et lire les données
df_femmes_parmi_medailles = pd.read_csv(io.StringIO(data_femmes_parmi_medailles_str_full.replace(',', '.')), sep=';')

# Création du graphique
plt.figure(figsize=(12, 7))

for pays in ['Japon', 'France', 'Allemagne', 'Russie', 'États-Unis']:
    plt.plot(df_femmes_parmi_medailles['Année'], df_femmes_parmi_medailles[pays], marker='o', linestyle='-', label=pays)

plt.title('Proportion des femmes parmi les médaillés (1992-2006)', fontsize=16)
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

# Affichage du graphique
plt.show()
