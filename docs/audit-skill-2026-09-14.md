# Audit de cohérence et de pertinence du skill

Date : 14 septembre 2026. Version examinée : `9b9e93f3671ba44ded527c9671002df7f3b33c96`.
Constats historiques avant correction. Voir le suivi ci-dessous pour les changements ultérieurs.

## Périmètre et méthode

Lecture de `green-codex/SKILL.md`, des six références et des métadonnées de découverte.
Les familles examinées couvrent service, code, API, web, données, infrastructure,
exploitation, réseau, matériel, IA, mesure, architectures, langages/frameworks,
accessibilité, charte, pratiques Codex et 3U. Examen complémentaire du scanner,
de l'évaluateur, du catalogue et des évaluations enregistrées.

Inventaire : 159 identifiants dans `rules.md`, 10 pour la charte et 14 pour les
pratiques Codex, soit 183 identifiants uniques. Le volume seul ne constitue pas
un défaut : il faut surtout éviter de charger ou imposer des règles non pertinentes.

Vérifications exécutées : les quatre suites Python du paquet, du scanner, du
catalogue et de liaison des revues passent. Deux faux positifs ont néanmoins été
reproduits sur des fichiers temporaires. Un agent indépendant a également répondu
à un cas SQL sans accéder au catalogue ni aux réponses antérieures.

Les sources externes n'ont pas été toutes revalidées dans leur édition actuelle.
Cet audit porte sur la cohérence et les comportements observables du skill,
pas sur une certification des référentiels ni sur tous les langages en production.

## Constats prioritaires

### 1. Important — règle SQL trop absolue, faux positif confirmé

Emplacements : `green-codex/references/rules.md:126` et
`green-codex/scripts/check_sobriety.py:57`.

L'interdiction de `SELECT *` ne distingue pas une projection de colonnes d'un
test d'existence. Le scanner retourne `FAIL DB-EFF-001` pour un `SELECT EXISTS`
contenant une sous-requête `SELECT *`, alors que cette forme ne demande pas de
transférer toutes les colonnes. La remplacer par `1` ne démontre aucune économie.

L'essai indépendant a correctement recommandé de ne rien changer, en écartant
explicitement la règle générale. Le bon raisonnement vient ici malgré une règle
du skill. Corriger sa portée et ajouter un contre-exemple au scanner ; garder
un test positif pour les projections réellement excessives. Aucun benchmark
PostgreSQL n'a été exécuté pendant cet audit.

### 2. Important — le scanner traite du texte comme du code rendu

Emplacement : `green-codex/scripts/check_sobriety.py:62`.

Le parseur HTML reçoit tout le contenu JSX/TSX sans retirer les commentaires et
chaînes JavaScript. Un commentaire TSX contenant un exemple de vidéo automatique
déclenche `FAIL WEB-EFF-004`, même lorsque le composant ne rend qu'un paragraphe.
Le faux positif est reproduit. Ce résultat peut bloquer une CI sans défaut réel.

Limiter les échecs bloquants aux syntaxes interprétées avec confiance ; masquer
les zones non exécutables ou demander une revue lorsque l'analyse est ambiguë.
Tester commentaires, chaînes, attributs dynamiques et médias réellement rendus.

### 3. Important — l'évaluateur mélange conformité de forme et intelligence

Emplacement : `green-codex/scripts/run_evals.py:87`.

En cas de mot ou d'identifiant absent, la revue sémantique n'est pas consultée.
Le résultat final reste `FAIL` même si cette revue valide le fond. Cela est déjà
visible dans `evals/runs/2026-09-14-three-u/README.md` : la réponse révisée passe
les quatre critères sémantiques mais échoue faute d'identifiants littéraux.

Il est légitime de vérifier la traçabilité, mais elle doit avoir un résultat
distinct. Afficher séparément qualité du raisonnement, preuves, respect du périmètre
et forme attendue. Ne pas inciter l'agent à accumuler des identifiants pour réussir.
Les mots interdits détectés par sous-chaîne doivent aussi tenir compte des négations.

### 4. Important — plusieurs obligations contredisent la proportionnalité

Emplacements : `green-codex/references/rules.md:68`, `:79`, `:82`, `:369` et
`green-codex/references/usage-practices.md:20`.

Exemples : test de borne et de pire cas pour chaque boucle, au moins deux métriques
pour une modification sensible aux performances, coût mesuré pour toute nouvelle
dépendance, benchmark avant toute optimisation du compilateur, fork avant toute
exploration différente. Leur formulation est plus systématique que le protocole
de mesure, qui demande la preuve la moins coûteuse capable de résoudre la décision.

Ces règles peuvent provoquer des tests ou manipulations sans bénéfice démontré.
Définir le déclencheur : données externes non bornées, chemin critique, régression,
risque ou décision récurrente. Autoriser une inspection suffisante pour les cas
simples ; choisir les métriques utiles au risque au lieu d'un nombre obligatoire.
Une configuration de compilation standard ne doit pas exiger une étude préalable.

### 5. Moyen — la charte reste trop largement routée

Emplacement : `green-codex/SKILL.md:48`.

Les lignes de routage « AI features or inference » et « Responsible AI design,
procurement, rollout, use » conduisent largement vers la charte, tandis que le
paragraphe suivant demande de la consulter sur demande ou pour un problème pertinent.
Ce n'est pas une contradiction totale, mais deux instructions de granularité
différente peuvent réintroduire la charge que le recentrage 3U devait éviter.

Séparer explicitement valeur/adoption/parcours (3U), optimisation technique IA
(règles AI-EFF) et risques ou audit de charte (sections ciblées de la charte).
Vérifier ce routage avec une petite modification IA sans enjeu organisationnel.

### 6. Moyen — des doublons augmentent le coût sans clarifier les décisions

Emplacements : `green-codex/references/rules.md:105`, `:110`, `:393`, `:399`,
`:488` et `:492`.

API-EFF-001 et API-EFF-003 répètent les limites de pagination. Les règles Python
002 et 004 recouvrent largement le choix de bibliothèques natives après profilage.
Les règles Solid 001 et 003 répètent la limitation des effets réactifs et des
mises à jour DOM. Les sections génériques frontend/backend/langages répètent aussi
une partie des familles identifiées.

Conserver une source par décision, référencer les règles communes et réserver les
variantes de langage aux détails réellement spécifiques. Préserver les anciens
identifiants comme alias lors d'une consolidation pour ne pas casser les archives.

### 7. Moyen — un arbitrage de compression est formulé avec des unités incompatibles

Emplacement : `green-codex/references/rules.md:140`.

La condition compare le coût CPU et la latence aux économies de stockage et de
réseau sans métrique commune. Des millisecondes ne sont pas « inférieures » à des
octets. Définir plutôt les budgets de latence/CPU à respecter, mesurer les octets
économisés et comparer l'énergie ou le coût total seulement si un modèle explicite
le permet. Le protocole de mesure contient déjà les distinctions nécessaires.

### 8. Moyen — la couverture comportementale est encore trop étroite

Emplacements : `evals/cases.json`, `green-codex/scripts/test_evals.py` et `evals/runs/`.

Les 22 scénarios mentionnent 45 identifiants distincts parmi les 183. Ce compte
mesure uniquement leur présence dans les attentes, pas leur exécution ou leur
importance. Huit scénarios n'ont que les critères sémantiques génériques.
Les archives contiennent sept réponses couvrant seulement quatre scénarios
distincts. Le nouvel essai SQL de cet audit est séparé de ces archives.

Les tests de paquet passent, mais ne démontrent pas la pertinence globale des
conseils. Ajouter quelques contre-exemples ciblés : ne rien modifier, besoin absent,
service rarement utilisé mais essentiel, arbitrage accessibilité/performance,
SQL valide et résultat négatif de mesure. Tester plusieurs formulations, notamment
en français, avant d'affirmer une robustesse générale. Ne pas viser mécaniquement
un test par règle au prix d'une batterie coûteuse et peu discriminante.

## Ce qui mérite d'être conservé

- Distinction claire entre données observées, estimations, proxies et conformité.
- Prise en compte des corrections humaines, tentatives, coûts totaux et effets rebond.
- Absence de langage, modèle, fournisseur ou technologie présenté comme toujours meilleur.
- Trois décisions séparées pour les 3U, sans seuil universel d'adoption ni score moyen.
- Préservation des données, de l'accessibilité et des autorisations de l'utilisateur.
- Réponses d'évaluation authentiques, échecs publiés et revues liées à leurs entrées.

Pour l'utilité, renforcer encore le lien entre besoin confirmé et bénéfice recherché :
accélérer une tâche n'établit pas que cette tâche est nécessaire. Le skill dispose
déjà de cette idée dans SERVICE-EFF-001 ; la fiche 3U doit y renvoyer clairement
avant la comparaison de temps et de qualité. C'est un raffinement, pas une absence
totale de prise en compte du besoin.

## Ordre de correction recommandé

1. Corriger les deux faux positifs et séparer les résultats lexicaux et sémantiques.
2. Rendre conditionnelles les obligations excessives et clarifier le routage 3U/charte.
3. Consolider les doublons, préciser l'arbitrage de compression et tester quelques contre-exemples.

Verdict : base cohérente et prudente, mais fiabilité de l'application inégale.
Le prochain progrès doit venir de règles mieux délimitées et de meilleurs tests
de jugement, pas d'un catalogue plus long. Aucun score global d'« intelligence »
n'est attribué : les observations disponibles ne permettraient pas de le justifier.

## Suivi des corrections

Les défauts SQL et JSX ont été corrigés avec tests de régression, y compris les
parenthèses SQL et l'ordre des attributs JSX. Les médias des templates restent
soumis à une revue, faute de compilateur JavaScript/Vue dans le scanner.

L'évaluateur affiche toujours les résultats de forme et de fond séparément.
Le code de sortie suit la revue sémantique liée aux preuves ; `--strict-format`
ajoute les exigences littérales. Les revues manquantes ou modifiées ne passent pas.

Les obligations disproportionnées sont conditionnées au risque et à la décision.
Trois doublons deviennent des alias compatibles ; la compression compare des
métriques cohérentes. Le routage technique IA/charte est séparé, et les 3U demandent
explicitement de confirmer le besoin avant de comparer l'efficacité.

Le catalogue compte désormais 25 scénarios avec critères sémantiques spécifiques.
Trois contre-exemples ont été ajoutés. Leur présence ne signifie pas qu'ils ont
tous été exécutés par un agent ; la couverture comportementale reste une limite
à améliorer progressivement. Les réponses et métadonnées historiques sont conservées.
