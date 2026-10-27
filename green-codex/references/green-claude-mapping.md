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
