<br/>
<p align="center">
    <picture>
        <source media="(prefers-color-scheme: dark)" srcset="https://github.com/yannouuuu/IUT-SAE2.04/raw/main/.github/assets/header_univlille_light.png" width="200px">
        <img alt="UnivLilleLogo" src="https://github.com/yannouuuu/IUT-SAE2.04/raw/main/.github/assets/header_univlille_dark.png" width="200px">
    </picture>
  <h1 align="center">IUT-SAE2.04 | Exploitation d'une base de données</h1>
</p>

<p align="center">
    Module d'exploitation d'une base de données PostgreSQL pour analyse statistique
    <br/>
    Jeux Olympiques | Analyse choisie : Turin Hiver 2006 
    <br/>
    <br/>
    <a href="https://moodle.univ-lille.fr/course/view.php?id=30827&sectionid=266882"><strong>Voir la page sur le moodle »</strong></a>
    <br/>
    <br/>
    <a href="https://github.com/yannouuuu/IUT-SAE2.04/"><strong>Voir le projet complet sur GitHub »</strong></a>
</p>

<br/>

## Environnement de développement

- **Langages :** SQL (PostgreSQL), Python
- **Outils :**
  - Analyse de données : Python avec bibliothèques (matplotlib, pandas, etc.)
  - Base de données : PostgreSQL 17
  - IDE/Text Editor : VS Code
  - Git pour la gestion de version

## Structure des fichiers
```plaintext
IUT-SAE2.04/
├── .github/
├── bdd/
│   └── schema.sql                # Schéma de la base de données
├── charts/
│   ├── 3bi.png                   # Graphique évolution du nombre de participants
│   ├── 3bii.png                  # Graphique évolution du nombre de médaillés
│   ├── 3biii.png                 # Graphique évolution du nombre de femmes participantes
│   ├── 3biv.png                  # Graphique proportion des femmes par rapport aux hommes
│   ├── 3bv.png                   # Graphique proportion des médaillées parmi les femmes
│   ├── 3bvi.png                  # Graphique proportion des femmes parmi les médaillés
│   ├── agemoyenparpays.png       # Graphique âge moyen par pays
│   ├── age_moyen_carte.png       # Carte choroplèthe de l'âge moyen par pays
│   ├── comparaisonpoidsmoyenhf.png # Graphique comparaison poids moyen H/F
│   ├── nbsportifsparpays.png     # Graphique nombre de sportifs par pays
│   ├── nombretotalmedaillesparpays.png # Graphique nombre total de médailles par pays
│   └── top20sportifsayantleplusdeparticipationsauxJO.png # Graphique top 20 sportifs
├── csv/
│   ├── athlete_events.csv        # Données des athlètes aux JO
│   ├── noc_regions.csv           # Correspondance des codes NOC et des pays
│   └── turin_stats_2006.csv      # Statistiques JO Turin 2006
├── graph/                        # Script Python pour les graphiques
├── rapport.md                    # Rapport d'analyse en Markdown
├── rapport.pdf                   # Rapport d'analyse en  PDF
├── README.md
├── SAE 2.04_2025.pdf             # Présentation de la SAE 2.04
└── Sujet statistique.pdf         # Sujet détaillé de l'analyse statistique
```

---

### Description du projet

Ce projet est une analyse statistique des données olympiques, réalisée dans le cadre de la SAE 2.04 de Statistiques. L'objectif principal est d'exploiter une base de données PostgreSQL préalablement ventillée par nos requêtes, contenant des informations sur les Jeux Olympiques, avec un focus particulier sur les Jeux d'hiver de Turin en 2006.

Les analyses effectuées comprennent :
- Identification des 20 athlètes avec le plus de participations aux JO
- Analyse détaillée des Jeux Olympiques d'hiver 2006 à Turin (âge moyen, nombre d'athlètes, etc.)
- Étude de la place des femmes dans les JO à travers différents indicateurs
- Comparaison de cinq pays sélectionnés (USA, France, Allemagne, Russie, Japon)

Les résultats sont présentés sous forme de requêtes SQL, tableaux statistiques et visualisations graphiques réalisées avec Python.

### Remerciements

Nous tenons à remercier **MATHIEU Phillipe et DELETOMBE  Marie** pour leurs encadrements dans le cadre de ce projet de base de données et statistiques.

<br/>
<p align="center">
    <picture>
        <img alt="UnivLilleLogo" src="https://github.com/yannouuuu/IUT-SAE2.04/raw/main/.github/assets/footer_univlille.png">
    </picture>
</p>
