# Correspondance avec Green Claude

Cette table relie chaque règle de Green Claude à Green Codex. Elle documente la provenance
des règles importées ; elle ne crée aucune règle. Ne la chargez que pour une question de
provenance ou de couverture.

Source : dépôt Green Claude de l'INR, version 1.5.0, commit `1a3d260`, dossier
`skills/green-claude/rules/`. Contenu sous CC BY 4.0. Aucun script n'a été importé.

Statuts :

- `couverte` : une règle Green Codex existante porte déjà la même substance.
- `nouvelle` : la règle a été réécrite dans Green Codex sous l'identifiant indiqué.
- `adaptée` : la règle citait un mécanisme propre à Claude ; elle a été reformulée pour Codex.
- `exclue` : la règle ne peut pas s'appliquer à Codex. La raison commence par un code :
  - `X-HOOK` : elle exige un événement de Claude Code sans équivalent Codex documenté ;
  - `X-CMD` : elle repose sur une commande ou une interface propre à Claude ;
  - `X-PRODUCT` : elle repose sur une donnée propre au produit Claude.

Les seuils chiffrés de la source (taille de police, température, taux de swap, taille de lot)
n'ont pas été repris lorsqu'ils n'étaient pas sourcés : les règles Green Codex demandent de
mesurer et de fixer le seuil dans le projet.

## Écoconception (`ecoconception.json`)

| ID Green Claude | Statut | ID Green Codex | Raison |
| --- | --- | --- | --- |
| `ECO-STRAT-01` | couverte | `MEASURE-EFF-001` | |
| `ECO-STRAT-02` | couverte | `DB-EFF-005` | |
| `ECO-STRAT-03` | nouvelle | `SERVICE-EFF-007` | |
| `ECO-STRAT-04` | couverte | `SERVICE-EFF-004`, `NR-CHARTER-004` | |
| `ECO-STRAT-05` | couverte | `NR-CHARTER-005` | |
| `ECO-STRAT-06` | nouvelle | `SERVICE-EFF-008` | |
| `ECO-STRAT-07` | couverte | `SERVICE-EFF-005` | |
| `ECO-STRAT-08` | couverte | `MEASURE-EFF-003` | |
| `ECO-STRAT-09` | couverte | `MEASURE-EFF-004` | |
| `ECO-SPEC-01` | nouvelle | `SERVICE-EFF-009` | |
| `ECO-SPEC-02` | couverte | `SERVICE-EFF-002` | |
| `ECO-SPEC-03` | couverte | `SERVICE-EFF-002`, `SERVICE-EFF-006` | |
| `ECO-SPEC-04` | nouvelle | `WEB-EFF-005` | |
| `ECO-SPEC-05` | couverte | `SERVICE-EFF-001`, `SERVICE-EFF-005` | |
| `ECO-ARCH-01` | nouvelle | `CODE-EFF-014` | |
| `ECO-ARCH-02` | couverte | `INFRA-EFF-003` | |
| `ECO-ARCH-03` | nouvelle | `SERVICE-EFF-010` | |
| `ECO-ARCH-04` | couverte | `INFRA-EFF-003`, `OPS-EFF-004` | |
| `ECO-ARCH-05` | nouvelle | `CODE-EFF-015` | |
| `ECO-ARCH-06` | nouvelle | `OPS-EFF-004` | |
| `ECO-ARCH-07` | nouvelle | `CODE-EFF-014` | |
| `ECO-ARCH-08` | couverte | `ARCH-SERVERLESS-001` | |
| `ECO-ARCH-09` | couverte | `ARCH-SERVERLESS-002` | |
| `ECO-ARCH-10` | couverte | `ARCH-EDGE-002` | |
| `ECO-ARCH-11` | couverte | `ARCH-DIST-002`, `ARCH-DIST-003` | |
| `ECO-ARCH-12` | nouvelle | `CODE-EFF-016` | |
| `ECO-UX-01` | couverte | `WEB-EFF-004` | |
| `ECO-UX-02` | couverte | `SERVICE-EFF-003` | |
| `ECO-UX-03` | couverte | `LANG-HTML-001` | |
| `ECO-UX-04` | nouvelle | `WEB-EFF-005` | |
| `ECO-UX-05` | couverte | `LANG-CSS-001` | |
| `ECO-UX-06` | nouvelle | `WEB-EFF-006` | |
| `ECO-UX-07` | couverte | `WEB-EFF-004`, `LANG-CSS-002` | |
| `ECO-UX-08` | nouvelle | `WEB-EFF-007` | |
| `ECO-CONT-01` | couverte | `WEB-EFF-002` | |
| `ECO-CONT-02` | couverte | `WEB-EFF-002`, `WEB-EFF-004` | |
| `ECO-CONT-03` | nouvelle | `WEB-EFF-006` | |
| `ECO-FRONT-01` | couverte | `CODE-EFF-007` | |
| `ECO-FRONT-02` | couverte | `WEB-EFF-001`, `LANG-JS-002` | |
| `ECO-FRONT-03` | nouvelle | `WEB-EFF-008` | |
| `ECO-FRONT-04` | couverte | `CODE-EFF-007` | |
| `ECO-FRONT-05` | nouvelle | `CODE-EFF-014` | |
| `ECO-FRONT-06` | nouvelle | `LANG-JS-006` | |
| `ECO-FRONT-07` | nouvelle | `LANG-JS-007` | |
| `ECO-FRONT-08` | couverte | `LANG-CSS-001` | |
| `ECO-FRONT-09` | nouvelle | `LANG-HTML-004` | |
| `ECO-FRONT-10` | nouvelle | `LANG-CSS-004` | |
| `ECO-FRONT-11` | nouvelle | `LANG-CSS-004` | |
| `ECO-FRONT-12` | nouvelle | `LANG-CSS-004` | |
| `ECO-FRONT-13` | couverte | `WEB-EFF-001` | |
| `ECO-FRONT-14` | couverte | `NET-EFF-004` | |
| `ECO-BACK-01` | couverte | `DB-EFF-001`, `DB-EFF-003`, `DB-EFF-004` | |
| `ECO-BACK-02` | nouvelle | `DB-EFF-011` | |
| `ECO-BACK-03` | couverte | `CODE-EFF-008` | |
| `ECO-BACK-04` | couverte | `API-EFF-001`, `CODE-EFF-003` | |
| `ECO-BACK-05` | couverte | `CODE-EFF-001` | |
| `ECO-BACK-06` | couverte | `CODE-EFF-002` | |
| `ECO-BACK-07` | couverte | `CODE-EFF-005` | |
| `ECO-BACK-08` | couverte | `CODE-EFF-010` | |
| `ECO-BACK-09` | couverte | `API-EFF-001` | |
| `ECO-BACK-10` | couverte | `DB-EFF-010` | |
| `ECO-BACK-11` | couverte | `ARCH-NOSQL-001`, `ARCH-NOSQL-002` | |
| `ECO-BACK-12` | couverte | `ARCH-DATA-001`, `ARCH-DATA-002` | |
| `ECO-BACK-13` | couverte | `DB-EFF-007` | |
| `ECO-HEB-01` | couverte | `INFRA-EFF-001`, `OPS-EFF-002` | |
| `ECO-HEB-02` | nouvelle | `WEB-EFF-008` | |
| `ECO-HEB-03` | couverte | `NET-EFF-002` | |
| `ECO-HEB-04` | nouvelle | `NET-EFF-005` | |
| `ECO-HEB-05` | nouvelle | `NET-EFF-005` | |
| `ECO-HEB-06` | nouvelle | `WEB-EFF-009` | |
| `ECO-HEB-07` | nouvelle | `INFRA-EFF-006` | |
| `ECO-HEB-08` | couverte | `INFRA-EFF-002` | |
| `ECO-HEB-09` | couverte | `INFRA-EFF-001` | |
| `ECO-HEB-10` | couverte | `DB-EFF-006` | |
| `ECO-HEB-11` | couverte | `DB-EFF-008` | |
| `ECO-HEB-12` | couverte | `OPS-EFF-001` | |
| `ECO-ALGO-01` | couverte | `AI-EFF-001` | |
| `ECO-ALGO-02` | adaptée | `AI-EFF-002`, `USAGE-CODEX-COMPUTE-01` | L'exemple de commande Claude est remplacé par le réglage du modèle et de l'effort de raisonnement dans Codex. |
| `ECO-ALGO-03` | nouvelle | `AI-EFF-007` | |
| `ECO-ALGO-04` | couverte | `AI-EFF-002` | |
| `ECO-ALGO-05` | couverte | `AI-EFF-002` | |
| `ECO-ALGO-06` | couverte | `AI-EFF-003` | |
| `ECO-ALGO-07` | couverte | `AI-EFF-005` | |
| `ECO-ALGO-08` | couverte | `AI-EFF-001`, `AI-EFF-002` | |
| `ECO-ALGO-09` | nouvelle | `AI-EFF-009` | |
| `ECO-ALGO-10` | nouvelle | `AI-EFF-008` | Le fichier imposé `IA_MEASUREMENTS.md` n'est pas repris. |
| `ECO-ALGO-11` | nouvelle | `AI-EFF-008` | |
| `ECO-ALGO-12` | couverte | `AI-EFF-006` | |
| `ECO-ALGO-13` | couverte | `AI-EFF-006` | |
| `ECO-ALGO-14` | nouvelle | `AI-EFF-011` | |
| `ECO-ALGO-15` | couverte | `AI-EFF-003`, `CODE-EFF-003` | |
| `ECO-ALGO-16` | couverte | `AI-EFF-003` | |
| `ECO-ALGO-17` | couverte | `AI-EFF-002` | |
| `ECO-ALGO-18` | couverte | `AI-EFF-004` | |
| `ECO-ALGO-19` | couverte | `AI-EFF-001` | |
| `ECO-ALGO-20` | couverte | `AI-EFF-001` | |
| `ECO-ALGO-21` | couverte | `AI-EFF-001`, `AI-EFF-002` | |
| `ECO-ALGO-22` | nouvelle | `AI-EFF-010` | |
| `ECO-ALGO-23` | nouvelle | `AI-EFF-010` | |
| `ECO-ALGO-24` | nouvelle | `AI-EFF-010` | |
| `ECO-ALGO-25` | nouvelle | `AI-EFF-012` | |
| `ECO-ALGO-26` | couverte | `AI-EFF-003` | |
| `ECO-ALGO-27` | nouvelle | `AI-EFF-012` | |
| `ECO-HOST-01` | couverte | `AI-EFF-004` | |
| `ECO-HOST-02` | couverte | `AI-EFF-004`, `INFRA-EFF-003` | |
| `ECO-HOST-03` | couverte | `INFRA-EFF-001`, `INFRA-EFF-002` | |
| `ECO-HOST-04` | couverte | `AI-EFF-004` | |

## Langages (`langages/*.json`)

| ID Green Claude | Statut | ID Green Codex | Raison |
| --- | --- | --- | --- |
| `ECO-NG-01` | couverte | `LANG-ANGULAR-001` | |
| `ECO-NG-02` | couverte | `LANG-ANGULAR-001` | |
| `ECO-NG-03` | couverte | `LANG-ANGULAR-003` | |
| `ECO-ASTRO-01` | couverte | `LANG-ASTRO-003` | |
| `ECO-ASTRO-02` | couverte | `LANG-ASTRO-002` | |
| `ECO-C-01` | couverte | `LANG-C-001` | |
| `ECO-C-02` | couverte | `LANG-C-002` | |
| `ECO-C-03` | nouvelle | `LANG-C-004` | |
| `ECO-C-04` | nouvelle | `LANG-C-004` | |
| `ECO-C-05` | nouvelle | `LANG-C-005` | |
| `ECO-C-06` | nouvelle | `CODE-EFF-017` | |
| `ECO-CPP-01` | couverte | `LANG-CPP-001` | |
| `ECO-CPP-02` | couverte | `LANG-CPP-002` | |
| `ECO-CPP-03` | nouvelle | `LANG-CPP-004` | |
| `ECO-CPP-04` | couverte | `CODE-EFF-009` | |
| `ECO-CPP-05` | couverte | `CODE-EFF-004` | |
| `ECO-CPP-06` | nouvelle | `CODE-EFF-017` | |
| `ECO-CS-01` | nouvelle | `LANG-CSHARP-001` | |
| `ECO-CS-02` | nouvelle | `LANG-CSHARP-002` | |
| `ECO-CS-03` | nouvelle | `LANG-CSHARP-003` | |
| `ECO-CS-04` | nouvelle | `LANG-CSHARP-004` | |
| `ECO-CS-05` | nouvelle | `LANG-CSHARP-005` | |
| `ECO-CS-06` | nouvelle | `CODE-EFF-017` | |
| `ECO-CS-07` | nouvelle | `LANG-CSHARP-006` | |
| `ECO-CS-08` | nouvelle | `LANG-CSHARP-007` | |
| `ECO-GO-01` | couverte | `LANG-GO-001` | |
| `ECO-GO-02` | nouvelle | `CODE-EFF-017` | |
| `ECO-GO-03` | nouvelle | `LANG-GO-005` | |
| `ECO-GO-04` | couverte | `LANG-GO-003` | |
| `ECO-GO-05` | nouvelle | `LANG-GO-006` | |
| `ECO-GO-06` | nouvelle | `LANG-GO-006` | |
| `ECO-JAVA-01` | couverte | `DB-EFF-002` | |
| `ECO-JAVA-02` | nouvelle | `LANG-JAVA-006` | |
| `ECO-JAVA-03` | couverte | `LANG-JAVA-005` | |
| `ECO-JAVA-04` | nouvelle | `LANG-JAVA-007` | |
| `ECO-JAVA-05` | couverte | `CODE-EFF-009`, `LANG-JAVA-004` | |
| `ECO-JAVA-06` | couverte | `LANG-JAVA-001` | |
| `ECO-JAVA-07` | couverte | `CODE-EFF-010` | |
| `ECO-JAVA-08` | nouvelle | `CODE-EFF-017` | |
| `ECO-JS-01` | nouvelle | `LANG-JS-008` | |
| `ECO-JS-02` | nouvelle | `LANG-JS-009` | |
| `ECO-JS-03` | couverte | `WEB-EFF-003` | |
| `ECO-JS-04` | couverte | `LANG-JS-001` | |
| `ECO-JS-05` | couverte | `CODE-EFF-009` | |
| `ECO-JS-06` | couverte | `LANG-JS-003` | |
| `ECO-JS-07` | couverte | `LANG-JS-003` | |
| `ECO-JS-08` | couverte | `LANG-JS-004` | |
| `ECO-JS-09` | couverte | `LANG-JS-002`, `CODE-EFF-003` | |
| `ECO-JULIA-01` | couverte | `LANG-JULIA-001` | |
| `ECO-JULIA-02` | couverte | `LANG-JULIA-001` | |
| `ECO-JULIA-03` | couverte | `LANG-JULIA-002` | |
| `ECO-KT-01` | couverte | `LANG-KOTLIN-002` | |
| `ECO-KT-02` | couverte | `LANG-KOTLIN-002` | |
| `ECO-KT-03` | couverte | `LANG-KOTLIN-002` | |
| `ECO-KT-04` | couverte | `LANG-KOTLIN-001` | |
| `ECO-KT-05` | couverte | `CODE-EFF-009` | |
| `ECO-NIM-01` | couverte | `LANG-NIM-001` | |
| `ECO-NIM-02` | couverte | `LANG-NIM-002` | |
| `ECO-NIM-03` | couverte | `LANG-NIM-001` | |
| `ECO-PHP-01` | couverte | `LANG-PHP-002`, `DB-EFF-002` | |
| `ECO-PHP-02` | nouvelle | `LANG-PHP-003` | |
| `ECO-PHP-03` | nouvelle | `LANG-PHP-003` | |
| `ECO-PHP-04` | couverte | `LANG-PHP-001`, `LANG-PHP-002` | |
| `ECO-PHP-05` | couverte | `CODE-EFF-009` | |
| `ECO-PHP-06` | couverte | `LANG-PHP-001` | |
| `ECO-PHP-07` | couverte | `LANG-PHP-002`, `CODE-EFF-003` | |
| `ECO-PY-01` | nouvelle | `LANG-PYTHON-006` | |
| `ECO-PY-02` | couverte | `LANG-PYTHON-001`, `DB-EFF-002` | |
| `ECO-PY-03` | nouvelle | `LANG-PYTHON-006` | |
| `ECO-PY-04` | nouvelle | `LANG-PYTHON-006` | |
| `ECO-PY-05` | couverte | `LANG-PYTHON-001` | |
| `ECO-PY-06` | couverte | `LANG-PYTHON-002` | |
| `ECO-PY-07` | couverte | `CODE-EFF-009` | |
| `ECO-PY-08` | couverte | `CODE-EFF-009` | |
| `ECO-PY-09` | couverte | `CODE-EFF-003` | |
| `ECO-PY-10` | couverte | `LANG-PYTHON-005` | |
| `ECO-PY-11` | nouvelle | `CODE-EFF-017` | |
| `ECO-REACT-01` | nouvelle | `LANG-REACT-004` | |
| `ECO-REACT-02` | couverte | `LANG-REACT-002`, `LANG-REACT-003` | |
| `ECO-REACT-03` | couverte | `LANG-REACT-001` | |
| `ECO-RB-01` | couverte | `LANG-RUBY-001` | |
| `ECO-RB-02` | nouvelle | `LANG-RUBY-003` | |
| `ECO-RB-03` | nouvelle | `LANG-RUBY-003` | |
| `ECO-RB-04` | couverte | `CODE-EFF-009` | |
| `ECO-RB-05` | couverte | `CODE-EFF-009` | |
| `ECO-RB-06` | couverte | `CODE-EFF-003` | |
| `ECO-RB-07` | couverte | `LANG-RUBY-002`, `CODE-EFF-017` | |
| `ECO-RS-01` | couverte | `LANG-RUST-001` | |
| `ECO-RS-02` | couverte | `LANG-RUST-001` | |
| `ECO-RS-03` | couverte | `LANG-RUST-003` | |
| `ECO-RS-04` | couverte | `LANG-RUST-002` | |
| `ECO-RS-05` | nouvelle | `LANG-RUST-004` | |
| `ECO-RS-06` | couverte | `CODE-EFF-015` | |
| `ECO-RS-07` | nouvelle | `LANG-RUST-005` | |
| `ECO-SCALA-01` | couverte | `LANG-SCALA-002` | |
| `ECO-SCALA-02` | couverte | `LANG-SCALA-002` | |
| `ECO-SCALA-03` | nouvelle | `LANG-SCALA-003` | |
| `ECO-SH-01` | couverte | `LANG-SHELL-001` | |
| `ECO-SH-02` | couverte | `LANG-SHELL-001` | |
| `ECO-SH-03` | couverte | `LANG-SHELL-001` | |
| `ECO-SH-04` | couverte | `LANG-SHELL-003` | |
| `ECO-SH-05` | couverte | `LANG-SHELL-006` | |
| `ECO-SH-06` | nouvelle | `LANG-SHELL-007` | |
| `ECO-SOLID-01` | couverte | `LANG-SOLID-001` | |
| `ECO-SOLID-02` | nouvelle | `LANG-SOLID-004` | |
| `ECO-SQL-01` | couverte | `LANG-SQL-001` | |
| `ECO-SQL-02` | couverte | `API-EFF-001` | |
| `ECO-SQL-03` | nouvelle | `LANG-SQL-004` | |
| `ECO-SQL-04` | nouvelle | `LANG-SQL-005` | |
| `ECO-SQL-05` | couverte | `DB-EFF-004` | |
| `ECO-SQL-06` | couverte | `LANG-SQL-003`, `LANG-PLSQL-001` | |
| `ECO-SQL-07` | couverte | `LANG-SQL-002`, `LANG-PLSQL-003` | |
| `ECO-SQL-08` | nouvelle | `LANG-SQL-006` | |
| `ECO-SQL-09` | couverte | `CODE-EFF-010` | |
| `ECO-SQL-10` | nouvelle | `LANG-SQL-007` | |
| `ECO-SQL-11` | couverte | `DB-EFF-005`, `DB-EFF-006` | |
| `ECO-SVELTE-01` | couverte | `LANG-SVELTE-003` | |
| `ECO-SVELTE-02` | couverte | `LANG-SVELTE-001` | |
| `ECO-SW-01` | nouvelle | `LANG-SWIFT-001` | |
| `ECO-SW-02` | nouvelle | `LANG-SWIFT-002` | |
| `ECO-SW-03` | nouvelle | `LANG-SWIFT-003` | |
| `ECO-SW-04` | nouvelle | `LANG-SWIFT-004` | |
| `ECO-SW-05` | nouvelle | `LANG-SWIFT-005` | |
| `ECO-VUE-01` | couverte | `LANG-VUE-001` | |
| `ECO-VUE-02` | couverte | `LANG-VUE-002` | |
| `ECO-ZIG-01` | couverte | `LANG-ZIG-001` | |
| `ECO-ZIG-02` | nouvelle | `LANG-ZIG-003` | |

## Usage (`usage.json`)

| ID Green Claude | Statut | ID Green Codex | Raison |
| --- | --- | --- | --- |
| `USAGE-CTX-01` | couverte | `USAGE-CODEX-CTX-01` |  |
| `USAGE-CTX-02` | adaptée | `USAGE-CODEX-CTX-02` | Le retour en arrière de Claude Code est remplacé par `/fork` et `codex fork`, documentés pour Codex ; un fork ne sert pas d'annulation. |
| `USAGE-CTX-03` | adaptée | `USAGE-CODEX-CTX-03`, `USAGE-CODEX-CTX-04` | `/clear` est complété par `/new`, et `/compact` est conservé, selon la référence des commandes Codex. |
| `USAGE-CTX-04` | couverte | `USAGE-CODEX-CTX-04` |  |
| `USAGE-CTX-05` | adaptée | `USAGE-CODEX-CTX-05` | La règle visait l'agent Claude ; elle s'applique à Codex sans autre changement. |
| `USAGE-BRIEF-01` | couverte | `USAGE-CODEX-BRIEF-01` |  |
| `USAGE-BRIEF-02` | couverte | `USAGE-CODEX-BRIEF-02` |  |
| `USAGE-BRIEF-03` | nouvelle | `USAGE-CODEX-BRIEF-03` |  |
| `USAGE-MEM-01` | adaptée | `USAGE-CODEX-MEM-01` | `CLAUDE.md` est remplacé par `AGENTS.md`. |
| `USAGE-MEM-02` | couverte | `USAGE-CODEX-MEM-02` |  |
| `USAGE-MEM-03` | couverte | `CODE-EFF-016` |  |
| `USAGE-VERIF-01` | adaptée | `USAGE-CODEX-VERIFY-01` | La règle visait l'agent Claude ; elle s'applique à Codex sans autre changement. |
| `USAGE-CPU-03` | adaptée | `USAGE-CODEX-COMPUTE-03` | L'option `--bare` de Claude Code est remplacée par une exécution minimale avec `codex exec`. |

## Sobriété des tokens (`tokens.json`)

Les 30 règles gardent leur identifiant. Green Codex conserve sa rédaction française, de même substance.

| ID Green Claude | Statut | ID Green Codex | Raison |
| --- | --- | --- | --- |
| `NR-TOK-001` | couverte | `NR-TOK-001` |  |
| `NR-TOK-002` | couverte | `NR-TOK-002` |  |
| `NR-TOK-003` | couverte | `NR-TOK-003` |  |
| `NR-TOK-004` | couverte | `NR-TOK-004` |  |
| `NR-TOK-005` | couverte | `NR-TOK-005` |  |
| `NR-TOK-006` | couverte | `NR-TOK-006` |  |
| `NR-TOK-007` | couverte | `NR-TOK-007` |  |
| `NR-TOK-008` | couverte | `NR-TOK-008` |  |
| `NR-TOK-009` | couverte | `NR-TOK-009` |  |
| `NR-TOK-010` | couverte | `NR-TOK-010` |  |
| `NR-TOK-011` | couverte | `NR-TOK-011` |  |
| `NR-TOK-012` | adaptée | `NR-TOK-012` | `CLAUDE.md` est remplacé par les fichiers d'instructions équivalents des autres agents. |
| `NR-TOK-013` | couverte | `NR-TOK-013` |  |
| `NR-TOK-014` | couverte | `NR-TOK-014` |  |
| `NR-TOK-015` | couverte | `NR-TOK-015` |  |
| `NR-TOK-016` | couverte | `NR-TOK-016` |  |
| `NR-TOK-017` | couverte | `NR-TOK-017` |  |
| `NR-TOK-018` | couverte | `NR-TOK-018` |  |
| `NR-TOK-019` | couverte | `NR-TOK-019` |  |
| `NR-TOK-020` | couverte | `NR-TOK-020` |  |
| `NR-TOK-021` | couverte | `NR-TOK-021` |  |
| `NR-TOK-022` | couverte | `NR-TOK-022` |  |
| `NR-TOK-023` | couverte | `NR-TOK-023` |  |
| `NR-TOK-024` | couverte | `NR-TOK-024`, `USAGE-CODEX-COMPUTE-02` |  |
| `NR-TOK-025` | couverte | `NR-TOK-025` |  |
| `NR-TOK-026` | couverte | `NR-TOK-026` |  |
| `NR-TOK-027` | couverte | `NR-TOK-027` |  |
| `NR-TOK-028` | couverte | `NR-TOK-028` |  |
| `NR-TOK-029` | couverte | `NR-TOK-029` |  |
| `NR-TOK-030` | couverte | `NR-TOK-030` |  |
