# Importation des bibliothèques nécessaires
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import io
from matplotlib.patches import Patch # Pour la légende personnalisée

# Données complètes pour la proportion hommes/femmes (1992-2006)
# Format: Année;Pays;Proportion_Hommes;Proportion_Femmes
data_proportion_str_full = """Année;Pays;Proportion_Hommes;Proportion_Femmes
1992;France;0.71;0.29
1992;Germany;0.65;0.35
1992;Japan;0.68;0.32
1992;Russia;0.66;0.34
1992;USA;0.65;0.35
1994;France;0.69;0.31
1994;Germany;0.71;0.29
1994;Japan;0.73;0.27
1994;Russia;0.66;0.34
1994;USA;0.65;0.35
1996;France;0.66;0.34
1996;Germany;0.60;0.40
1996;Japan;0.51;0.49
1996;Russia;0.59;0.41
1996;USA;0.58;0.42
1998;France;0.71;0.29
1998;Germany;0.62;0.38
1998;Japan;0.59;0.41
1998;Russia;0.65;0.35
1998;USA;0.56;0.44
2000;France;0.63;0.37
2000;Germany;0.57;0.43
2000;Japan;0.59;0.41
2000;Russia;0.55;0.45
2000;USA;0.57;0.43
2002;France;0.76;0.24
2002;Germany;0.56;0.44
2002;Japan;0.57;0.43
2002;Russia;0.56;0.44
2002;USA;0.57;0.43
2004;France;0.63;0.37
2004;Germany;0.57;0.43
2004;Japan;0.45;0.55
2004;Russia;0.55;0.45
2004;USA;0.52;0.48
2006;France;0.61;0.39
2006;Germany;0.61;0.39
2006;Japan;0.53;0.47
2006;Russia;0.57;0.43
2006;USA;0.57;0.43
"""

# Lecture des données. La virgule décimale est déjà un point dans les données fournies.
df_proportion = pd.read_csv(io.StringIO(data_proportion_str_full), sep=';')

# Option : Graphique avec des barres groupées par année, chaque barre étant un pays
annees = df_proportion['Année'].unique()
pays_liste = df_proportion['Pays'].unique() # France, Germany, Japan, Russia, USA
n_annees = len(annees)
n_pays = len(pays_liste)

# Définir la largeur des barres et les positions
bar_width = 0.15 # Largeur d'une barre individuelle dans un groupe
group_width = n_pays * bar_width # Largeur totale d'un groupe de barres pour une année
x_indices = np.arange(n_annees) # Un indice par année

fig, ax = plt.subplots(figsize=(18, 10))

# Couleurs pour hommes et femmes
couleur_femmes = 'lightcoral'
couleur_hommes = 'lightblue'

# Itérer sur chaque pays pour dessiner ses barres pour chaque année
for i, pays_actuel in enumerate(pays_liste):
    # Extraire les proportions pour le pays actuel, en s'assurant de l'ordre des années
    prop_femmes_pays = df_proportion[df_proportion['Pays'] == pays_actuel].set_index('Année').reindex(annees)['Proportion_Femmes'].values
    prop_hommes_pays = df_proportion[df_proportion['Pays'] == pays_actuel].set_index('Année').reindex(annees)['Proportion_Hommes'].values
    
    # Calculer la position x pour les barres de ce pays
    # Chaque groupe d'années est à x_indices. À l'intérieur de ce groupe, chaque pays est décalé.
    positions_barres = x_indices - group_width/2 + i*bar_width + bar_width/2
    
    ax.bar(positions_barres, prop_femmes_pays, bar_width, label=f'{pays_actuel} - Femmes' if i==0 else None, color=plt.cm.get_cmap('Pastel1')(i*2)) # Couleur par pays+genre
    ax.bar(positions_barres, prop_hommes_pays, bar_width, bottom=prop_femmes_pays, label=f'{pays_actuel} - Hommes' if i==0 else None, color=plt.cm.get_cmap('Pastel1')(i*2+1))


ax.set_xlabel('Année', fontsize=14)
ax.set_ylabel('Proportion', fontsize=14)
ax.set_title('Proportion des femmes et des hommes par pays et par année (1992-2006)', fontsize=18)
ax.set_xticks(x_indices)
ax.set_xticklabels(annees)
plt.yticks(np.arange(0, 1.1, 0.1))
ax.grid(True, axis='y', linestyle='--', alpha=0.7)

# Création d'une légende plus claire
handles = []
labels = []
for i, pays_actuel in enumerate(pays_liste):
    handles.append(Patch(facecolor=plt.cm.get_cmap('Pastel1')(i*2), label=f'{pays_actuel} - Femmes'))
    handles.append(Patch(facecolor=plt.cm.get_cmap('Pastel1')(i*2+1), label=f'{pays_actuel} - Hommes'))
# Pour éviter les doublons si la logique de label dans la boucle est complexe:
# temp_handles, temp_labels = ax.get_legend_handles_labels()
# by_label = dict(zip(temp_labels, temp_handles))
# ax.legend(by_label.values(), by_label.keys(), title="Pays - Genre", bbox_to_anchor=(1.02, 1), loc='upper left', fontsize=10)

# Simplification de la légende: une couleur pour Femmes, une pour Hommes, et les pays sont groupés
# Redessinons avec une approche de légende plus simple si le groupement par pays est visuellement clair
ax.clear() # Nettoyer l'axe pour redessiner
colors = plt.cm.get_cmap('tab10', n_pays) # Une couleur par pays

for i, annee_actuelle in enumerate(annees):
    df_annee = df_proportion[df_proportion['Année'] == annee_actuelle].set_index('Pays').reindex(pays_liste) # Assurer l'ordre
    
    prop_femmes_annee = df_annee['Proportion_Femmes'].values
    prop_hommes_annee = df_annee['Proportion_Hommes'].values
    
    # Position des barres pour cette année (groupées par pays)
    bar_positions_annee = np.arange(n_pays) + i * (n_pays + 2) * bar_width # Groupes d'années séparés

    # Pour chaque pays dans l'année
    for j, pays_nom in enumerate(pays_liste):
        pos = j * bar_width + i * (group_width + 0.2) # Position pour la barre du pays j dans l'année i
        
        # Barres pour les femmes (en bas)
        ax.bar(pos, df_annee.loc[pays_nom, 'Proportion_Femmes'], bar_width, color=colors(j), alpha=0.6, label=f'{pays_nom} - Femmes' if i == 0 else "")
        # Barres pour les hommes (empilées sur celles des femmes)
        ax.bar(pos, df_annee.loc[pays_nom, 'Proportion_Hommes'], bar_width, bottom=df_annee.loc[pays_nom, 'Proportion_Femmes'], color=colors(j), alpha=1.0, label=f'{pays_nom} - Hommes' if i == 0 else "")

ax.set_xlabel('Pays regroupés par Année', fontsize=14)
ax.set_ylabel('Proportion', fontsize=14)
ax.set_title('Proportion des femmes et des hommes par pays et par année (1992-2006)', fontsize=18)

# Étiquettes X: Années centrées sur leurs groupes de barres
tick_positions = [i * (group_width + 0.2) + group_width/2 - bar_width/2 for i in range(n_annees)]
ax.set_xticks(tick_positions)
ax.set_xticklabels(annees)

plt.yticks(np.arange(0, 1.1, 0.1))
ax.grid(True, axis='y', linestyle='--', alpha=0.7)

# Légende (une entrée par pays, la distinction H/F est par l'empilement et alpha/couleur)
legend_handles = [Patch(facecolor=colors(j), label=pays_liste[j], alpha=0.8) for j in range(n_pays)]
# Ajouter des patches pour Hommes/Femmes si nécessaire
legend_handles.append(Patch(facecolor='grey', alpha=0.6, label='Femmes (partie inf.)'))
legend_handles.append(Patch(facecolor='grey', alpha=1.0, label='Hommes (partie sup.)'))
ax.legend(handles=legend_handles, title="Légende", bbox_to_anchor=(1.02, 1), loc='upper left')

plt.tight_layout(rect=[0, 0, 0.85, 1]) # Ajuster pour la légende externe
plt.show()

# --- Version alternative: une figure par année (souvent plus lisible pour ce type de données) ---
# (Le code pour cette version est dans la réponse précédente et peut être adapté avec les nouvelles données si préféré)
# for annee_specifique in annees:
#     df_annee_specifique = df_proportion[df_proportion['Année'] == annee_specifique].set_index('Pays')
#     # ... (reste du code pour le graphique par année) ...
