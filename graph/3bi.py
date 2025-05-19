# Importation des bibliothèques nécessaires
import matplotlib.pyplot as plt
import pandas as pd
import io
import numpy as np

# Données complètes pour le nombre de participants (1992-2016)
data_participants_str_full = """Année;Japon;France;Allemagne;Russie;États-Unis
1992;315;448;574;604;693
1994;59;98;112;113;148
1996;306;299;466;390;648
1998;156;106;125;122;186
2000;266;336;422;435;586
2002;103;114;157;151;202
2004;306;308;441;446;533
2006;110;82;155;174;204
2008;332;309;420;454;588
2010;91;104;149;175;212
2012;291;324;383;429;530
2014;109;107;151;213;222
2016;335;392;418;284;555
"""

# Lecture des données dans un DataFrame pandas
# io.StringIO permet de lire la chaîne de caractères comme si c'était un fichier
df_participants = pd.read_csv(io.StringIO(data_participants_str_full), sep=';')

# Création du graphique
plt.figure(figsize=(12, 7)) # Définition de la taille de la figure

# Boucle pour tracer une courbe pour chaque pays
# L'ordre des pays ici correspond aux colonnes du DataFrame après lecture du CSV
for pays in ['Japon', 'France', 'Allemagne', 'Russie', 'États-Unis']:
    plt.plot(df_participants['Année'], df_participants[pays], marker='o', linestyle='-', label=pays)

# Ajout du titre et des étiquettes pour les axes
plt.title('Évolution du nombre de participants par pays (1992-2016)', fontsize=16)
plt.xlabel('Année', fontsize=12)
plt.ylabel('Nombre de participants', fontsize=12)

# Affichage de la légende pour identifier les courbes
plt.legend(title='Pays', fontsize=10)

# Ajout d'une grille pour une meilleure lisibilité
plt.grid(True, linestyle='--', alpha=0.7)

# S'assurer que toutes les années sont affichées sur l'axe X
plt.xticks(df_participants['Année'], rotation=45) # Rotation pour éviter le chevauchement

# Ajustement automatique de la mise en page pour éviter que les éléments ne se coupent
plt.tight_layout()

# Affichage du graphique
plt.show()
