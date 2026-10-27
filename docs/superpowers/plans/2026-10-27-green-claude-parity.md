# Mise à niveau de Green Codex sur Green Claude : plan d'implémentation

> **Pour les agents :** sous-skill requis : superpowers:subagent-driven-development (recommandé) ou superpowers:executing-plans pour exécuter ce plan tâche par tâche. Les étapes utilisent des cases à cocher (`- [ ]`).

**Objectif :** couvrir dans Green Codex toutes les règles et tout le périmètre de Green Claude v1.5.0, sauf les règles qui dépendent d'un mécanisme propre à Claude Code sans équivalent dans Codex.

**Architecture :** Green Codex garde son propre système d'identifiants (`SERVICE-EFF-*`, `CODE-EFF-*`, `LANG-*`, etc.). Une table de correspondance indique, pour chacune des 277 règles de Green Claude, si elle est déjà couverte, si elle devient une nouvelle règle Green Codex ou si elle est exclue, avec la raison. Les nouvelles règles s'ajoutent aux fichiers de référence existants. Des tests vérifient que la table est complète et que chaque identifiant cible existe.

**Technologies :** Markdown (références du skill), Python 3 sans dépendance (`unittest`, scripts existants).

**Spec :** pas de document de conception. La source est la demande du 2026-10-27 : « mettre à niveau green codex avec les règles et le périmètre de green claude, exclus toutefois les règles qui ne peuvent pas s'appliquer à Codex ». Les décisions marquées « décision du plan » ci-dessous n'ont pas été validées par l'utilisateur.

## Source de référence

- Dépôt : `/Volumes/Ugreen/projects/inr/green-claude`, commit `1a3d260` (version 1.5.0).
- Règles : `skills/green-claude/rules/`.
  - `ecoconception.json` : 107 règles `ECO-*` réparties en 9 familles RGESN.
  - `usage.json` : 13 règles `USAGE-*`.
  - `tokens.json` : 30 règles `NR-TOK-*`.
  - `langages/*.json` : 24 fichiers et 127 règles.
  - Total : 277.
- Périmètre : `skills/green-claude/SKILL.md` (description, « Proactive mode », « Language-specific rules », « Recording a decision », « Writing your replies »).
- Notez le commit source dans la table de correspondance. Ne lisez pas la copie du plugin `~/.claude/plugins/cache/green-claude/.../1.4.0` : elle est plus ancienne.

## Contraintes globales

- Python sans dépendance externe, comme `scripts/check_sobriety.py` et `scripts/nr_summary.py`.
- Une règle se définit sous la forme `- **ID — Titre :** texte`, où `ID` correspond à `[A-Z][A-Z0-9-]+-\d{3}`. Les fonctions `known_rules()` et `test_definitions_unique_and_registered` ne reconnaissent que ce format (`**ID` ou `### ID`).
- La table de correspondance ne doit jamais écrire un identifiant après `**` ni après `### `. Sinon `known_rules()` le compterait comme une définition.
- Les nouvelles règles de `rules.md` sont rédigées en anglais, comme le reste du fichier. La table de correspondance et les notes de provenance sont rédigées en français, comme `reuse-rights.md` et `sources.md`.
- Toute règle importée (`nouvelle` ou `adaptée`) est réécrite dans le style de `rules.md` : une phrase d'action, une phrase de vérification. Ne copiez jamais le texte source ; les champs `title` et `recommendation` servent seulement à comprendre la substance.
- Langages manquants à ajouter : C# (`LANG-CSHARP-*`) et Swift (`LANG-SWIFT-*`). Les 22 autres langages de Green Claude ont déjà une famille Green Codex.
- Numérotation : continuez après le plus grand numéro existant de la famille. Ne réutilisez jamais un numéro.
- Chaque règle indique comment la vérifier (test, commande, mesure ou inspection), comme les règles `CODE-EFF-*` existantes.
- Les noms « Claude », `CLAUDE.md`, « Haiku », « Sonnet », « Opus » et « Anthropic » ne doivent pas apparaître dans les fichiers de `RULE_FILES`, sauf dans une phrase de provenance.
- Avant d'écrire une commande ou un comportement Codex (par exemple `/compact`, `/new`, `AGENTS.md`, les hooks, `/model`), vérifiez-le dans la documentation officielle actuelle de Codex : https://developers.openai.com/codex. Citez la page consultée dans le message de commit.
- Appliquez `green-codex/references/expression.md` à tout texte rédigé, y compris les commits et la PR.
- Le contenu de Green Claude est sous CC BY 4.0 (INR) et ses scripts sous Apache-2.0. N'importez aucun script.

## Critères d'exclusion (décision du plan)

Une règle Green Claude est exclue seulement si l'une de ces conditions est vraie et qu'aucun équivalent n'existe dans la documentation Codex actuelle :

- **X-HOOK** : la règle exige un événement de Claude Code (`PostToolUse`, `UserPromptSubmit` ou `Stop` pour le cache de réponses).
- **X-CMD** : la règle repose sur une commande ou une interface propre à Claude (mode `/green-claude`, choix Haiku/Sonnet/Opus).
- **X-PRODUCT** : la règle repose sur une donnée propre au produit Claude (tarif ou comportement du cache de prompt Anthropic).

Une règle qui cite un nom Claude mais garde un sens pour Codex est **adaptée**, pas exclue. Par exemple : `CLAUDE.md` devient `AGENTS.md`, `/clear` devient la commande Codex équivalente une fois vérifiée, et « Haiku » devient « un modèle plus léger disponible dans l'hôte ».

## Hors périmètre (décision du plan)

- Portage des détecteurs `eco-audit.sh` et `*.awk` dans `check_sobriety.py`. À traiter dans un plan séparé.
- Fichier de décisions `.green-claude/decisions.md`. Ce mécanisme n'est pas une règle ; il est à proposer séparément sous la forme `.green-codex/decisions.md`.
- Cache de réponses « zéro token » par hooks.
- Modifications du site `docs/`, sauf un compteur de règles devenu faux.

## Points d'attention pour la revue

1. **Doublon sémantique** : une nouvelle règle reformule une règle Green Codex existante sous un autre identifiant. Comportement attendu : la ligne de la table est `couverte`, sans nouvelle règle. Le relecteur vérifie chaque `nouvelle` contre la section cible de `rules.md`.
2. **Formulation Claude restée en place** : un nom de produit Claude, ou une commande non vérifiée pour Codex, se retrouve dans un fichier de règles. Couvert par `test_no_claude_specific_wording` (Tâche 1).
3. **Identifiant cible inexistant ou mal saisi dans la table**. Couvert par `test_mapping_targets_exist` (Tâche 1).
4. **Compteurs devenus faux** : README, `SKILL.md`, `sources.md` ou le site annoncent un ancien nombre de règles. Couvert par l'étape de recherche de la Tâche 4.
5. **Règle d'une famille de langage nouvelle sans routage** : C# ou Swift sont définis mais `SKILL.md` et la matrice de `nr-charter.md` ne les routent pas. La ligne C# actuelle de `nr-charter.md` interdit même d'inventer `LANG-CSHARP-*`. Couvert par `test_language_families_routed` (Tâche 2).

---

### Tâche 1 : table de correspondance et règles transverses (`ECO-*`)

**Fichiers :**
- Créer : `green-codex/references/green-claude-mapping.md`
- Modifier : `green-codex/references/rules.md` (sections « Enforceable sobriety rules » et « Modern architecture guidance »)
- Créer : `green-codex/scripts/test_green_claude_mapping.py`
- Modifier : `.github/workflows/validate.yml` (ajouter le nouveau test après `test_reference_catalog.py`)

**Interfaces :**
- Produit : le format de la table, que les Tâches 2 à 4 reprennent sans le changer.
  ```
  | ID Green Claude | Statut | ID Green Codex | Raison |
  ```
  `Statut` vaut `couverte`, `nouvelle`, `adaptée` ou `exclue`.
  `ID Green Codex` contient un ou plusieurs identifiants séparés par `, `, ou `—` si la règle est exclue.
  `Raison` est obligatoire pour `exclue` (code `X-HOOK`, `X-CMD` ou `X-PRODUCT`, puis une phrase) et pour `adaptée` (ce qui a changé).
- Produit : `parse_mapping(path: Path) -> list[dict[str, str]]` dans `test_green_claude_mapping.py`, avec les clés `source`, `status`, `targets`, `reason`.
- Consomme : `known_rules()` depuis `nr_summary.py`.

- [ ] **Étape 1 : écrire les tests qui doivent échouer**

  ```python
  def test_mapping_rows_valid(self):
      rows = parse_mapping(MAPPING)
      self.assertTrue(rows)
      self.assertEqual(len({r["source"] for r in rows}), len(rows))
      for r in rows:
          self.assertIn(r["status"], {"couverte", "nouvelle", "adaptée", "exclue"}, r)
          if r["status"] in {"exclue", "adaptée"}:
              self.assertTrue(r["reason"].strip(), r)
          if r["status"] == "exclue":
              self.assertRegex(r["reason"], r"^X-(HOOK|CMD|PRODUCT)\b", r)

  def test_mapping_targets_exist(self):
      known = known_rules()
      for r in parse_mapping(MAPPING):
          if r["status"] != "exclue":
              targets = set(r["targets"].split(", "))
              self.assertFalse(targets - known, r)

  def test_mapping_not_registered_as_definitions(self):
      text = MAPPING.read_text(encoding="utf-8")
      self.assertNotRegex(text, r"(?:\*\*|### )[A-Z][A-Z0-9-]+-\d{2,3}")

  def test_no_claude_specific_wording(self):
      pattern = re.compile(r"\b(CLAUDE\.md|Haiku|Sonnet|Opus|Anthropic)\b")
      for name in RULE_FILES:
          text = (REFS / name).read_text(encoding="utf-8")
          self.assertIsNone(pattern.search(text), name)
  ```

- [ ] **Étape 2 : lancer les tests et vérifier qu'ils échouent**

  Commande : `python green-codex/scripts/test_green_claude_mapping.py`
  Résultat attendu : `FileNotFoundError` sur `green-claude-mapping.md` pour les trois premiers tests. `test_no_claude_specific_wording` peut déjà passer ; s'il échoue, adaptez la formulation trouvée.

- [ ] **Étape 3 : classer les 107 règles `ECO-*`**

  Pour chaque règle de `ecoconception.json`, lisez `title`, `description` et `recommendation`. Comparez-la à la section correspondante de `rules.md`, en vous aidant de `rgesn_ref` et de `gr491_famille`. Correspondance des familles RGESN vers Green Codex : stratégie et spécifications → `SERVICE-EFF`/`MEASURE-EFF` ; architecture → `ARCH-*`/`CODE-EFF` ; UX et contenus → `WEB-EFF`/`SERVICE-EFF` ; frontend → `WEB-EFF`/`LANG-HTML`/`LANG-CSS` ; backend → `API-EFF`/`DB-EFF`/`CODE-EFF` ; hébergement → `INFRA-EFF`/`OPS-EFF`/`HW-EFF` ; algorithmes et IA → `CODE-EFF`/`AI-EFF`. Choisissez la famille la plus précise.

  - Même substance déjà présente : `couverte`.
  - Substance absente : ajoutez une règle dans la famille choisie, puis marquez `nouvelle`.
  - Règles `ECO-ALGO-09` à `27` et `ECO-HOST-07` à `10` (eau, électricité, CPU, GPU) : elles sont originales à Green Claude. Ajoutez la mention de provenance demandée par `attribution_note` dans `sources.md` (Tâche 4).

  En tête de la table, écrivez le commit source `1a3d260` et les critères d'exclusion.

- [ ] **Étape 4 : lancer les tests et vérifier qu'ils passent**

  Commandes : `python green-codex/scripts/test_green_claude_mapping.py && python green-codex/scripts/test_reference_catalog.py`
  Résultat attendu : `OK` pour les deux.

- [ ] **Étape 5 : commit**

  ```bash
  git add green-codex/references/green-claude-mapping.md green-codex/references/rules.md green-codex/scripts/test_green_claude_mapping.py .github/workflows/validate.yml
  git commit
  ```
  Le message suit `expression.md` et donne les nombres de règles couvertes, nouvelles et exclues.

### Tâche 2 : règles par langage, C# et Swift

**Fichiers :**
- Modifier : `green-codex/references/rules.md` (section « Language-specific sobriety guidance » et sous-sections `LANG-*`)
- Modifier : `green-codex/references/nr-charter.md:109` (ligne C#) et la matrice des langages (ajouter Swift)
- Modifier : `green-codex/SKILL.md` (section « Language rule routing »)
- Modifier : `green-codex/references/green-claude-mapping.md`
- Modifier : `green-codex/scripts/test_green_claude_mapping.py`

**Interfaces :**
- Consomme : le format de table et `parse_mapping` de la Tâche 1.
- Produit : les familles `LANG-CSHARP-*` (sous-section `### C# and .NET (\`LANG-CSHARP-*\`)`) et `LANG-SWIFT-*` (sous-section `### Swift (\`LANG-SWIFT-*\`)`), numérotées à partir de `001`.

- [ ] **Étape 1 : écrire le test qui doit échouer**

  ```python
  def test_language_families_routed(self):
      rules = (REFS / "rules.md").read_text(encoding="utf-8")
      charter = (REFS / "nr-charter.md").read_text(encoding="utf-8")
      for family in ("LANG-CSHARP", "LANG-SWIFT"):
          self.assertIn(f"`{family}-*`", rules)
          self.assertRegex(charter, rf"{family}-\d{{3}}")
      self.assertNotIn("inventer une famille `LANG-CSHARP-*`", charter)
  ```

- [ ] **Étape 2 : lancer le test et vérifier qu'il échoue**

  Commande : `python green-codex/scripts/test_green_claude_mapping.py`
  Résultat attendu : FAIL sur `test_language_families_routed`.

- [ ] **Étape 3 : classer les 127 règles des 24 fichiers `langages/*.json`**

  Utilisez la même méthode qu'à la Tâche 1. Correspondance des préfixes :
  `ECO-JS` → `LANG-JS` ; `ECO-PY` → `LANG-PYTHON` ; `ECO-KT` → `LANG-KOTLIN` ; `ECO-RS` → `LANG-RUST` ; `ECO-RB` → `LANG-RUBY` ; `ECO-SH` → `LANG-SHELL` ; `ECO-NG` → `LANG-ANGULAR` ; `ECO-CS` → `LANG-CSHARP` ; `ECO-SW` → `LANG-SWIFT`. Pour les autres préfixes, retirez `ECO-` et ajoutez `LANG-`.

  Créez les sous-sections C# (8 règles source) et Swift (5 règles source). Remplacez la ligne C# de `nr-charter.md` par une ligne qui cite les identifiants `LANG-CSHARP-*`, et ajoutez une ligne Swift. Dans `SKILL.md`, gardez la règle « never invent a `LANG-*` identifier ».

- [ ] **Étape 4 : lancer les tests et vérifier qu'ils passent**

  Commandes : `python green-codex/scripts/test_green_claude_mapping.py && python green-codex/scripts/test_reference_catalog.py`
  Résultat attendu : `OK`. `test_new_rule_cross_references_exist` vérifie aussi que les identifiants cités dans `nr-charter.md` existent.

- [ ] **Étape 5 : commit**

### Tâche 3 : pratiques d'usage et sobriété des tokens

**Fichiers :**
- Modifier : `green-codex/references/usage-practices.md`
- Modifier : `green-codex/references/token-sobriety.md` et, si une commande Codex change, `green-codex/references/codex-token-sobriety.md`
- Modifier : `green-codex/references/green-claude-mapping.md`

**Interfaces :**
- Consomme : le format de table de la Tâche 1.
- Conserve : les identifiants `NR-TOK-001` à `030`, ni plus ni moins (`test_token_rules_complete_and_registered`). Pour les pratiques d'usage, conservez les identifiants existants de `usage-practices.md`.

- [ ] **Étape 1 : comparer `usage.json` (13 règles) à `usage-practices.md` (14 pratiques)**

  Classez chaque `USAGE-*`. Les règles qui citent Claude (`USAGE-CTX-03`, `USAGE-CTX-05`, `USAGE-BRIEF-01` à `03`, `USAGE-MEM-01`, `USAGE-MEM-03`, `USAGE-VERIF-01`, `USAGE-CPU-03`) sont `adaptée` si Codex a un équivalent documenté, sinon `exclue` avec un code `X-*`.

- [ ] **Étape 2 : comparer `tokens.json` à `token-sobriety.md`, règle par règle**

  Mettez à jour la substance changée dans Green Claude 1.5.0 sans renuméroter. `NR-TOK-012` et `NR-TOK-024` citent Claude dans la source : vérifiez que la version Green Codex reste formulée pour Codex. Marquez `couverte` ou `adaptée`.

- [ ] **Étape 3 : lancer les tests**

  Commandes : `python green-codex/scripts/test_green_claude_mapping.py && python green-codex/scripts/test_reference_catalog.py && python green-codex/scripts/test_skill.py`
  Résultat attendu : `OK`.

- [ ] **Étape 4 : commit**

### Tâche 4 : périmètre du skill, complétude et documentation

**Fichiers :**
- Modifier : `green-codex/SKILL.md` (champ `description` ; ajouter les réflexes du « Proactive mode » à « Working method »)
- Modifier : `green-codex/agents/openai.yaml` si son texte de déclenchement reprend la description
- Modifier : `green-codex/references/sources.md`, `green-codex/references/reuse-rights.md`
- Modifier : `README.md`, `CHANGELOG.md`, `VERSION`
- Modifier : `green-codex/scripts/test_green_claude_mapping.py`

**Interfaces :**
- Consomme : la table complète des Tâches 1 à 3.

- [ ] **Étape 1 : écrire le test de complétude qui doit échouer s'il manque une ligne**

  ```python
  def test_mapping_complete(self):
      rows = parse_mapping(MAPPING)
      self.assertEqual(len(rows), 277)
      prefixes = {r["source"].rsplit("-", 1)[0] for r in rows}
      self.assertTrue({"ECO-STRAT", "USAGE-CTX", "NR-TOK", "ECO-CS", "ECO-SW"} <= prefixes)
  ```

- [ ] **Étape 2 : lancer le test**

  Commande : `python green-codex/scripts/test_green_claude_mapping.py`
  Résultat attendu : `OK` si les Tâches 1 à 3 sont complètes. Sinon, complétez la table avant de continuer.

- [ ] **Étape 3 : élargir le périmètre de `SKILL.md`**

  - Description : ajoutez les déclencheurs de Green Claude qui manquent : choix de format de fichier, requêtes réseau, images et assets, boucles, cache, pagination, dépendances, choix de framework ou de modèle d'IA, ainsi que les mots-clés « eco-design audit », `--eco-check`, « RGESN », « GR491 », « audit éco-conception », « écoconception ». Gardez une seule phrase.
  - « Working method » : ajoutez en quelques lignes les réflexes appliqués sans demande. Formats ouverts et légers, peu de requêtes et de petites réponses, pas de boucle ou de traitement redondant, imports limités à ce qui sert, images compressées et bien dimensionnées. Ajoutez aussi la règle de conflit : signaler le compromis en une phrase, proposer l'option plus légère, livrer ce qui est demandé.
  - Ne copiez pas les sections X-HOOK ou X-CMD : « Guaranteed application », « Browse mode » et « What this skill does NOT do ».

- [ ] **Étape 4 : documentation et compteurs**

  - `sources.md` : provenance de Green Claude (dépôt, commit `1a3d260`, licence CC BY 4.0), mention d'originalité des règles `ECO-ALGO-09` à `27` et `ECO-HOST-07` à `10`, et lien vers `green-claude-mapping.md`.
  - `reuse-rights.md` : courte section « Green Claude » qui indique la même organisation, la même licence de contenu et qu'aucun script Apache-2.0 n'a été importé.
  - Lancez `grep -rnE "\b(183|295|277)\b|[0-9]+ (rules|règles|IDs|identifiants)" README.md green-codex docs/*.md docs/index.html`. Corrigez chaque compteur faux à partir de `len(known_rules())`.
  - `CHANGELOG.md` : entrée 1.1.0. `VERSION` : `1.1.0`.

- [ ] **Étape 5 : lancer la suite complète, comme la CI**

  ```bash
  for t in test_skill test_sobriety test_nr_summary test_nr_hook test_reference_catalog test_green_claude_mapping test_evals test_eval_review; do python green-codex/scripts/$t.py || break; done
  python green-codex/scripts/check_sobriety.py --path .
  ```
  Résultat attendu : tous les tests `OK`, et `check_sobriety.py` ne signale aucun `FAIL` nouveau par rapport à `main`.

- [ ] **Étape 6 : commit, puis revue de toute la branche**

  Relisez la PR et le message de squash selon `expression.md`. Décrivez dans la PR les nombres `couverte`/`nouvelle`/`adaptée`/`exclue` et la liste des exclusions avec leur code.
