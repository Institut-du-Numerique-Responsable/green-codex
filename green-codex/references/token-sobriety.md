# Règles NR : sobriété des tokens pour les agents IA

Licence : Apache-2.0. Règles inspirées et adaptées de Caveman, Copyright 2026 Julius Brussee.
Modifications et extensions : Copyright 2026 Institut du Numérique Responsable.
Voir [l'attribution et la provenance](third-party-attributions.md).

## Objectif

Réduire les tokens consommés, les appels aux modèles et les traitements inutiles,
sans dégrader la qualité, la sécurité, la maintenabilité ni la compréhension du code.

Réduire les tokens et les appels inutiles contribue au Numérique Responsable en
limitant les traitements mobilisés pour un même résultat, tout en préservant la qualité ;
le gain environnemental réel dépend du modèle, de l'infrastructure et de l'usage.

Ces règles s'appliquent aux agents IA de développement, notamment Claude Code,
OpenAI Codex et Mistral Vibe. Ce sont des conventions du projet. Les mécanismes
disponibles doivent être vérifiés dans l'environnement utilisé ; aucune commande
propre à un produit ne doit être transposée automatiquement à un autre.

## A. Sobriété des réponses

**NR-TOK-001 : Répondre directement**

Fournir la réponse ou le résultat sans introduction superflue. Supprimer les formules
automatiques de politesse et les annonces d'intention inutiles.

**NR-TOK-002 : Éliminer les répétitions**

Chaque information doit apparaître une seule fois, sauf si sa répétition est
nécessaire à la compréhension ou à la sécurité.

**NR-TOK-003 : Privilégier les formulations concises**

Utiliser des phrases courtes, un vocabulaire précis et des termes techniques
standardisés. Ne jamais sacrifier la clarté pour réduire le nombre de mots.

**NR-TOK-004 : Supprimer les conclusions redondantes**

Ne pas reformuler une réponse déjà donnée. Terminer lorsque l'information nécessaire
a été transmise.

**NR-TOK-005 : Adapter la longueur à la complexité**

Produire une réponse proportionnelle à la demande. Une question simple nécessite une
réponse courte. Une décision complexe peut nécessiter une explication détaillée.

**NR-TOK-006 : Limiter les messages intermédiaires**

Éviter les commentaires entre appels d'outils. Communiquer uniquement les étapes
significatives, les blocages et les résultats.

## B. Gestion du contexte

**NR-TOK-007 : Charger uniquement les informations nécessaires**

Ne pas charger systématiquement l'intégralité d'un projet, d'un dépôt ou d'une documentation.

**NR-TOK-008 : Privilégier la recherche ciblée**

Utiliser la recherche par symbole, nom de fichier, fonction ou expression avant de lire
un fichier complet.

**NR-TOK-009 : Éviter les lectures répétées**

Réutiliser les informations déjà disponibles dans le contexte lorsqu'elles sont encore valides.
Relire une preuve après une modification susceptible de l'invalider : fichier changé,
branche différente, dépendance mise à jour ou résultat externe devenu périmé.

**NR-TOK-010 : Compresser les informations volumineuses**

Résumer les logs, fichiers JSON, CSV, YAML et résultats de tests avant leur transmission
au modèle, lorsque le détail complet n'est pas nécessaire.
Conserver la sortie complète accessible localement si elle est utile au diagnostic.
Une sortie tronquée doit être signalée et explorée par recherche ciblée si nécessaire.

**NR-TOK-011 : Préserver les données critiques**

Toute compression doit conserver les erreurs pertinentes, négations, nombres, unités,
chemins, identifiants et informations nécessaires à la résolution du problème.
Préserver aussi les codes de sortie, les critères d'acceptation, les décisions prises,
les autorisations et les travaux non terminés. Ne jamais exposer de secret pour rendre
un résumé plus complet.

**NR-TOK-012 : Optimiser les fichiers d'instructions**

Maintenir concis `AGENTS.md`, `SKILL.md` et les fichiers d'instructions équivalents des autres agents. Éviter les instructions
dupliquées et charger les règles spécialisées uniquement lorsque nécessaire.

**NR-TOK-013 : Externaliser les connaissances secondaires**

Placer les références détaillées dans des fichiers spécialisés plutôt que dans les
instructions systématiquement chargées.

**NR-TOK-014 : Éviter la surcharge contextuelle**

Ne pas transmettre au modèle des données sans rapport avec la tâche. Écarter les résultats
non pertinents avant leur inclusion dans le contexte.

## C. Sobriété des opérations

**NR-TOK-015 : Investiguer avant de modifier**

Identifier les causes probables d'un problème avant de produire du code. Éviter les
modifications successives fondées sur des hypothèses non vérifiées.

**NR-TOK-016 : Effectuer des modifications ciblées**

Modifier uniquement les éléments nécessaires. Ne pas réécrire un fichier entier pour
corriger quelques lignes.
Préserver les modifications de l'utilisateur et des autres agents. Relire le diff
effectif avant de conclure ; une économie de tokens ne justifie aucun écrasement.

**NR-TOK-017 : Limiter les sorties de code**

Afficher uniquement les lignes modifiées et le contexte indispensable, sauf demande
explicite de restitution complète.

**NR-TOK-018 : Réutiliser les outils existants**

Privilégier les scripts, commandes et outils déjà disponibles plutôt que de recréer
une solution équivalente.

**NR-TOK-019 : Réduire les appels redondants**

Éviter les recherches, commandes et appels d'outils dont le résultat est déjà connu
et toujours valide.

**NR-TOK-020 : Regrouper les opérations indépendantes**

Exécuter ensemble les opérations compatibles lorsque cela réduit les échanges avec
le modèle, sans compromettre la traçabilité.
Regrouper les lectures indépendantes. Garder séquentielles les opérations dépendantes,
les mutations concurrentes sur un même fichier et les actions soumises à autorisation.
Examiner le résultat et le code de sortie de chaque opération.

**NR-TOK-021 : Vérifier de manière proportionnée**

Exécuter d'abord les tests directement concernés par une modification. Étendre la
vérification lorsque le risque ou les dépendances le justifient.
Exécuter les contrôles exigés par le projet. Un test réussi avant une modification
ne vérifie pas cette modification. Une vérification de types ne prouve pas à elle seule
le comportement demandé.

**NR-TOK-022 : Arrêter les traitements inutiles**

Arrêter l'exploration et les modifications lorsque les critères d'acceptation sont
satisfaits. Ne pas ajouter de fonctionnalités ou de refactorisations hors périmètre.
Définir ces critères à partir de la demande et des consignes du projet. Un blocage
doit être signalé avec les travaux restants ; il ne vaut pas achèvement. Après un échec,
ne répéter une opération qu'avec une hypothèse nouvelle, une entrée corrigée ou un
changement d'état vérifiable.

## D. Optimisation des modèles

**NR-TOK-023 : Adapter le modèle à la difficulté**

Lorsque l'environnement le permet, sélectionner un modèle ou un niveau de raisonnement
proportionné à la complexité de la tâche.
Respecter le choix explicite de l'utilisateur. Évaluer le résultat complet avant
de réduire l'effort ; ne pas prétendre modifier un réglage inaccessible.

**NR-TOK-024 : Éviter les appels coûteux sans justification**

Ne pas mobiliser systématiquement les modèles les plus coûteux pour des opérations
simples, déterministes ou réalisables localement.

**NR-TOK-025 : Privilégier les traitements déterministes**

Utiliser des outils locaux pour les opérations de filtrage, tri, formatage, validation
syntaxique et calcul lorsque cela est pertinent.

**NR-TOK-026 : Exploiter le cache disponible**

Réutiliser les résultats et les mécanismes de cache existants lorsque les données et
les conditions d'exécution restent valides.
Distinguer cache de résultats locaux et cache de préfixe du modèle. La présence
d'un préfixe identique ne prouve pas un cache hit. Ne pas conserver un résultat périmé
ni ajouter du contenu inutile pour augmenter un taux de cache.

## E. Qualité et mesure

**NR-TOK-027 : Préserver la qualité fonctionnelle**

Aucune économie de tokens ne doit justifier une perte de sécurité, d'exactitude,
d'accessibilité, de maintenabilité ou de compréhension.

**NR-TOK-028 : Mesurer les économies réelles**

Lorsque les métriques sont disponibles, relever les tokens d'entrée, de sortie et de
cache, le nombre d'appels et le coût. Comparer à une référence équivalente.
Indiquer la source, le périmètre et les champs manquants des mesures. Une mesure absente
reste inconnue. Éviter les doubles comptes entre sous-totaux, totaux cumulés et cache.

**NR-TOK-029 : Évaluer le coût global**

Prendre en compte les tentatives supplémentaires, les erreurs, les corrections et les
reprises. Une réponse plus courte n'est pas nécessairement une exécution plus sobre.
Inclure les sous-agents et leurs vérifications dans le périmètre mesuré lorsqu'ils
participent au résultat. Ne pas confondre appels d'outils, tours et appels au modèle.

**NR-TOK-030 : Rendre compte des règles appliquées**

En fin de session, produire un bilan concis indiquant les règles effectivement
appliquées, les optimisations réalisées et les gains mesurés lorsqu'ils sont disponibles.
Ne jamais inventer de métriques.

## Priorités d'application

- **Obligatoires :** NR-TOK-007, NR-TOK-011, NR-TOK-015, NR-TOK-016, NR-TOK-022,
  NR-TOK-027 et NR-TOK-030.
- **Recommandées par défaut :** toutes les autres règles.
- **Conditionnelles :** NR-TOK-023 à NR-TOK-026 et NR-TOK-028, selon les capacités
  techniques de l'environnement. Cette condition précise leur application par défaut.

Respecter les instructions de priorité supérieure, les autorisations et les exigences
de sécurité de l'environnement, y compris les communications obligatoires. Appliquer
chaque règle à son déclencheur : NR-TOK-011 concerne une compression, NR-TOK-015 une
investigation de problème et NR-TOK-016 une modification. Ne pas créer une opération
inutile pour déclarer une règle appliquée.

## Articulation avec les pratiques existantes

Le [guide d'application à Codex](codex-token-sobriety.md) précise les déclencheurs,
les preuves attendues, les différences entre interfaces et la méthode de mesure.
Le consulter pour configurer, mesurer ou auditer Codex ; une tâche ordinaire ne demande
pas son chargement intégral.

Les [pratiques Codex](usage-practices.md) détaillent les mécanismes propres à Codex.
Conserver leurs identifiants pour les évaluations existantes. Lorsqu'une même action
répond à plusieurs règles, la décrire une seule fois avec les identifiants concernés
et ne compter son éventuel gain qu'une seule fois.

| Règles transversales | Pratiques Codex associées |
| --- | --- |
| NR-TOK-007 à NR-TOK-014 | USAGE-CODEX-CTX-01, USAGE-CODEX-CTX-04, USAGE-CODEX-CTX-05, USAGE-CODEX-MEM-01, USAGE-CODEX-MEM-02 |
| NR-TOK-001 à NR-TOK-006 | USAGE-CODEX-CTX-06 |
| NR-TOK-021, NR-TOK-027 | USAGE-CODEX-VERIFY-01 |
| NR-TOK-023 à NR-TOK-029 | USAGE-CODEX-COMPUTE-01, USAGE-CODEX-COMPUTE-02, USAGE-CODEX-COMPUTE-03 |

## Format du bilan de session

Intégrer ce bilan au [bilan NR existant](closing-summary.md) sans répéter les actions
déjà décrites. Regrouper les métriques indisponibles en une phrase si cela suffit.
Le script `nr_summary.py` accepte les identifiants NR-TOK ; il ne collecte pas les
métriques de tokens et ne vérifie pas leur véracité. Compléter le bilan textuel avec
les mesures disponibles et leur provenance.

### Sobriété des tokens

**Règles appliquées :** identifiants NR-TOK concernés.

**Optimisations réalisées :** actions concrètes effectuées.

**Mesures disponibles :**
- Tokens d'entrée :
- Tokens de sortie :
- Tokens de cache :
- Nombre d'appels au modèle :
- Coût :
- Économie mesurée :

**Qualité :** tests réalisés et résultats.

**Limites :** métriques indisponibles, risques résiduels ou compromis éventuels.

Ne présenter un pourcentage d'économie que si une référence comparable est disponible.
Ne pas confondre réduction de tokens, réduction des coûts et réduction d'impact
environnemental. Conserver un périmètre, un résultat fonctionnel et des exigences de
qualité équivalents pour la comparaison ; inclure les tentatives et reprises.
