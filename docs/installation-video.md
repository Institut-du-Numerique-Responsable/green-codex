# Vidéo d’installation

La page d’accueil propose une démonstration animée muette de 50 secondes, avec une
transcription HTML contenant les commandes copiables. Elle illustre une première
installation sur macOS ou Linux, avec Git et Codex déjà installés. Elle ne simule
aucune réponse de modèle ni installation réalisée sur la machine du visiteur.

## Contenu et mise à jour

- 0 à 6 secondes : objectif et prérequis.
- 6 à 19 secondes : clonage du dépôt et ouverture de son dossier.
- 19 à 32 secondes : copie dans `~/.agents/skills/green-codex`.
- 32 à 40 secondes : vérification de la présence de `SKILL.md`.
- 40 à 50 secondes : invocation dans Codex CLI ou l’extension IDE.

La [documentation officielle des skills](https://learn.chatgpt.com/docs/build-skills),
consultée le 21 octobre 2026, indique `~/.agents/skills` pour les skills personnels.
Une copie existante doit être examinée avant mise à jour. La présence du fichier ne
prouve pas sa détection dans Codex ; vérifier le sélecteur de skills et redémarrer
Codex si nécessaire. Une ancienne copie dans un autre emplacement peut créer un doublon.

Le scénario est défini dans `scripts/render-install-video.py`. Mettre à jour ensemble
le scénario, la transcription dans `docs/index.html` et le README si les commandes
évoluent. Le script ne lance aucune commande d’installation sur la machine qui génère
la vidéo. Le logo local reste celui de l’INR, utilisé pour identifier l’institution.

## Génération

Le générateur utilise Python, Pillow et FFmpeg avec l’encodeur libx264. Il cherche
Arial et Menlo sur macOS ou DejaVu Sans et DejaVu Sans Mono sur Linux. Les polices
servent à produire les images et ne sont pas distribuées comme fichiers de police.
Depuis la racine du dépôt, avec ces dépendances disponibles :

```sh
python3 scripts/render-install-video.py --preview /tmp/green-codex-video-preview.png
```

Le MP4 et l’affiche WebP sont écrits dans `docs/media/`. Le paramètre `--output`
permet de choisir un autre répertoire. La planche de contrôle reste hors du dépôt.
Le MP4 utilise H.264, yuv420p, 1 280 × 720 pixels, 10 images par seconde et faststart.
La version initiale pèse 208 067 octets. L’encodage peut varier selon les versions.

## Accessibilité et sobriété

Le lecteur natif possède ses contrôles, `preload="none"`, une affiche et aucune lecture
automatique ni boucle. La vidéo ne contient pas d’audio ; toutes les instructions
sont présentes à l’écran et dans la transcription accessible sous le lecteur.
Le téléchargement direct du MP4 reste possible. Aucun lecteur externe ni JavaScript
n’est ajouté. Le navigateur garde la décision finale sur son préchargement.

La vérification couvre les images des séquences, le décodage intégral du MP4, ses
caractéristiques et la copie du skill dans un répertoire temporaire. Elle ne prouve
pas la détection par toutes les versions de Codex. La lecture dans un navigateur
et le parcours clavier du lecteur restent à vérifier si aucun navigateur n’est disponible.
