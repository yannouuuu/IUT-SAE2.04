# Importation des bibliothèques nécessaires
import matplotlib.pyplot as plt
import pandas as pd
import io
import numpy as np

# Données complètes pour le nombre de femmes participantes (1992-2006)
data_femmes_str_full = """Année;Japon;France;Allemagne;Russie;États-Unis
1992;100;128;199;208;240
1994;16;30;33;38;52
1996;149;102;187;158;273
1998;64;31;47;43;81
2000;110;125;181;194;253
2002;44;27;69;66;87
2004;167;113;191;202;254
2006;52;32;61;74;87
"""

# Lecture des données
df_femmes = pd.read_csv(io.StringIO(data_femmes_str_full), sep=';')

# Création du graphique
plt.figure(figsize=(12, 7))

for pays in ['Japon', 'France', 'Allemagne', 'Russie', 'États-Unis']:
    plt.plot(df_femmes['Année'], df_femmes[pays], marker='o', linestyle='-', label=pays)

plt.title('Évolution du nombre de femmes participantes par pays (1992-2006)', fontsize=16)
plt.xlabel('Année', fontsize=12)
plt.ylabel('Nombre de femmes participantes', fontsize=12)
plt.legend(title='Pays', fontsize=10)
plt.grid(True, linestyle='--', alpha=0.7)
plt.xticks(df_femmes['Année'], rotation=45)
plt.tight_layout()

# Affichage du graphique
plt.show()
