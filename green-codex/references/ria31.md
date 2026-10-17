# RIA31 : consignes opérationnelles

Adapté du *RIA31 — Référentiel IA éthique et responsable*, Institut du Numérique Responsable / ISIT
et groupe de travail IA. [Site officiel](https://ref-ia.isit-europe.org/), interface française consultée
le 17 octobre 2026. La [méthodologie v1.21, juin 2024](https://ref-ia.isit-europe.org/data/method_FR.pdf)
est attribuée à D. Didier, F. Abrikh et E. Benoits. Licence de cette adaptation : [CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/). Adaptation Green Codex du 17 octobre 2026 : reformulation, regroupement et ajout de preuves opérationnelles ; aucun soutien des auteurs à cette adaptation n’est présumé.

## Version et portée

Le site consulté affiche **5 familles, 13 recommandations, 41 critères**. La méthode PDF
annonce 31 critères : conserver cette différence, ne pas attribuer les 41 à sa version 2024.
Le site indique Licence Ouverte 2.0 en pied de page, tandis que la méthode indique CC BY-SA 4.0
pour le référentiel. Cette adaptation conserve l’attribution et le partage à l’identique ;
ces mentions divergentes sont signalées, sans conclure à une licence source unique.

Les 41 questions visibles ont été reformulées ci-dessous. Les tests proposés sont des ajouts
Green Codex ; les fiches détaillées et leurs calculs ne sont pas reproduits. Les identifiants
`RIA-001` à `RIA-041` appartiennent au skill, pas au référentiel. La correspondance source
suit l’ordre de lecture du site. Celui-ci emploie `STR-1_03-1` deux fois : les occurrences
sont distinguées ci-dessous. Pour retrouver un critère, ouvrir sa famille et sa recommandation ;
les liens de l’interface ne fournissent pas ici d’URL individuelle stable.

Le RIA31 n’est pas le règlement européen sur l’IA. Ses mentions juridiques ne remplacent pas
une vérification actuelle des textes et de leur applicabilité. Une petite optimisation technique
mobilise seulement les points techniques touchés ; l’audit complet est réservé à une demande
explicite ou à un périmètre de gouvernance pertinent.

## Mode d’emploi

Appliquer le filtre de périmètre de `../SKILL.md` et les exigences de preuve de
[closing-summary.md](closing-summary.md). Ces règles servent à sélectionner un point
concret, pas à certifier un engagement entier. Les contrôles organisationnels ne sont
pas exécutés par le scanner statique. Une action commune à plusieurs référentiels se
vérifie une seule fois ; citer les correspondances utiles sans multiplier les constats.

### RIA-001 — Contribution utile

Repère source : `STR-1_01` sur le [site RIA31](https://ref-ia.isit-europe.org/).

Action : Relier le besoin aux effets sociaux ou environnementaux recherchés, et examiner les effets contraires.

Preuve : Cible pertinente, bénéficiaires et indicateur ; citer un ODD ne démontre pas un bénéfice.

### RIA-002 — Durée de vie

Repère source : `STR-1_02-1` sur le [site RIA31](https://ref-ia.isit-europe.org/).

Action : Prévoir maintenance, support, remplacement des dépendances et sortie du service.

Preuve : Plan de maintien et scénario de fin de vie ; réutiliser SERVICE-EFF-005.

### RIA-003 — Réutilisation

Repère source : `STR-1_02-2` sur le [site RIA31](https://ref-ia.isit-europe.org/).

Action : Isoler les composants réutilisables et documenter leurs interfaces et droits d’usage.

Preuve : Essai de réutilisation dans un second contexte, sans créer une abstraction sans besoin.

### RIA-004 — Besoin

Repère source : `STR-1_03-1, occurrence 1` sur le [site RIA31](https://ref-ia.isit-europe.org/).

Action : Vérifier le problème réel, les utilisateurs et la valeur attendue avant de retenir l’IA.

Preuve : Recherche utilisateur ou usage observé ; réutiliser AI-EFF-001 et les 3U.

### RIA-005 — Alternative simple

Repère source : `STR-1_03-2` sur le [site RIA31](https://ref-ia.isit-europe.org/).

Action : Comparer avec une procédure humaine ou déterministe adaptée.

Preuve : Même tâche et seuil de qualité, coût total et risques comparés.

### RIA-006 — Alternative au génératif

Repère source : `STR-1_03-1, occurrence 2` sur le [site RIA31](https://ref-ia.isit-europe.org/).

Action : Si l’IA est utile, examiner un modèle spécialisé ou non génératif.

Preuve : Évaluation représentative face au génératif, incluant reprises et ressources.

### RIA-007 — Regards croisés

Repère source : `STR-1_04` sur le [site RIA31](https://ref-ia.isit-europe.org/).

Action : Associer les compétences nécessaires au contexte et les personnes exposées aux effets du système.

Preuve : Contributions effectives et décisions ; une liste de noms ne suffit pas.

### RIA-008 — Arbitrage éthique

Repère source : `STR-1_05-1` sur le [site RIA31](https://ref-ia.isit-europe.org/).

Action : Désigner une instance proportionnée capable de traiter les risques éthiques et environnementaux.

Preuve : Mandat, compétences, décisions et suivi ; pas de comité imposé pour une petite correction.

### RIA-009 — Suivi de la finalité

Repère source : `STR-1_05-2` sur le [site RIA31](https://ref-ia.isit-europe.org/).

Action : Réexaminer finalité, sources et usages lors des changements significatifs.

Preuve : Historique des arbitrages et alertes examinées.

### RIA-010 — Essais adverses

Repère source : `STR-1_06` sur le [site RIA31](https://ref-ia.isit-europe.org/).

Action : Tester les détournements et comportements inattendus pertinents dans un environnement autorisé.

Preuve : Scénarios adverses, résultats, corrections et risques résiduels ; réutiliser AI-CHARTER-TRUST-004.

### RIA-011 — Regard indépendant

Repère source : `STR-1_07` sur le [site RIA31](https://ref-ia.isit-europe.org/).

Action : Pour une évaluation formelle, demander une revue compétente indépendante de la réalisation.

Preuve : Mandat et rapport avec périmètre et conflits d’intérêts ; une auto-revue ne la remplace pas.

### RIA-012 — Gouvernance des données

Repère source : `STR-2_01` sur le [site RIA31](https://ref-ia.isit-europe.org/).

Action : Attribuer responsabilités, droits d’accès, usages et conservation sur tout le cycle de vie.

Preuve : Traçabilité, tests d’accès et d’expiration ; réutiliser DB-EFF-005.

### RIA-013 — Compétences des acteurs

Repère source : `CAD-1_01` sur le [site RIA31](https://ref-ia.isit-europe.org/).

Action : Adapter formation et accompagnement aux concepteurs, opérateurs et utilisateurs.

Preuve : Exercice pratique et couverture ; réutiliser AI-CHARTER-HUM-002.

### RIA-014 — Grille de confiance

Repère source : `CAD-2_01-1` sur le [site RIA31](https://ref-ia.isit-europe.org/).

Action : Documenter les exigences de confiance retenues et leur applicabilité, puis les relier à des contrôles.

Preuve : Matrice datée avec sources ; ne pas assimiler une grille de confiance à une preuve de conformité au règlement IA.

### RIA-015 — Risques transversaux

Repère source : `CAD-2_01-2` sur le [site RIA31](https://ref-ia.isit-europe.org/).

Action : Examiner équité, transparence, sécurité, explication et protection des données ensemble.

Preuve : Risques, responsables et tests ciblés ; réutiliser les familles AI-CHARTER-ETH et TRUST.

### RIA-016 — Dossier technique

Repère source : `CAD-2_02` sur le [site RIA31](https://ref-ia.isit-europe.org/).

Action : Versionner les informations sur modèles, données, limites, essais et risques, y compris les composants achetés.

Preuve : Dossier correspondant à la version déployée, pièces fournisseur et lacunes explicites.

### RIA-017 — Contrôles proportionnés

Repère source : `CAD-2_03` sur le [site RIA31](https://ref-ia.isit-europe.org/).

Action : Adapter intensité et fréquence des contrôles à la gravité et à la probabilité des risques.

Preuve : Justification, seuils et réexamen ; conserver les protections nécessaires sans multiplier les validations inutiles.

### RIA-018 — Cycle de vie complet

Repère source : `CAD-3_01-1` sur le [site RIA31](https://ref-ia.isit-europe.org/).

Action : Inclure préparation des données, acquisition, entraînement, exploitation et retrait dans l’analyse.

Preuve : Étapes, acteurs, impacts et risques identifiés, y compris externalisés.

### RIA-019 — Amélioration par étape

Repère source : `CAD-3_01-2` sur le [site RIA31](https://ref-ia.isit-europe.org/).

Action : Choisir des améliorations mesurables pour les étapes les plus contributrices.

Preuve : Comparaison de ressources et effets sociaux, sans transfert de charge caché ; MEASURE-EFF-004.

### RIA-020 — Références applicables

Repère source : `CAD-4_01` sur le [site RIA31](https://ref-ia.isit-europe.org/).

Action : Sélectionner les textes et référentiels pertinents pour le contexte, avec édition et périmètre.

Preuve : Registre de sources et examen compétent des obligations ; ne pas reprendre les dates juridiques du site sans vérification actuelle.

### RIA-021 — Catalogue des outils

Repère source : `CAD-4_02-1` sur le [site RIA31](https://ref-ia.isit-europe.org/).

Action : Documenter les outils autorisés, leur usage, limites et responsable.

Preuve : Inventaire consultable et configuration correspondant à la pratique.

### RIA-022 — Veille utile

Repère source : `CAD-4_02` sur le [site RIA31](https://ref-ia.isit-europe.org/).

Action : Réexaminer les outils après incident, évolution de risque ou changement significatif.

Preuve : Revue datée, décision et test de migration si nécessaire ; pas de mise à jour aveugle.

### RIA-023 — Engagement explicite

Repère source : `UX-1_01` sur le [site RIA31](https://ref-ia.isit-europe.org/).

Action : Préparer une présentation claire des engagements, limites et contacts du service.

Preuve : Texte cohérent avec les pratiques vérifiées ; publication par une personne autorisée.

### RIA-024 — Réglages compréhensibles

Repère source : `UX-1_02` sur le [site RIA31](https://ref-ia.isit-europe.org/).

Action : Proposer uniquement les réglages utiles que l’utilisateur peut comprendre et maîtriser.

Preuve : Essai de tâche et valeurs par défaut sûres ; ne pas exposer des paramètres techniques sans utilité.

### RIA-025 — Interaction annoncée

Repère source : `UX-1_03-1` sur le [site RIA31](https://ref-ia.isit-europe.org/).

Action : Rendre visible le rôle de l’IA avant que l’utilisateur ne s’y fie.

Preuve : Test du parcours réel, y compris erreurs et transfert humain ; AI-CHARTER-TRUST-001.

### RIA-026 — Choix de la personne

Repère source : `UX-1_03-2` sur le [site RIA31](https://ref-ia.isit-europe.org/).

Action : Identifier le profilage et les mécanismes influençant le comportement ; prévoir les choix et alternatives applicables.

Preuve : Essai du refus et de l’alternative ; analyse des droits selon le contexte, sans déduire leur portée du seul référentiel.

### RIA-027 — Analyse des émotions

Repère source : `UX-1_03-3` sur le [site RIA31](https://ref-ia.isit-europe.org/).

Action : Repérer toute analyse émotionnelle et demander une revue de sa nécessité et de son admissibilité avant usage.

Preuve : Décision compétente et information vérifiée si usage autorisé ; informer ne suffit pas à rendre une pratique admissible.

### RIA-028 — Origine des contenus

Repère source : `UX-1_03-4` sur le [site RIA31](https://ref-ia.isit-europe.org/).

Action : Indiquer de manière appropriée quand le contenu fourni provient de l’IA.

Preuve : Vérification des sorties et exports ; information fidèle sans faux certificat d’origine.

### RIA-029 — Qualité et écarts

Repère source : `FRT-1_01` sur le [site RIA31](https://ref-ia.isit-europe.org/).

Action : Tester erreurs, variations et disparités sur les populations et contextes pertinents.

Preuve : Jeux d’essai, tailles d’échantillon et limites ; AI-CHARTER-ETH-001.

### RIA-030 — Explication vérifiable

Repère source : `FRT-1_02` sur le [site RIA31](https://ref-ia.isit-europe.org/).

Action : Expliquer les facteurs réellement connus et les limites du résultat dans une forme compréhensible.

Preuve : Cas d’explication correcte et de source manquante ; ne pas inventer le raisonnement interne ; AI-CHARTER-TRUST-002.

### RIA-031 — Responsabilité humaine

Repère source : `FRT-1_03` sur le [site RIA31](https://ref-ia.isit-europe.org/).

Action : Attribuer les décisions et interventions nécessaires aux personnes habilitées.

Preuve : Test de rejet, correction, arrêt et absence de réviseur ; AI-CHARTER-TRUST-003.

### RIA-032 — Marquage de provenance

Repère source : `FRT-1_04` sur le [site RIA31](https://ref-ia.isit-europe.org/).

Action : Examiner un marquage de provenance adapté au média et aux usages, quand il est pertinent.

Preuve : Test après export ou transformation, limites d’effacement et d’erreur ; ni filigrane invisible systématique ni promesse de détection parfaite.

### RIA-033 — Outils de sécurité

Repère source : `BCK-1_01` sur le [site RIA31](https://ref-ia.isit-europe.org/).

Action : Mettre à disposition des tests adaptés aux menaces du système IA.

Preuve : Exécution sur entrées hostiles et contrôle des droits ; pas seulement une bibliothèque installée.

### RIA-034 — Choix techniques mesurés

Repère source : `BCK-1_02` sur le [site RIA31](https://ref-ia.isit-europe.org/).

Action : Comparer les solutions techniques à service et qualité équivalents.

Preuve : Profil ou mesure représentative ; indiquer les impacts inconnus. Aucun langage ou framework n’est intrinsèquement vert.

### RIA-035 — Modèle ajusté

Repère source : `BCK-2_01` sur le [site RIA31](https://ref-ia.isit-europe.org/).

Action : Comparer réemploi, compression ou spécialisation du modèle avec l’existant.

Preuve : Qualité, sécurité et ressources totales mesurées ; conserver le candidat répondant au besoin, sans gain présumé.

### RIA-036 — Corpus fiable

Repère source : `BCK-2_02` sur le [site RIA31](https://ref-ia.isit-europe.org/).

Action : Contrôler origine, qualité et contamination des données, notamment synthétiques.

Preuve : Échantillonnage documenté, séparation entraînement/test et erreurs suivies.

### RIA-037 — Langues et cultures

Repère source : `BCK-2_03` sur le [site RIA31](https://ref-ia.isit-europe.org/).

Action : Évaluer les langues et contextes culturels réellement visés.

Preuve : Résultats par langue et limites des données ; ne pas imposer une proportion uniforme sans besoin.

### RIA-038 — Partage maîtrisé

Repère source : `BCK-3_01-1` sur le [site RIA31](https://ref-ia.isit-europe.org/).

Action : Étudier le partage des composants et jeux d’essai réutilisables lorsque droits et confidentialité le permettent.

Preuve : Licence, contrôle des données et décision autorisée ; aucune publication automatique de corpus.

### RIA-039 — Conditions connues

Repère source : `BCK-3_01-2` sur le [site RIA31](https://ref-ia.isit-europe.org/).

Action : Documenter conditions d’usage, limites éthiques et données d’empreinte disponibles.

Preuve : Versions, périmètres, méthodes et inconnues ; prix et tokens ne valent pas mesure carbone.

### RIA-040 — Provenance des composants

Repère source : `BCK-4_01` sur le [site RIA31](https://ref-ia.isit-europe.org/).

Action : Tracer sources, versions et licences des composants, modèles et données intégrés.

Preuve : Inventaire et vérification des droits, intégrité et maintenance ; reformuler ne supprime pas les obligations de licence.

### RIA-041 — Données nécessaires

Repère source : `BCK-5_01` sur le [site RIA31](https://ref-ia.isit-europe.org/).

Action : Limiter copies, transferts et conservation aux usages justifiés.

Preuve : Cartographie, volumes et tests de rétention ; réutiliser DB-EFF-005 et AIR-008.
