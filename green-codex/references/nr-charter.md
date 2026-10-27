# Charte Numérique Responsable : mise en pratique

Source : [Charte NR de l’Institut du Numérique Responsable / ISIT](https://charter.isit-europe.org/?lang=fr_FR),
page publique consultée le 17 octobre 2026. Les cinq axes sont repris comme repères ; les
consignes et preuves ci-dessous sont rédigées pour Green Codex, sans recopier les engagements.
La page décrit un engagement volontaire, pas un audit ni une certification.
Cette charte NR est distincte de la [charte IA](responsible-ai-charter.md).

## Mode d’emploi

Appliquer le filtre de périmètre de `../SKILL.md` et les exigences de preuve de
[closing-summary.md](closing-summary.md). Ces règles servent à sélectionner un point
concret, pas à certifier un engagement entier. Les contrôles organisationnels ne sont
pas exécutés par le scanner statique. Une action commune à plusieurs référentiels se
vérifie une seule fois ; citer les correspondances utiles sans multiplier les constats.

### NR-CHARTER-001 — Environnement

Action : Sur le service concerné, choisir une action qui réduit un impact identifié sur son cycle de vie, puis vérifier son effet et les éventuels transferts.

Preuve : Comparaison datée à service équivalent ; limites de mesure explicites. Réutiliser CODE-EFF-012 et MEASURE-EFF-004.

### NR-CHARTER-002 — Accès durable

Action : Vérifier que le parcours essentiel reste utilisable par les personnes concernées, y compris avec équipement ancien ou connexion limitée.

Preuve : Essai de parcours représentatif et obstacles relevés. Réutiliser SERVICE-EFF-002 et SERVICE-EFF-006.

### NR-CHARTER-003 — Éthique

Action : Repérer les données et choix pouvant affecter les personnes ; prévoir protection, recours et responsabilité.

Preuve : Examen des accès, information comprise et traitement d’une réclamation simulée.

### NR-CHARTER-004 — Résilience

Action : Attribuer la continuité de la démarche et préparer une reprise adaptée au service.

Preuve : Responsable nommé, revue prévue et exercice de restauration ou de fonctionnement dégradé.

### NR-CHARTER-005 — Pratiques collectives

Action : Expliquer les actions NR dans le travail quotidien et vérifier leur appropriation.

Preuve : Support adapté, exercice pratique et retour des participants ; diffuser seulement avec autorisation.

## Matrice d’application dans Codex

Cette matrice est une déclinaison éditoriale Green Codex, pas une liste d’exigences
techniques publiée par la charte. Elle ne crée pas de nouveaux identifiants : citer
l’axe `NR-CHARTER-*` et, pour le code, la règle technique précise. Une preuve peut
soutenir plusieurs axes mais ne se compte qu’une fois. Ne conclure `PASS` que pour
le point et le périmètre examinés, jamais pour l’engagement organisationnel entier.

### Ce que Codex peut réellement faire

| Niveau | Attendu | Ce qui ne l’est pas | Preuve ou limite |
| --- | --- | --- | --- |
| Exécution technique | Lire, modifier et tester dans les outils disponibles et le périmètre autorisé. | Supposer un accès, installer un outil ou agir sur la production sans l’autorisation nécessaire. | Résultat observé, fichier ou configuration et commande réellement exécutée. |
| Analyse de preuves | Examiner des documents fournis, préparer un questionnaire, une décision ou un plan. | Déduire une pratique réelle de la seule présence d’une procédure ou d’une promesse. | Document, date, périmètre et constat ; réalisation externe non observée = `REVIEW_REQUIRED`. |
| Décision humaine ou organisationnelle | Identifier le responsable, les données nécessaires et préparer les éléments de décision. | Signer, certifier, attribuer un marché, attester une formation ou annoncer une conformité juridique à la place des personnes habilitées. | Décision humaine ou preuve externe requise ; Codex ne la fabrique pas. |
| Hors tâche ou sans moyen de vérification | Exclure avec une raison dans un audit ; signaler un test pertinent mais inaccessible. | Charger tous les guides ou créer un chantier organisationnel pour une correction locale. | Distinguer « non applicable » de « applicable mais non vérifié ». |

Cette distinction s’applique à **tout le catalogue** :

- `LANG-*`, `CODE-*`, `API-*`, `DB-*`, `WEB-*`, `NET-*`, `ARCH-*` : vérifiables seulement
  sur le code, les configurations, les parcours et les environnements accessibles.
- `INFRA-*`, `OPS-*`, `HW-*`, `MEASURE-*`, `AI-EFF-*` : mélangent contrôles techniques
  et données externes ; facture, matériel, énergie et conditions fournisseur ne sont pas
  déductibles d’un langage, d’un dépôt ou d’un nombre de tokens.
- `SERVICE-*`, `NR-CHARTER-*`, `AIR-*`, `STAKE-*`, `RIA-*`, `AI-CHARTER-*` : sélectionner
  le point concret. Codex peut tester une partie technique et examiner les pièces ;
  gouvernance, participation, achats, formation et effets sociaux demandent des preuves humaines.
- `USAGE-CODEX-*` : appliquer uniquement aux moyens réellement disponibles dans l’hôte.
  Une commande CLI documentée n’existe pas nécessairement dans l’application ou l’API utilisée.
  Ne pas simuler un hook, un réglage de modèle, une compaction ou une mesure inaccessible.

### Les cinq axes, quel que soit le langage

Chaque ligne « langage » ci-dessous se combine avec ces cinq axes. Il n’est pas nécessaire
de répéter cinq fois chaque technique : retenir les axes effectivement touchés par la tâche.

| Axe | Attendu dans une tâche de code | À éviter | Preuve proportionnée |
| --- | --- | --- | --- |
| `NR-CHARTER-001` | Éviter du travail inutile observé ; borner les ressources et réutiliser l’existant adapté. | Optimiser sans problème identifié ; déclarer une technologie verte ; assimiler temps ou coût à du carbone. | Diff, test de borne ou profil selon le risque ; mesure comparative pour un gain annoncé. |
| `NR-CHARTER-002` | Préserver les interfaces, formats, erreurs compréhensibles et profils matériels utiles. Pour une interface humaine, vérifier les besoins d’accès concernés. | Retirer une alternative accessible ou imposer une migration matérielle sans justification. Imposer un audit de lecteur d’écran à une bibliothèque sans interface humaine. | Test de compatibilité ou de parcours ; expliquer les profils non testés. |
| `NR-CHARTER-003` | Minimiser les données exposées ; respecter autorisations, licences et information des personnes. | Journaliser des secrets, copier un corpus sans examiner ses droits ou laisser une optimisation contourner un contrôle d’accès. | Cas d’accès refusé, inspection des logs et vérification de provenance selon la modification. |
| `NR-CHARTER-004` | Gérer erreurs, annulation, reprise et nettoyage des ressources à la bonne échelle. | Réessayer sans limite, masquer les échecs ou imposer une architecture redondante à un script ponctuel. | Test de panne ou d’annulation ; pour une modification documentaire, vérifier ses liens et sa cohérence suffit. |
| `NR-CHARTER-005` | Expliquer le choix utile, les tests et les limites ; documenter ce qui facilite la maintenance. | Ajouter un discours NR générique ou prétendre que l’utilisateur est formé parce qu’une explication a été donnée. | Commentaire utile, exemple exécutable ou bilan final factuel ; appropriation réelle à vérifier séparément. |

### Déclinaison par langage et framework

Les preuves suivantes sont des exemples à choisir selon le changement, pas des commandes
à exécuter systématiquement. Les règles `LANG-*` détaillées restent dans `rules.md`.
Les exemples concernent surtout les axes environnement et résilience ; les protections
transversales d’accès, d’éthique et de transmission ci-dessus restent applicables.

| Contexte et règles | Attendu | À éviter | Vérification concrète |
| --- | --- | --- | --- |
| Python — `LANG-PYTHON-001`, `LANG-PYTHON-003` | Lire les gros volumes par lots et fermer fichiers et clients même en cas d’erreur. | Charger une entrée non bornée ; remplacer Python par principe. Un petit fichier borné peut être lu intégralement. | Essai de volume représentatif, mémoire si pertinente et erreur de lecture. |
| JavaScript / TypeScript navigateur — `LANG-JS-002`, `LANG-JS-004` | Annuler les requêtes périmées et libérer timers et écouteurs. | Polling sans fin ou optimisations qui perturbent focus et clavier. | Changement rapide de saisie, démontage du composant et observation des appels restants. |
| Node.js — `LANG-JS-003`, `LANG-JS-004` | Borner la concurrence et traiter les charges volumineuses en flux. | Charger toutes les réponses ou appliquer des règles DOM à un serveur sans DOM. | Requête interrompue, limite de taille et maximum d’appels simultanés. |
| Java — `LANG-JAVA-001`, `LANG-JAVA-002` | Borner pools et files ; fermer les ressources ; ajuster la mémoire à partir de la charge. | Ajouter des pools d’objets ou modifier le GC sans problème démontré. | Saturation, fermeture après exception et profil d’allocation si nécessaire. |
| Kotlin — `LANG-KOTLIN-001`, `LANG-KOTLIN-002` | Donner une durée de vie aux coroutines et borner les canaux. | Lancer des tâches sans propriétaire ; imposer des séquences à de petites collections. | Annulation parent/enfants et comportement d’un canal plein. |
| Scala — `LANG-SCALA-001`, `LANG-SCALA-002` | Choisir itération, matérialisation et parallélisme selon le volume. | Empiler les transformations ou activer le parallélisme sans bénéfice observé. | Comparaison à données et résultat identiques, mémoire et temps si optimisation. |
| Rust — `LANG-RUST-001`, `LANG-RUST-002` | Éviter les copies inutiles et borner tâches et canaux tout en préservant la propriété des données. | Introduire du code non sûr pour un gain hypothétique. | Test de charge bornée, annulation et profil d’allocation si nécessaire. |
| C — `LANG-C-001`, `LANG-C-002` | Définir limites et propriété des buffers ; libérer les ressources sur tous les chemins. | Débordement, fuite ou désactivation des contrôles pour gagner du temps. | Entrées limites, échec d’allocation et sanitizer adapté si disponible. |
| C++ — `LANG-CPP-001`, `LANG-CPP-003` | Utiliser RAII et des tâches bornées avec arrêt explicite. | Copies coûteuses non justifiées ou thread créé par élément sans limite. | Exceptions, arrêt des workers et test de durée de vie mémoire. |
| C# / .NET — `LANG-CSHARP-001`, `LANG-CSHARP-005` | Filtrer et paginer avant de matérialiser une requête ; rester asynchrone de bout en bout ; réutiliser les clients HTTP. | Bloquer sur une tâche ; charger une table entière puis filtrer en mémoire. | Requêtes SQL générées et nombre de connexions sous charge. |
| Swift — `LANG-SWIFT-001`, `LANG-SWIFT-003` | Arrêter capteurs et timers dès qu’ils ne servent plus ; garder le thread principal pour l’interface. | Capteur ou timer actif après la fermeture de l’écran. | Profil d’énergie Xcode sur un appareil représentatif. |
| Go — `LANG-GO-001`, `LANG-GO-003` | Propager l’annulation et fermer les réponses ; borner goroutines et canaux. | Goroutine sans sortie ou buffer réutilisé avec une durée de vie incorrecte. | Requête annulée, arrêt des workers et test de fuite pertinent. |
| PHP — `LANG-PHP-001`, `LANG-PHP-002` | Parcourir imports et exports volumineux par lots ; mesurer les caches utiles. | Rendu de collections non bornées ou cache activé sans politique de validité. | Import interrompu, mémoire de pointe et contenu exporté complet. |
| Ruby — `LANG-RUBY-001`, `LANG-RUBY-002` | Traiter les grandes relations par lots et borner jobs et reprises. | Charger toutes les lignes ou laisser un job conserver sa connexion après erreur. | Compte de requêtes, échec de job et restitution de la connexion. |
| SQL — `LANG-SQL-001`, `LANG-SQL-002` | Limiter les données récupérées et choisir transaction et index selon la requête. | Index systématique, pagination incohérente ou lecture complète accidentelle. `EXISTS (SELECT *)` n’est pas une projection inutile. | Plan de requête lorsque pertinent, résultats, verrous et aller-retour sur une charge représentative. |
| PL/SQL — `LANG-PLSQL-001`, `LANG-PLSQL-003` | Utiliser des traitements ensemblistes ou lots bornés avec reprise définie. | Curseur non fermé, collecte sans borne ou commit par ligne sans justification. | Interruption puis reprise, doublons, mémoire PGA et redo si accessibles. |
| Julia — `LANG-JULIA-001`, `LANG-JULIA-002` | Profiler les allocations et distinguer compilation, échauffement et exécution. | Mutation risquant de modifier le résultat ou benchmark qui masque le démarrage. | Résultats identiques, allocations et phases de temps séparées. |
| Nim — `LANG-NIM-001`, `LANG-NIM-002` | Borner génération de code et allocations ; fermer les ressources. | Changer de gestion mémoire sur une supposition de sobriété. | Taille produite et chemins de nettoyage ; mesure si changement de stratégie. |
| Zig — `LANG-ZIG-001`, `LANG-ZIG-002` | Rendre l’allocateur et les limites explicites. | Ignorer l’échec d’allocation ou multiplier les copies sans besoin. | Allocation refusée, libération et limites de buffer. |
| Bash / Zsh / Tcsh — `LANG-SHELL-002`, `LANG-SHELL-003`, `LANG-SHELL-006` | Préserver les noms de fichiers, borner reprises et temporaires, gérer les erreurs selon le shell. | Copier les options strictes de Bash dans un autre shell ; supprimer des données sans autorisation. | Noms avec espaces et caractères spéciaux, commande en échec et nettoyage des seuls temporaires créés. |
| HTML — `LANG-HTML-001`, `LANG-HTML-002` | Employer une structure sémantique et des contrôles natifs ; adapter les médias. | Widget lourd remplaçant inutilement un contrôle utilisable ; supprimer les alternatives textuelles. | Parcours clavier, libellés et chargement des médias sur profil cible. |
| CSS — `LANG-CSS-001`, `LANG-CSS-002` | Limiter le style inutile et respecter les préférences de mouvement. | Effets permanents, suppression du focus ou retrait d’un style utilisé dans un état rare. | Focus, mouvement réduit, zoom et états d’erreur ; poids de production si modifié. |
| React / Preact — `LANG-REACT-003`, `LANG-PREACT-003` | Stabiliser les identités et cibler les rendus réellement coûteux. | Mémoïsation systématique ou virtualisation rendant la liste inaccessible. | Profil de rendu lorsque nécessaire et parcours clavier sur la liste. |
| Vue — `LANG-VUE-001`, `LANG-VUE-003` | Cibler la réactivité et nettoyer les observateurs. | Observation profonde d’un gros corpus immuable sans besoin. | Mises à jour attendues et absence d’observation après démontage. |
| Angular — `LANG-ANGULAR-001`, `LANG-ANGULAR-003` | Suivre l’identité des éléments et terminer les abonnements. | Modifier la détection des changements sans tester les mises à jour visibles. | Évolution réelle des données, rendu correct et destruction du composant. |
| Svelte — `LANG-SVELTE-001`, `LANG-SVELTE-003` | Limiter les dépendances réactives et la durée des abonnements. | Supposer que le compilateur rend toute implémentation sobre. | Mises à jour et nettoyage ; taille réellement produite si comparée. |
| Astro — `LANG-ASTRO-001`, `LANG-ASTRO-003` | Hydrater uniquement les interactions nécessaires au bon moment. | Retarder une interaction essentielle au nom d’une réduction des octets. | JavaScript transféré et disponibilité du parcours, avec repli pertinent. |
| Solid — `LANG-SOLID-001`, `LANG-SOLID-002` | Limiter les effets aux données nécessaires et conserver les identités. | Effets globaux déclenchés pour des modifications locales. | Nœuds mis à jour et parcours sur terminal cible. |
| Autre langage | Appliquer les règles techniques transversales et les conventions vérifiées du projet. | Inventer un identifiant spécialisé ou imposer un changement de langage. | Test du comportement concerné ; préciser les outils indisponibles. |

### Questions et productions en langage naturel

Ces cas concernent le comportement de l’assistant, pas une certification de son infrastructure.
Ils s’appliquent lorsque Green Codex est invoqué ou retenu pour la tâche. Ils ne forcent pas
son déclenchement pour toute conversation. Une réponse utile peut être longue si la demande
l’exige. Ne jamais sacrifier exactitude, accessibilité ou vérification à la brièveté.

| Contexte et axes concernés | Attendu | À éviter | Preuve ou limite |
| --- | --- | --- | --- |
| Question factuelle simple — `NR-CHARTER-001`, `NR-CHARTER-005` | Répondre directement à partir des informations fiables disponibles. | Explorer le dépôt, lancer le scanner ou déléguer sans utilité. | Réponse qui couvre la question ; aucune mesure de gain carbone déduite du nombre d’outils. |
| Information actuelle, incertaine ou recherche demandée — `NR-CHARTER-003`, `NR-CHARTER-004` | Vérifier les sources pertinentes, dates et limites ; utiliser le web quand les instructions l’exigent. | Éviter une recherche nécessaire au nom de la sobriété ; inventer une source ou cacher un accès refusé. | Liens effectivement consultés et distinction entre faits, inférences et inconnues. |
| Explication / apprentissage — `NR-CHARTER-002`, `NR-CHARTER-005` | Adapter vocabulaire, exemple et profondeur au besoin ; expliciter les notions nécessaires. | Jargon, simplification trompeuse ou affirmation que la lecture prouve la compétence acquise. | Explication cohérente et exemple vérifiable ; demander un retour si une évaluation pédagogique est souhaitée. |
| Résumé / reformulation — `NR-CHARTER-002`, `NR-CHARTER-003` | Préserver conclusions, conditions, incertitudes et attribution utiles du texte source. | Supprimer une nuance décisive, ajouter des faits ou prétendre que reformuler efface le droit d’auteur. | Comparaison au texte fourni et signalement des passages non disponibles. |
| Rédaction — `NR-CHARTER-003`, `NR-CHARTER-005` | Respecter audience, objectif et format ; distinguer brouillon et publication autorisée. | Statistiques ou citations inventées ; publication ou envoi non demandé. | Texte conforme au brief, sources pour les affirmations qui le nécessitent. |
| Recommandation / comparaison — `NR-CHARTER-001`, `NR-CHARTER-003` | Comparer les alternatives sur le même besoin et déclarer critères et hypothèses. | Recommandation universelle ou classement environnemental sans données comparables. | Tableau ou raisonnement vérifiable ; mesures manquantes explicitement inconnues. |
| Données personnelles ou confidentielles — `NR-CHARTER-003` | Ne traiter et transmettre que ce qui est nécessaire et autorisé ; anonymiser les exemples si possible. | Coller un document confidentiel dans une recherche publique ou inférer des attributs sensibles. | Périmètre des données utilisées et destinataires autorisés ; ne pas exposer les données dans le bilan. |
| Plan d’action organisationnel — `NR-CHARTER-004`, `NR-CHARTER-005` | Préparer actions, responsabilités à confirmer, échéances et preuves attendues. | Déclarer le plan réalisé, les personnes formées ou l’organisation conforme. | Livrable clairement présenté comme proposition ; réalisation externe à vérifier. |
| Travail long / outils — `NR-CHARTER-001`, `NR-CHARTER-004` | Réutiliser les résultats encore valides et choisir des appels utiles à la décision. | Refaire la même exploration, multiplier les agents ou cacher un échec pour conclure plus vite. | Résultats consultables, contrôles proportionnés et limites de reprise documentées. |

### Bilan attendu et exceptions

Pour une tâche simple, une phrase factuelle suffit lorsque le skill demande un bilan.
Ne créer un registre JSON ou lancer `nr_summary.py` que pour une clôture structurée où
les contrôles statiques ont un périmètre pertinent. Une question sans fichier à scanner
peut recevoir un bilan textuel : le script ne prouve pas la qualité d’une réponse en langage naturel.

Exemple code : « `NR-CHARTER-004` / `LANG-JS-004` : requête annulée lors du changement de
page ; test d’annulation réussi. Gain énergétique non mesuré. »

Exemple rédaction : « `NR-CHARTER-003` : résumé vérifié contre le texte fourni ; incertitudes
et attribution conservées. Aucune évaluation de conformité organisationnelle réalisée. »

Si aucun point NR matériel n’a été appliqué, le dire brièvement sans inventer une action.
Un budget, un test, une recherche ou une explication plus longue peut être nécessaire :
justifier le choix par le besoin et le risque. Les exigences de sécurité, d’accessibilité,
d’exactitude et les instructions de l’utilisateur priment sur une réduction arbitraire de moyens.
