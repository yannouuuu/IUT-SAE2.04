# Importation des bibliothèques nécessaires
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import io

# Données complètes pour la proportion des médaillées parmi les femmes (1992-2006)
data_prop_med_femmes_str_full = """Année;Japon;France;Allemagne;Russie;États-Unis
1992;0.11;0.10;0.41;0.46;0.37
1994;0.06;0.13;0.33;0.42;0.17
1996;0.11;0.15;0.19;0.18;0.39
1998;0.03;0.10;0.34;0.30;0.32
2000;0.33;0.10;0.29;0.41;0.43
2002;0.02;0.22;0.29;0.12;0.34
2004;0.22;0.16;0.36;0.41;0.49
2006;0.02;0.16;0.33;0.24;0.33
"""

# Remplacer la virgule par un point pour les décimaux et lire les données
df_prop_med_femmes = pd.read_csv(io.StringIO(data_prop_med_femmes_str_full.replace(',', '.')), sep=';')

# Création du graphique
plt.figure(figsize=(12, 7))

for pays in ['Japon', 'France', 'Allemagne', 'Russie', 'États-Unis']:
    plt.plot(df_prop_med_femmes['Année'], df_prop_med_femmes[pays], marker='o', linestyle='-', label=pays)

plt.title('Proportion des médaillées parmi les femmes participantes (1992-2006)', fontsize=16)
plt.xlabel('Année', fontsize=12)
plt.ylabel('Proportion des médaillées femmes', fontsize=12)
plt.legend(title='Pays', fontsize=10)
plt.grid(True, linestyle='--', alpha=0.7)
plt.xticks(df_prop_med_femmes['Année'], rotation=45)

# Ajuster dynamiquement les graduations de l'axe Y
y_max_value = df_prop_med_femmes[['Japon', 'France', 'Allemagne', 'Russie', 'États-Unis']].max().max()
plt.yticks(np.arange(0, y_max_value + 0.05, 0.05)) # Pas de 0.05

plt.tight_layout()

# Affichage du graphique
plt.show()
