# BP-AIR : décisions d’architecture applicables

Adapté de *BP-AIR — Bonnes pratiques pour des architectures informatiques responsables*,
Institut du Numérique Responsable / ISIT et contributeurs (notamment Vincent Courboulay,
Benjamin Duthil, Guillaume Gallon ; attribution complète dans le
[CITATION.cff source](https://github.com/Institut-du-Numerique-Responsable/BP-AIR/blob/f7b0f6b/CITATION.cff)).
Source consultée le 17 octobre 2026, révision `f7b0f6b` ; 18 fiches.
Licence : [CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/). Adaptation Green Codex du 17 octobre 2026 : reformulation, regroupement et ajout de preuves opérationnelles ; aucun soutien des auteurs à cette adaptation n’est présumé.

Les fiches consultées sont des documents de travail, souvent marqués « brouillon ».
Les seuils illustratifs du guide ne deviennent pas des obligations universelles ici.
Cette adaptation couvre les actions principales des 18 fiches, pas tous leurs exemples ou outils.

## Mode d’emploi

Appliquer le filtre de périmètre de `../SKILL.md` et les exigences de preuve de
[closing-summary.md](closing-summary.md). Ces règles servent à sélectionner un point
concret, pas à certifier un engagement entier. Les contrôles organisationnels ne sont
pas exécutés par le scanner statique. Une action commune à plusieurs référentiels se
vérifie une seule fois ; citer les correspondances utiles sans multiplier les constats.

### AIR-001 — Mandat

Source : [G1](https://github.com/Institut-du-Numerique-Responsable/BP-AIR/blob/f7b0f6b/docs/fiches/G1-mandat.md).

Action : Faire préciser qui porte la démarche, les décisions couvertes, les moyens et les limites du mandat.

Preuve : Mandat daté, responsable et budget ou temps attribué ; une adhésion à un organisme reste facultative.

### AIR-002 — Participation

Source : [G2](https://github.com/Institut-du-Numerique-Responsable/BP-AIR/blob/f7b0f6b/docs/fiches/G2-parties-prenantes.md).

Action : Associer métiers, utilisateurs, achats et équipes techniques concernés ; consigner leurs contraintes et arbitrages.

Preuve : Cartographie des acteurs, compte rendu et répartition des responsabilités.

### AIR-003 — Objectifs

Source : [G3](https://github.com/Institut-du-Numerique-Responsable/BP-AIR/blob/f7b0f6b/docs/fiches/G3-objectifs-odd.md).

Action : Choisir les priorités à partir des problèmes observés et des impacts attendus ; fixer une référence, une cible et une échéance.

Preuve : Fiche objectif avec calcul de l’indicateur, source et hypothèses ; une donnée absente reste inconnue.

### AIR-004 — Feuille de route

Source : [G4](https://github.com/Institut-du-Numerique-Responsable/BP-AIR/blob/f7b0f6b/docs/fiches/G4-feuille-de-route.md).

Action : Ordonner les actions selon impact attendu, effort, risques et dépendances, puis attribuer responsable et échéance.

Preuve : Plan financé ou moyens explicitement manquants ; revue des résultats et décisions.

### AIR-005 — Diagnostic

Source : [M1](https://github.com/Institut-du-Numerique-Responsable/BP-AIR/blob/f7b0f6b/docs/fiches/M1-diagnostic.md).

Action : Inventorier équipements, services et données utiles au périmètre ; mesurer un échantillon représentatif et recueillir les besoins.

Preuve : Inventaire daté, couverture de l’échantillon, méthode et données manquantes ; aucun score outil assimilé à une conformité.

### AIR-006 — Pilotage

Source : [M2](https://github.com/Institut-du-Numerique-Responsable/BP-AIR/blob/f7b0f6b/docs/fiches/M2-pilotage-kpi.md).

Action : Conserver un petit nombre d’indicateurs exploitables, avec unité, source, fréquence et responsable.

Preuve : Calcul reproductible, mesure par tâche et total sur une période ; coût et énergie restent distincts.

### AIR-007 — Conception de service

Source : [C1](https://github.com/Institut-du-Numerique-Responsable/BP-AIR/blob/f7b0f6b/docs/fiches/C1-eco-conception-services.md).

Action : Valider les 3U, fixer des budgets et tester les parcours essentiels sur les profils matériels retenus.

Preuve : Tests fonctionnels et budgets comparés avant/après ; réutiliser SERVICE-EFF-001, WEB-EFF-002 et la méthode 3U.

### AIR-008 — Données

Source : [C2](https://github.com/Institut-du-Numerique-Responsable/BP-AIR/blob/f7b0f6b/docs/fiches/C2-cycle-vie-donnees.md).

Action : Nommer le responsable des données, leur usage, leur source de référence et leur durée de conservation ; adapter stockage et purge.

Preuve : Inventaire, test d’expiration et de restauration ; autorisation préalable aux suppressions. Réutiliser DB-EFF-005.

### AIR-009 — IA sobre

Source : [C3](https://github.com/Institut-du-Numerique-Responsable/BP-AIR/blob/f7b0f6b/docs/fiches/C3-ia-sobre.md).

Action : Comparer une solution simple, un petit modèle et les autres candidats au même seuil de qualité ; borner contexte, appels et essais.

Preuve : Évaluations représentatives et ressources totales incluant reprises et exploitation. Ne présumer ni la supériorité de RAG ni celle de l’inférence sur l’entraînement ; réutiliser AI-EFF-002.

### AIR-010 — Flux et intégration

Source : [C4](https://github.com/Institut-du-Numerique-Responsable/BP-AIR/blob/f7b0f6b/docs/fiches/C4-dette-integration.md).

Action : Décrire les consommateurs, fréquences et volumes des échanges ; tester les contrats et retirer progressivement les flux devenus inutiles.

Preuve : Traces comparées à la cartographie, test de compatibilité, observation des traitements périodiques et retour arrière ; aucun retrait sur simple absence de propriétaire.

### AIR-011 — Accessibilité

Source : [C5](https://github.com/Institut-du-Numerique-Responsable/BP-AIR/blob/f7b0f6b/docs/fiches/C5-accessibilite.md).

Action : Inclure les besoins d’accès dans les critères d’achèvement et vérifier le parcours complet, y compris documents et erreurs.

Preuve : Tests clavier, technologies d’assistance et contrôles pertinents ; ne pas transformer un score automatisé en conformité RGAA.

### AIR-012 — Capacités

Source : [I1](https://github.com/Institut-du-Numerique-Responsable/BP-AIR/blob/f7b0f6b/docs/fiches/I1-infrastructures.md).

Action : Ajuster calcul, mémoire et stockage à la charge mesurée ; prévoir expiration des environnements temporaires et rétention des journaux.

Preuve : Mesures d’usage et test en charge ; vérifier continuité et récupération avant arrêt. Réutiliser INFRA-EFF-001 et OPS-EFF-001.

### AIR-013 — Achats

Source : [I2](https://github.com/Institut-du-Numerique-Responsable/BP-AIR/blob/f7b0f6b/docs/fiches/I2-achats-responsables.md).

Action : Vérifier d’abord réemploi et besoin, puis demander des preuves adaptées de réparabilité, durée de support et conditions sociales.

Preuve : Comparaison du coût complet, certificats applicables et critères vérifiables ; le choix et les engagements contractuels restent aux personnes habilitées.

### AIR-014 — Reprise

Source : [I3](https://github.com/Institut-du-Numerique-Responsable/BP-AIR/blob/f7b0f6b/docs/fiches/I3-resilience.md).

Action : Définir le délai de reprise et la perte de données acceptable avec le métier ; choisir une architecture proportionnée au risque.

Preuve : Exercice isolé de panne, restauration et retour à la normale avec résultats comparés aux objectifs ; ne pas réduire la redondance sans analyse.

### AIR-015 — Maturité fournisseur

Source : [V1](https://github.com/Institut-du-Numerique-Responsable/BP-AIR/blob/f7b0f6b/docs/fiches/V1-maturite-parties-prenantes.md).

Action : Distinguer la demande d’information préalable de la sélection contractuelle ; poser des questions ouvertes puis examiner les pratiques actuelles.

Preuve : Réponses précises, certificats datés, revue croisée et débriefing ; utiliser stakeholder-maturity.md.

### AIR-016 — Réversibilité

Source : [V2](https://github.com/Institut-du-Numerique-Responsable/BP-AIR/blob/f7b0f6b/docs/fiches/V2-souverainete.md).

Action : Recenser les dépendances fournisseur, les contraintes de localisation et le coût de sortie ; essayer un export puis un import ailleurs.

Preuve : Données réutilisables, durée, coût et pertes observées ; une clause seule ne prouve pas la réversibilité.

### AIR-017 — Exigences

Source : [D1](https://github.com/Institut-du-Numerique-Responsable/BP-AIR/blob/f7b0f6b/docs/fiches/D1-conformite.md).

Action : Attribuer les exigences applicables au bon périmètre, avec date de vérification et preuves à chaque jalon.

Preuve : Table de suivi et résultats de revue ; faire examiner les conclusions juridiques par une personne compétente, sans déduire la conformité d’un dépôt.

### AIR-018 — Communication

Source : [D2](https://github.com/Institut-du-Numerique-Responsable/BP-AIR/blob/f7b0f6b/docs/fiches/D2-communiquer-valoriser.md).

Action : Expliquer les progrès avec leur référence, périmètre, période et incertitude ; distinguer mesures, estimations et objectifs.

Preuve : Chaque affirmation renvoie à un résultat contrôlable ; pas de label ni de gain carbone inventé ; publication seulement autorisée.
