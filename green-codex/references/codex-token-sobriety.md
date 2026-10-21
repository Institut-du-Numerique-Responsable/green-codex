# Appliquer la sobriété des tokens dans Codex

Licence : Apache-2.0. Adaptation INR des règles de sobriété inspirées de Caveman,
Copyright 2026 Julius Brussee. Modifications : Copyright 2026 Institut du Numérique Responsable.
Voir [l'attribution et la provenance](third-party-attributions.md).

Ce guide met en pratique [NR-TOK-001 à NR-TOK-030](token-sobriety.md). Les identifiants
et priorités restent inchangés. Les procédures et critères ci-dessous sont des choix
du projet ; les liens officiels documentent les capacités des produits.

## Déclencheurs et preuves

| Situation | Action attendue dans Codex | Preuve utile | Règles |
| --- | --- | --- | --- |
| Demande reçue | Relever le résultat attendu, le périmètre, les contraintes et la vérification qui établira l'achèvement. Réutiliser les critères déjà fournis. | Critères concrets dans le contexte ; plan seulement si la complexité le justifie. | NR-TOK-005, NR-TOK-022, NR-TOK-027 |
| Exploration | Lire les instructions applicables et une cartographie existante, puis chercher un chemin ou symbole avec `rg --files` ou `rg -n`. Lire les passages pertinents. | Chemins et extraits nécessaires à la décision. | NR-TOK-007, NR-TOK-008, NR-TOK-014 |
| Lecture déjà effectuée | Réutiliser le résultat encore valide. Relire après une mutation pertinente ou un changement externe. | État auquel correspond la preuve. | NR-TOK-009, NR-TOK-019 |
| Log volumineux | Filtrer localement, conserver erreur et code de sortie, signaler la troncature. Garder le détail utile accessible sans exposer de secret. | Résumé diagnostique et chemin du log si conservé. | NR-TOK-010, NR-TOK-011, NR-TOK-025 |
| Correction | Établir la cause probable, utiliser un patch ciblé, préserver le travail existant et examiner le diff. | Symptôme, cause étayée, diff et test concerné. | NR-TOK-015, NR-TOK-016, NR-TOK-017 |
| Appels d'outils indépendants | Regrouper les lectures compatibles et vérifier chaque résultat. Séquencer les dépendances, mutations et autorisations. | Résultat et statut de chaque commande. | NR-TOK-018, NR-TOK-020 |
| Délégation autorisée | Déléguer une tâche bornée avec entrées, sortie attendue et critère d'arrêt ; éviter les explorations identiques et les modifications concurrentes. | Résultat vérifié et coût des agents inclus si disponible. | NR-TOK-024, NR-TOK-029 |
| Vérification | Tester le comportement touché, puis les dépendances à risque et les contrôles imposés. Ne relancer qu'après une nouvelle modification ou un doute étayé. | Commande, résultat observé et limites. | NR-TOK-021, NR-TOK-027 |
| Fin de travail | Vérifier les critères, transmettre le résultat et les limites, puis arrêter. Conserver les travaux bloqués comme inachevés. | Bilan concis fondé sur les opérations effectuées. | NR-TOK-001 à NR-TOK-006, NR-TOK-022, NR-TOK-030 |

## Contexte et instructions

Conserver le socle obligatoire dans `SKILL.md` et les références spécialisées à part.
Lier cette référence depuis les instructions du projet lorsqu'elle est pertinente,
sans recopier tout le catalogue dans chaque fichier. Les corrections durables vont
dans les consignes ; l'état provisoire d'une tâche reste dans son suivi.

Codex assemble les instructions `AGENTS.md` selon leur portée et reconnaît
`AGENTS.override.md`. Vérifier les fichiers applicables au répertoire de travail
avant de déduire les règles actives. Un fichier modifié dans ce dépôt ne prouve pas
que la copie installée du skill a été mise à jour.
[Documentation officielle des instructions](https://learn.chatgpt.com/docs/agent-configuration/agents-md).

Avant une compaction ou une reprise, préserver l'objectif, les contraintes, les
autorisations, les chemins utiles, les décisions, les tests réalisés et les travaux
restants. Ne pas compacter après chaque tour. Pour une tâche sans rapport avec la
précédente, une nouvelle conversation peut limiter le contexte inutile.

## Capacités selon l'interface

Vérification documentaire : 21 octobre 2026. Aide locale consultée : `codex-cli 0.163.0`.
Revalider les commandes après une évolution de version ou un changement d'interface.

| Environnement | Capacité documentée | Limite d'application |
| --- | --- | --- |
| CLI interactive | `/compact` résume l'historique ; `/model` sélectionne les réglages disponibles ; `/status` affiche l'état de session. | Les commandes doivent être proposées ou utilisées uniquement dans une interface qui les expose. |
| CLI non interactive | `codex exec --json` produit des événements JSONL ; `--output-last-message` enregistre la réponse finale. | Le journal complet peut contenir prompts et sorties d'outils. Filtrer avant partage. |
| Application, extension IDE ou autre hôte | Utiliser les contrôles et métriques effectivement exposés. | Ne pas simuler une commande CLI ni supposer un compteur accessible au modèle. |

Sources : [commandes interactives](https://learn.chatgpt.com/docs/developer-commands?surface=cli),
[mode non interactif](https://learn.chatgpt.com/docs/non-interactive-mode).

Respecter les autorisations et le modèle choisi par l'utilisateur. Ne pas désactiver
le sandbox, la revue ou la validation des hooks pour réduire les échanges. Maintenir
les mises à jour de progression imposées par l'hôte, avec un contenu utile et concis.

## Cache et compaction

Réutiliser les sorties locales seulement si leurs entrées, dépendances et conditions
restent valides. Pour le cache du modèle, conserver les instructions stables quand
cela convient au travail. Une compaction peut changer le préfixe et réduire sa
réutilisation. Comparer le coût global avant de retenir une stratégie.

L'API expose des mécanismes de cache qui dépendent du modèle et des paramètres.
Ce guide n'affirme pas que Codex donne accès à tous ces réglages. Un taux de cache
élevé ne prouve ni une réduction des tokens totaux ni un gain environnemental.
[Documentation officielle du cache](https://developers.openai.com/api/docs/guides/prompt-caching).

## Mesurer une tâche complète

Choisir une tâche et des critères de qualité équivalents. Consigner la version de
Codex, le modèle et l'effort quand ils sont connus, l'état du dépôt, les tests attendus
et le périmètre des agents inclus. Comparer plusieurs exécutions représentatives
lorsque la variabilité influence la décision. Ne pas lancer de benchmark supplémentaire
pour une simple correction documentaire sans objectif de mesure.

Le mode JSONL documente un événement `turn.completed` avec un objet `usage`, notamment
`input_tokens`, `cached_input_tokens` et `output_tokens`. Vérifier le schéma réellement
émis par la version utilisée. Compter chaque événement une seule fois dans un journal
complet ; ne pas sommer en plus des compteurs cumulés issus d'une autre source.
[Source du format](https://learn.chatgpt.com/docs/non-interactive-mode).

| Indicateur | Convention de mesure |
| --- | --- |
| Tokens d'entrée | Reporter le champ fourni avec son périmètre. Pour le schéma qui inclut le cache dans l'entrée, ne pas ajouter le cache une seconde fois. |
| Tokens de cache | Reporter séparément le sous-ensemble mis en cache. Distinguer lecture et écriture si le fournisseur les sépare. |
| Tokens de sortie | Conserver la définition du fournisseur ; ne pas ajouter un sous-total de raisonnement déjà inclus. |
| Appels au modèle | Utiliser une télémétrie explicite. Un tour peut comprendre plusieurs appels ; un appel d'outil n'est pas un appel au modèle. |
| Coût | Reporter le coût observé ou une estimation clairement étiquetée, avec tarifs, date et hypothèses. Un abonnement ne donne pas automatiquement un coût réel par tâche. |
| Total de la tâche | Inclure corrections, tentatives échouées, reprises, sous-agents et vérifications. Signaler toute partie absente du journal. |

Une interruption ou un journal incomplet rend le total partiel. Ne pas remplacer les
champs absents par zéro. Les métriques d'une exécution enfant ne mesurent pas à elles
seules la session qui l'a lancée.

Pour une référence strictement positive :
`économie (%) = 100 × (référence - candidat) / référence`.
Une valeur négative indique une augmentation. Calculer séparément tokens et coût.
Sans référence comparable, publier les valeurs disponibles sans pourcentage d'économie.

Exemple fictif : référence de 1 000 tokens ; candidat de 800 tokens puis correction
de 500 tokens. Le candidat totalise 1 300 tokens, soit une augmentation de 30 %.
Ces nombres illustrent le calcul et ne mesurent pas ce projet.

## Bilan proportionné

Reprendre le [format commun](token-sobriety.md#format-du-bilan-de-session). Dans une
tâche courte, regrouper les mesures indisponibles et les actions communes. Conserver
les champs du hook NR lorsqu'il est actif. La réponse finale doit rester compréhensible
sans lire les messages de progression.

Une revue vérifie les actes observés, le diff, les tests et la provenance des mesures.
Les tests du catalogue établissent la présence des règles ; les scénarios de `evals/`
permettent une évaluation des réponses. Aucun de ces contrôles ne garantit à lui seul
le respect systématique des règles par un modèle.
