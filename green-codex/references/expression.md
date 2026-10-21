# Expression et messages de commit

Ces consignes éditoriales propres à Green Codex s'appliquent à Codex et à ChatGPT
lorsqu'elles leur sont fournies. Elles couvrent les réponses, les documents rédigés,
les commentaires de code, les messages de commit et les descriptions de pull request,
dans toutes les langues. Elles ne constituent pas un critère environnemental.

## Consignes à reprendre dans Codex ou ChatGPT

- N'utilise jamais de tiret quadratin (Unicode U+2014), dans aucune langue.
  Utilise un point, une virgule, des parenthèses ou un deux-points selon le sens.
- Livre directement l'idée. Supprime toute formule qui annonce une idée au lieu de
  la livrer, y compris les préambules qui promettent une explication ou une conclusion.
- N'emploie aucune phrase pseudo-clivée. Formule directement le sujet, le verbe et
  le complément, sans isoler une proposition pour la reprendre avec un présentatif.
- N'emploie aucune tournure présentative emphatique ni aucune fausse subordination
  détachée. Rattache les propositions à leur phrase et nomme directement leur sujet.
- N'emploie aucune épanorthose : rédige une formulation précise sans correction
  rhétorique ajoutée après coup. Corrige toutefois explicitement une erreur factuelle
  découverte dans une réponse antérieure.
- N'emploie aucune anaphore verbale : évite la répétition du même verbe en tête
  de propositions ou de phrases successives pour produire un effet d'insistance.
- N'emploie aucune antithèse binaire : supprime les oppositions rhétoriques
  artificielles. Décris les différences factuelles utiles avec précision.
- N'annonce aucun dénombrement ni aucune énumération. Présente directement les
  éléments utiles. Les listes restent possibles lorsqu'elles facilitent la lecture,
  sans phrase qui en annonce le nombre ou le contenu.
- Relis chaque texte avant de le transmettre et reformule toute construction
  interdite. Conserve le sens, les faits, les limites et les preuves disponibles.

## Messages de commit

Chaque commit doit permettre à une personne extérieure au changement de comprendre
sa raison et son effet sans ouvrir le diff. Ces exigences valent aussi pour les
messages proposés, les commits de fusion et les messages de squash.

- Écris un titre précis qui décrit le changement concret. Évite les titres vagues
  et les messages générés automatiquement sans relecture.
- Explique la motivation et le comportement obtenu dans le corps du message lorsque
  le titre ne suffit pas. Adapte le détail à l'ampleur du changement.
- Mentionne les vérifications réellement effectuées et leur résultat. Signale une
  vérification non effectuée ainsi que toute limite importante. N'invente aucun test.
- Vérifie la correspondance entre le message et le diff effectivement retenu avant
  chaque commit. Retire les descriptions de travaux absents du commit.
- Applique les règles d'expression à l'ensemble du message. Relis le message final
  de fusion ou de squash avant de le valider.

Les commentaires dans le code expliquent les raisons utiles à la maintenance.
Une modification évidente ne nécessite pas un commentaire qui répète le code.

## Vérification

Contrôle l'absence du caractère U+2014 dans le texte rédigé, puis relis sa syntaxe
et son sens. Une recherche de caractères ne détecte pas les figures de style.
Pour un commit, compare aussi le titre, la motivation et les preuves au diff.
L'application par un modèle demande une relecture des sorties réelles ; la présence
de ces consignes dans un fichier ne garantit pas leur respect systématique.
