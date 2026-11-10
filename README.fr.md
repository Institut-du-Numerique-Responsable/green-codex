# Green Codex

[English](README.md) | **Français**

[![Version](https://img.shields.io/github/v/release/Institut-du-Numerique-Responsable/green-codex?sort=semver)](https://github.com/Institut-du-Numerique-Responsable/green-codex/releases)
[![CI](https://github.com/Institut-du-Numerique-Responsable/green-codex/actions/workflows/validate.yml/badge.svg)](https://github.com/Institut-du-Numerique-Responsable/green-codex/actions/workflows/validate.yml)
[![Licence](https://img.shields.io/badge/license-Apache--2.0%20%2B%20CC%20BY%204.0%20%2B%20CC%20BY--SA%204.0-yellow.svg)](LICENSE)
[![INR](https://img.shields.io/badge/INR-Institut%20du%20Num%C3%A9rique%20Responsable-4CAF50?logo=leaf&style=flat)](https://institutnr.org/)

Green Codex est un skill Codex qui applique les pratiques du Green IT et du Numérique
Responsable pendant la conception, le développement, la revue ou l'audit de logiciels
et de services numériques.

Il condense les recommandations du RGESN, du GR491, d'Opquast et du RGAA en une démarche
pratique pour Codex. Les sigles officiels restent inchangés. Il contient aussi des
adaptations délimitées de la charte NR, de BP-AIR, du guide de maturité des parties
prenantes et de RIA31. L'[inventaire des sources](green-codex/references/sources.md)
précise leur provenance et les limites de leur couverture.

La démarche est présentée sur le site de l'INR :
[Écoconcevoir avec un assistant de code](https://institutnr.org/ecoconcevoir-avec-un-assistant-de-code).

La version actuelle du paquet est `1.0.0` (voir [`VERSION`](VERSION)). Les identifiants de
règles comme `CODE-EFF-*` et `LANG-*` appartiennent à ce projet. Ils servent à orienter
l'analyse et le travail technique ; ce ne sont ni des numéros de critères officiels ni un
score de conformité.

La documentation technique du dossier `green-codex/references/` est rédigée en anglais ou en
français selon le fichier. Ce README en français en présente le contenu.

## Expression dans Codex et ChatGPT

Green Codex applique des [règles d'expression et de rédaction des messages de commit](green-codex/references/expression.md)
dans toutes les langues. Le skill charge cette référence pour chaque tâche. Pour ChatGPT,
fournissez les consignes autonomes de ce fichier comme contexte de conversation. Une
modification du dépôt ne met pas à jour automatiquement les instructions d'un compte. Ces
règles sont des conventions éditoriales du projet ; les réponses réelles doivent être
relues.

## Ce que couvre le skill

Les [règles de sobriété des tokens](green-codex/references/token-sobriety.md) couvrent
NR-TOK-001 à NR-TOK-030 pour les agents de développement, dont Codex, Claude Code et
Mistral Vibe. Elles définissent des garde-fous obligatoires, des recommandations par
défaut, des actions qui dépendent des capacités de l'outil et un compte rendu de session
concis. Une économie de tokens ou de coût exige des mesures comparables ; elle ne prouve
pas une économie environnementale.

Réduire les tokens et les appels inutiles contribue au Numérique Responsable en
limitant les traitements mobilisés pour un même résultat, tout en préservant la qualité ;
le gain environnemental réel dépend du modèle, de l'infrastructure et de l'usage.

Le [guide d'application dans Codex](green-codex/references/codex-token-sobriety.md) traite
des recherches ciblées, des preuves périmées, de la compaction, du cache, de la délégation
à des agents, des critères d'acceptation et des limites de mesure, avec des sources
officielles et un exemple complet.

- écoconception numérique et logicielle ;
- efficacité énergétique, des données, du stockage, du réseau et de l'infrastructure ;
- interfaces accessibles et résilientes ;
- usage responsable de l'IA : taille du modèle, contexte, cache et minimisation des données ;
- 15 pratiques d'usage responsable de Codex : contexte, consignes, instructions durables,
  vérification et calcul proportionné ;
- audits fondés sur des preuves, avec sévérité, niveau de confiance et étapes de vérification ;
- utilité du service, durée de vie des équipements, accès inclusif, retrait du service et
  effets rebond ;
- mesures reproductibles qui distinguent indicateurs de ressources, énergie et impacts
  environnementaux modélisés.

Le catalogue oriente aussi les recommandations pour les déploiements serverless et edge,
les services mobiles et hors ligne, l'IoT et l'embarqué, les systèmes distribués, les bases
NoSQL et plateformes de données, ainsi que les langages et frameworks suivants : Java,
Kotlin, Scala, Rust, C, C++, C#, Swift, Go, Python, JavaScript, TypeScript, PHP, Ruby, Julia,
Nim, Zig, Shell, SQL, PL/SQL, HTML, CSS, React, Vue, Angular, Svelte, Preact, Astro et Solid.
La détection d'une technologie resserre l'analyse ; elle ne rend pas chaque règle applicable
à chaque fichier.

## Comment les règles NR sont appliquées

Green Codex ne qualifie aucun langage, framework, fournisseur cloud ou base de données de
« vert » par nature. Les pratiques de l'Institut du Numérique Responsable (NR) portent sur
la façon dont une technologie est conçue, configurée et exploitée : d'abord une
fonctionnalité utile, puis moins de travail CPU et mémoire, moins de requêtes et d'octets,
un stockage borné, l'accessibilité, la sécurité et un cycle de vie documenté.

Quand le skill est utilisé, Codex suit cette démarche :

1. **Délimiter le périmètre.** Il identifie l'étape du cycle de vie, l'impact pour les
   utilisateurs, les flux de données, la charge et les technologies à partir des fichiers
   source, des manifestes, des fichiers de verrouillage et de la configuration d'exécution.
2. **Sélectionner les règles.** Il applique les règles universelles et chaque famille
   pertinente de [`green-codex/references/rules.md`](green-codex/references/rules.md) :
   `CODE-*`, `API-*`, `WEB-*`, `DB-*`, `INFRA-*`, `OPS-*`, `NET-*`, `HW-*`, `AI-*`,
   `SERVICE-*`, `MEASURE-*`, les règles `ARCH-*` applicables et les règles `LANG-*`
   correspondantes. Un projet React reçoit donc `LANG-JS-*` et `LANG-REACT-*` ; SQL et PL/SQL
   reçoivent chacun leur jeu de règles.
3. **Passer de la recommandation à l'action.** Pour chaque règle applicable, il propose un
   changement concret ou confirme que l'implémentation actuelle convient. Exemples : borner
   la pagination, retirer les colonnes renvoyées inutilement, éviter les requêtes N+1,
   lire les gros fichiers en flux, limiter les nouvelles tentatives, charger les médias à la
   demande ou fixer une durée de conservation des données.
4. **Exiger des preuves.** Chaque règle applicable évaluée reçoit le statut `PASS`, `FAIL`
   ou `REVIEW_REQUIRED`. Le constat indique le fichier et la ligne (ou la preuve côté
   service), l'impact environnemental ou pour les utilisateurs, la sévérité, le niveau de
   confiance et une méthode de vérification : test, benchmark, plan de requête, profil
   d'allocation, trace réseau ou estimation SCI.
5. **Préserver des compromis responsables.** Aucune optimisation ne doit affaiblir la
   sécurité, l'exactitude, l'accessibilité, la résilience, la vie privée ou les besoins des
   utilisateurs. Un changement de langage, une migration cloud ou un modèle plus petit n'est
   recommandé que si le bénéfice est démontré sur la charge réelle.

Un changement ciblé reçoit des vérifications ciblées ; un audit complet documente aussi sa
couverture et ses exclusions. Les identifiants de règles du projet ne sont pas des numéros
de critères officiels. Certaines correspondances avec le RGESN sont consignées, avec leur
édition, dans la référence des critères ; elles n'établissent pas une conformité formelle.

## Usage responsable de Codex

### Charte IA responsable

Commencez les évaluations courantes d'un service par [le guide des 3U](green-codex/references/three-u.md) :
**utile** (comparer les résultats utiles et l'effort de correction avec le processus
actuel), **utilisé** (observer l'usage réel quand le besoin se présente) et **utilisable**
(observer la réalisation autonome de la tâche, y compris avec une interaction accessible).
Quelques tâches comparables, un relevé d'usage volontaire et des parcours observés
suffisent pour démarrer. Convenez des critères pour le service ; il n'existe ni objectif
d'adoption universel ni score combiné. Sans preuve d'usage, l'adoption réelle reste
`REVIEW_REQUIRED`.

La charte complète sert de référence pour les questions qui la concernent ou pour un audit
explicite. Ce n'est pas une liste à dérouler pour chaque tâche d'IA.

Pour les travaux d'IA, Green Codex applique aussi la charte IA responsable de l'INR et
d'ISIT au moyen d'[une référence dédiée](green-codex/references/responsible-ai-charter.md).
Elle répartit les seize engagements de la charte selon quatre axes : humain, inclusion et
éthique, confiance, responsabilité environnementale. Dix règles `AI-CHARTER-*` traitent les
trois premiers axes ; les règles existantes sur l'IA et la mesure couvrent la frugalité et
le cycle de vie.

L'application courante reste proportionnée à la tâche : vérifier les droits d'accès aux
données et aux outils d'un agent IA, l'indication des sources d'un chatbot, le contrôle
humain des décisions à risque, ou la participation et la formation du personnel lors d'un
déploiement en entreprise. Un utilitaire sans IA ne déclenche pas d'audit
organisationnel. Utilisez `$green-codex` avec une demande bornée, par exemple :
« Examine cet agent de support IA au regard de la charte IA responsable ; identifie les
engagements concernés, les preuves manquantes et les tests, sans rien modifier. »

Certains comportements du produit se testent automatiquement : isolation entre clients,
contournement d'une validation, échecs de recherche documentaire et budgets de ressources.
Les parcours d'accessibilité demandent aussi des vérifications manuelles ; les engagements
de participation, de formation et d'achat exigent des preuves humaines. Les constats
utilisent `PASS`, `FAIL` ou `REVIEW_REQUIRED` pour le périmètre évalué. Des tests réussis ne
certifient jamais une organisation ni la conformité au règlement européen sur l'IA. Le
[catalogue d'évaluation](evals/README.md) contient sept scénarios sur la charte, dont un
contrôle qui vérifie qu'une petite tâche sans rapport ne devient pas un audit de la charte.

### Pratiques d'usage de Codex

Quand la tâche concerne Codex lui-même, le skill applique les 15 pratiques rédigées par le
projet dans [`green-codex/references/usage-practices.md`](green-codex/references/usage-practices.md).
Elles couvrent le contexte initial utile, les forks et les limites de tâche, la compaction
volontaire, la carte du code tenue à jour, les consignes complètes, la délégation bornée,
les instructions durables du projet, la vérification proportionnée, le choix du modèle et
du niveau de raisonnement, le travail en parallèle justifié et les exécutions non
interactives minimales. Ces pratiques sont des recommandations éditoriales adaptées à
Codex ; elles ne sont pas attribuées à une personne.

## Charte NR et guides complémentaires

Choisissez ces références selon la tâche évaluée ; elles ne forment pas une liste à
dérouler en entier :

- [Charte NR](green-codex/references/nr-charter.md) : cinq axes traduits en attentes concrètes
  pour les langages de programmation et les tâches en langage naturel.
- [BP-AIR](green-codex/references/air-practices.md) : décisions d'architecture adaptées de
  18 fiches sources.
- [Maturité des parties prenantes](green-codex/references/stakeholder-maturity.md) : demandes
  de preuves fondées sur 48 questions sources, sans reproduire la méthode de notation
  officielle.
- [RIA31](green-codex/references/ria31.md) : adaptations des 41 questions observées sur le site
  source ; la référence explique l'écart avec l'ancien document à 31 questions. RIA31 est
  distinct du règlement européen sur l'IA.

Une vérification applicable sans preuve reste `REVIEW_REQUIRED`. Des documents générés ne
peuvent établir ni les décisions humaines ni l'adoption réelle par une organisation. Pour
une simple demande de texte, un bilan NR court et factuel suffit ; ni scanner ni
enregistrement JSON n'est requis.

## Mesure et preuves

Pour une comparaison ou une affirmation environnementale, suivez le protocole
[`measurement.md`](green-codex/references/measurement.md). Il définit la tâche utile et
l'unité fonctionnelle, la référence équivalente, le périmètre de mesure, les conditions de
charge, l'incertitude et les compromis sur le cycle de vie. Les indicateurs de ressources,
le nombre de tokens, la latence et le coût ne mesurent pas directement le carbone. Quand la
méthode SCI s'applique, le rapport consigne les composantes opérationnelles et intrinsèques,
les facteurs, l'allocation, la période et l'incertitude ; une preuve manquante reste
`REVIEW_REQUIRED`.

Exemple de constat (le format reste en anglais) :

```text
FAIL DB-EFF-001 at src/repository/users.sql:14
SELECT * transfers unused columns for every request.
Action: select the named fields required by the endpoint.
Verification: query test plus an EXPLAIN plan and response-size comparison.
```

Un gain d'énergie ou de carbone annoncé n'est jamais une promesse universelle. Une mesure
indique sa charge, sa référence, son environnement, sa méthode, sa durée et son
incertitude. Quand une CI hébergée ne fournit pas de données énergétiques fiables, le skill
indique `REVIEW_REQUIRED` au lieu d'inventer un résultat.

## Installation

Pour une première installation sur macOS ou Linux, avec Git et Codex déjà installés,
clonez ce dépôt et ouvrez son dossier racine :

```bash
git clone https://github.com/Institut-du-Numerique-Responsable/green-codex.git
cd green-codex
```

Copiez le dossier `green-codex` dans votre dossier personnel de skills. Si la destination
existe déjà, examinez et sauvegardez vos modifications locales avant de la mettre à jour ;
n'exécutez pas la copie de première installation sur une installation existante.

```bash
mkdir -p ~/.agents/skills
cp -R green-codex ~/.agents/skills/green-codex
```

Vérifiez la copie avec `ls ~/.agents/skills/green-codex/SKILL.md`. Dans Codex CLI ou
l'extension IDE, appelez `$green-codex` dans votre demande. Si le skill n'apparaît pas,
redémarrez Codex. Selon la [documentation officielle](https://learn.chatgpt.com/docs/build-skills),
Codex cherche les skills personnels dans `~/.agents/skills`.

Regardez la [démonstration d'installation de 50 secondes](https://institut-du-numerique-responsable.github.io/green-codex/#installation-video)
ou lisez sa transcription sur la même page.

## Fichiers inclus

- `green-codex/SKILL.md` : démarche et aide à la décision ;
- `green-codex/references/criteria.md` : carte compacte des critères et liste des preuves ;
- `green-codex/references/measurement.md` : protocole de comparaison, niveaux de preuve et
  limites du calcul carbone ;
- `green-codex/references/responsible-ai-charter.md` : traçabilité de la charte, actions
  courantes et preuves attendues ;
- `green-codex/references/three-u.md` : petits tests pratiques d'utilité, d'usage réel et
  d'utilisabilité ;
- `green-codex/references/rules.md` : règles complètes pour le frontend, le backend, les
  données, l'accessibilité, la qualité web, l'IA responsable, les architectures modernes,
  l'exploitation et les recommandations propres à chaque langage ou framework ;
- `green-codex/references/green-claude-mapping.md` : correspondance entre les 277 règles de
  Green Claude 1.5.0 et les identifiants Green Codex, avec le statut de chaque règle ;
- `green-codex/references/usage-practices.md` : 15 pratiques rédigées par le projet et
  adaptées à Codex, avec des sources officielles pour les mécanismes propres à Codex ;
- `green-codex/scripts/check_sobriety.py` : contrôles statiques prudents de quelques
  anti-patterns détectés avec une forte confiance ;
- `green-codex/scripts/nr_hook.py` : contrôle natif optionnel du bilan ; à installer avec
  `scripts/install_nr_hook.py` depuis le dossier du skill installé, puis à approuver dans
  `/hooks` de Codex ;
- `green-codex/scripts/nr_summary.py` : valide les enregistrements de tâche et produit le
  bilan NR de fin de tâche ;
- `green-codex/references/closing-summary.md` : format d'enregistrement, commande et limites
  d'intégration ;
- `green-codex/references/sources.md` : inventaire des sources et lacunes de provenance ;
- `green-codex/references/reuse-rights.md` : conditions d'attribution et de réutilisation ;
- `green-codex/scripts/run_evals.py` : contrôles de format et revues sémantiques liées par
  empreinte, séparés ;
- `evals/cases.json` : scénarios d'évaluation réalistes du comportement ;
- `evals/README.md` : procédure pour évaluer des réponses Codex enregistrées ;
- `green-codex/agents/openai.yaml` : métadonnées d'interface pour la découverte du skill.

Lancez le test de fumée du paquet et le validateur de skills Codex avant de publier une
modification :

```bash
python3 green-codex/scripts/test_skill.py
python3 ~/.codex/skills/.system/skill-creator/scripts/quick_validate.py green-codex
```

### Contrôles automatiques de sobriété

Le dépôt contient un vérificateur statique, sans dépendance, pour les anti-patterns détectés
avec une forte confiance. Il signale les `SELECT *` en SQL, la lecture automatique des
médias et l'interrogation périodique non bornée en JavaScript, avec fichier et ligne. Il
reste volontairement prudent : un scan sans constat n'est pas une déclaration de
conformité, et la performance, l'énergie, l'accessibilité et l'architecture demandent
toujours des tests ou des mesures ciblés.

```bash
python3 green-codex/scripts/test_sobriety.py
python3 green-codex/scripts/check_sobriety.py --path .
python3 green-codex/scripts/check_sobriety.py --path . --format json
```

Les mêmes contrôles s'exécutent dans le workflow GitHub Actions `validate`. Un seuil propre
au projet ou une nouvelle règle ne s'ajoute qu'avec un test de non-régression et une preuve
documentée.

### Bilan NR de fin de tâche

Chaque tâche qui utilise le skill demande désormais une explication concise des actions NR
réalisées, avec les identifiants de règles, les bénéfices pour les utilisateurs, les
preuves et les vérifications restantes. Pour l'automatisation, utilisez
`green-codex/scripts/nr_summary.py` avec un enregistrement de tâche à jour et un périmètre
de scan explicite. Le script valide l'enregistrement et relance les trois contrôles
statiques ; il ne certifie pas les autres règles. Voir
[le format d'enregistrement, la commande et l'intégration du hook](green-codex/references/closing-summary.md).
Un hook natif optionnel vérifie la structure du bilan et demande au plus une correction.
Installez-le explicitement depuis le dossier persistant du skill, puis examinez et
approuvez ses deux entrées dans `/hooks` de Codex ; copier le skill ne suffit pas à
l'activer. Le guide lié décrit les limites de détection, l'installation, la vérification
et la désinstallation.

## Utilisation et contribution

Utilisez le skill pour des audits, des revues de code, des décisions d'architecture et du
développement. Les constats distinguent les preuves observées des recommandations et ne
sacrifient jamais la sécurité, l'exactitude, l'accessibilité ou la résilience à un score
environnemental.

Les issues et pull requests sont les bienvenues sur le [dépôt GitHub](https://github.com/Institut-du-Numerique-Responsable/green-codex).
Consultez [CONTRIBUTING.md](CONTRIBUTING.md), [SECURITY.md](SECURITY.md) et
[CODE_OF_CONDUCT.md](CODE_OF_CONDUCT.md) avant de contribuer (documents en anglais).

## Publication d'une version

La version est enregistrée dans `VERSION` et doit correspondre au tag de publication
(`vX.Y.Z`). Lancez les deux commandes de validation, mettez à jour `CHANGELOG.md`, puis
créez une release GitHub à partir du tag. Le workflow de CI liste les contrôles exécutés sur
chaque pull request.

## Licence

Le code et les scripts de test sont sous licence Apache-2.0. La documentation et le contenu
des règles sont disponibles sous [CC BY 4.0](https://creativecommons.org/licenses/by/4.0/),
sauf les adaptations explicitement marquées [CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/).
Voir [LICENSE](LICENSE) et [LICENSE-CC-BY-4.0](LICENSE-CC-BY-4.0).

Les références de sobriété des tokens inspirées et adaptées de Caveman sont sous licence
Apache-2.0. L'[attribution tierce](green-codex/references/third-party-attributions.md)
précise le droit d'auteur de Julius Brussee, les modifications de l'INR, l'indépendance du
projet et les limites de provenance.

## Équipe

Green Codex est maintenu par une équipe de l'Institut du Numérique Responsable (INR) :

| Nom | GitHub | Rôle |
|------|-------|------|
| Guillaume Gallon | [@gridboy](https://github.com/gridboy) | Mainteneur |
| Guillaume Bourgeois | [@bourgeoisguillaume01-glitch](https://github.com/bourgeoisguillaume01-glitch) | Mainteneur |
| Vincent Courboulay | [@vincentcourboulay](https://github.com/vincentcourboulay) | Mainteneur |

La liste complète des contributeurs se trouve dans [AUTHORS.md](AUTHORS.md).

## Autres références INR et réutilisation

Le skill contient des adaptations délimitées de la charte NR (5 axes), de BP-AIR (18 fiches),
du guide de maturité des parties prenantes (48 questions) et de RIA31 en ligne (41 questions
visibles). Chaque consigne renvoie à sa source et précise une action et une preuve. La
commande de bilan de fin de tâche accepte ces identifiants ; la couverture du scanner
statique reste inchangée. Voir l'[inventaire des sources](green-codex/references/sources.md)
et les [droits de réutilisation](green-codex/references/reuse-rights.md). Les adaptations de
BP-AIR, de la maturité et de RIA31 sont explicitement sous CC BY-SA 4.0 ; la reformulation
ne lève pas les conditions de licence de la source.

## Sources

Voir l'[inventaire complet des sources documentées et des lacunes de provenance](green-codex/references/sources.md).

- [Charte IA responsable (INR/ISIT)](https://charter.isit-europe.org/charte-ia/?lang=fr_FR)

- [RGESN](https://ecoresponsable.numerique.gouv.fr/publications/referentiel-general-ecoconception/)
- [GR491](https://gr491.isit-europe.org/)
- [Opquast](https://checklists.opquast.com/fr/qualite-numerique/)
- [RGAA](https://accessibilite.numerique.gouv.fr/)
- [Spécification SCI](https://sci.greensoftware.foundation/)
- [Référence des commandes Codex CLI](https://developers.openai.com/codex/cli/reference)
- [Recommandations Codex pour `AGENTS.md`](https://developers.openai.com/codex/guides/agents-md)
- [Recommandations OpenAI pour la rédaction des prompts](https://learn.chatgpt.com/docs/prompting)
- [Bonnes pratiques OpenAI](https://learn.chatgpt.com/guides/best-practices)
- [Recommandations OpenAI sur les modèles](https://developers.openai.com/api/docs/guides/latest-model?model=gpt-5.5)

Green Codex est un guide d'ingénierie réutilisable. Il ne remplace ni les référentiels
officiels ni un audit de conformité formel. Le projet consigne les éditions vérifiées quand
c'est utile, mais chaque équipe doit vérifier les versions en vigueur et documenter ses
propres preuves avant toute déclaration formelle.

## Site web et référencement

Le site du projet est publié depuis [`docs/`](docs/). Il comprend une page d'accueil légère
et accessible, des métadonnées structurées, un sitemap, `robots.txt` et un résumé `llms.txt`
pour les moteurs de recherche et les assistants IA. Il existe en français et en anglais :

- français : <https://institut-du-numerique-responsable.github.io/green-codex/>
- anglais : <https://institut-du-numerique-responsable.github.io/green-codex/en/>

## Limites de vérification et périmètre pratique

Les 3U partent d'un besoin confirmé. Les travaux techniques d'IA appliquent les règles
d'efficacité ; les sections de la charte sont lues pour une évaluation explicite ou un
risque identifié. Une inspection peut suffire pour un changement simple ; un benchmark lève
une incertitude importante. Les alias de règles conservent les identifiants existants sans
imposer de constats en double.

Le scanner exclut des constats de projection excessive les tests d'existence SQL directs.
Les commentaires et exemples de chaînes JSX/TSX sont masqués ; les médias dans les templates
demandent une revue, car ce scanner n'est pas un compilateur JavaScript ou Vue. Un scan sans
constat ne prouve pas tout le comportement à l'exécution.

La sortie des évaluations sépare `FORMAT` et `SEMANTIC`. Une correspondance de mots-clés ne
valide jamais un raisonnement ; `--strict-format` exige aussi les identifiants et termes
littéraux. Voir les [instructions d'évaluation](evals/README.md) et le
[relevé d'audit et de corrections](docs/audit-skill-2026-09-14.md).
