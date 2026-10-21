"""Render the silent installation walkthrough using Pillow and local FFmpeg."""

import argparse
import shutil
import subprocess
from pathlib import Path

from PIL import Image, ImageDraw, ImageFont


ROOT = Path(__file__).resolve().parents[1]
WIDTH, HEIGHT, FPS = 1280, 720, 10
BLUE, TEAL, INK = "#0d3280", "#006b80", "#172b46"
SCENES = [
    (0, 6, "Installer Green Codex", "Un skill pour le Numérique Responsable",
     ["Première installation sur macOS ou Linux", "Git et Codex doivent déjà être installés."],
     "Les commandes sont disponibles sous la vidéo."),
    (6, 19, "Récupérer le projet", "Dans votre terminal",
     ["git clone \\",
      "  https://github.com/Institut-du-Numerique-Responsable/green-codex.git",
      "cd green-codex"],
     "Placez-vous dans le dossier du dépôt téléchargé."),
    (19, 32, "Copier le skill", "Depuis la racine du dépôt",
     ["mkdir -p ~/.agents/skills",
      "cp -R green-codex ~/.agents/skills/green-codex"],
     "Si le dossier cible existe déjà, consultez le guide avant de le modifier."),
    (32, 40, "Vérifier la copie", "Dans votre terminal",
     ["ls ~/.agents/skills/green-codex/SKILL.md"],
     "Le chemin du fichier doit s’afficher sans erreur."),
    (40, 50, "Utiliser Green Codex", "Dans Codex CLI ou l’extension IDE, sur votre projet",
     ["$green-codex", "Examine ce projet et propose des améliorations", "d’écoconception vérifiables."],
     "Si le skill n’apparaît pas, redémarrez Codex."),
]


def font_path(candidates):
    for candidate in candidates:
        if Path(candidate).is_file():
            return candidate
    raise SystemExit("Install Arial/Menlo or DejaVu fonts to render the video.")


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--output", type=Path, default=ROOT / "docs/media")
    parser.add_argument("--preview", type=Path, help="Optional contact sheet for review")
    args = parser.parse_args()
    if not shutil.which("ffmpeg"):
        raise SystemExit("FFmpeg is required.")
    regular = font_path(["/System/Library/Fonts/Supplemental/Arial.ttf",
                         "/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf"])
    bold = font_path(["/System/Library/Fonts/Supplemental/Arial Bold.ttf",
                      "/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf"])
    mono = font_path(["/System/Library/Fonts/Menlo.ttc",
                      "/usr/share/fonts/truetype/dejavu/DejaVuSansMono.ttf"])
    fonts = {"title": ImageFont.truetype(bold, 52),
             "body": ImageFont.truetype(regular, 27),
             "small": ImageFont.truetype(regular, 22),
             "code": ImageFont.truetype(mono, 25),
             "label": ImageFont.truetype(bold, 24)}
    args.output.mkdir(parents=True, exist_ok=True)
    logo = Image.open(ROOT / "docs/images/inr-logo.webp").convert("RGB")
    logo.thumbnail((214, 68))

    def frame(scene, elapsed, progress):
        start, end, title, subtitle, lines, note = scene
        picture = Image.new("RGB", (WIDTH, HEIGHT), "#f0f5f9")
        draw = ImageDraw.Draw(picture)
        draw.rectangle((0, 0, WIDTH, 100), fill="white")
        picture.paste(logo, (52, 17))
        draw.text((925, 36), "Green Codex / Installation", font=fonts["small"], fill=BLUE)
        draw.text((62, 135), title, font=fonts["title"], fill=BLUE)
        draw.text((65, 208), subtitle, font=fonts["body"], fill=TEAL)
        draw.rounded_rectangle((60, 272, 1220, 555), radius=12, fill="white", outline="#d6e0e9", width=2)
        draw.text((88, 292), "Guide animé" if start == 0 else "Codex" if start == 40 else "Terminal",
                  font=fonts["label"], fill=TEAL)
        y = 355
        for index, line in enumerate(lines):
            # Reveal whole lines, leaving most of the scene available for reading.
            if elapsed >= index * .65:
                font = fonts["body"] if start == 0 else fonts["code"]
                if draw.textlength(line, font=font) > 1100:
                    raise ValueError(f"Line exceeds the safe frame area: {line}")
                draw.text((88, y), line, font=font, fill=INK)
            y += 57
        if draw.textlength(note, font=fonts["small"]) > 1150:
            raise ValueError("Instruction exceeds the safe frame area")
        draw.text((65, 588), note, font=fonts["small"], fill=INK)
        draw.text((65, 658), "Démonstration animée • Sans audio • Commandes à exécuter sur votre machine",
                  font=fonts["small"], fill="#506176")
        draw.rectangle((0, 710, WIDTH, HEIGHT), fill="#d6e0e9")
        draw.rectangle((0, 710, int(WIDTH * progress), HEIGHT), fill=TEAL)
        return picture

    destination = args.output / "installation-greencodex.mp4"
    command = ["ffmpeg", "-hide_banner", "-loglevel", "error", "-y",
               "-f", "rawvideo", "-pix_fmt", "rgb24", "-s", f"{WIDTH}x{HEIGHT}",
               "-r", str(FPS), "-i", "pipe:0", "-an", "-c:v", "libx264",
               "-preset", "medium", "-tune", "stillimage", "-crf", "24",
               "-pix_fmt", "yuv420p", "-movflags", "+faststart", str(destination)]
    with subprocess.Popen(command, stdin=subprocess.PIPE) as process:
        try:
            for scene in SCENES:
                for tick in range((scene[1] - scene[0]) * FPS):
                    elapsed = tick / FPS
                    picture = frame(scene, elapsed, (scene[0] + elapsed) / 50)
                    process.stdin.write(picture.tobytes())
        finally:
            process.stdin.close()
        if process.wait() != 0:
            raise SystemExit("Video encoding failed.")
    frame(SCENES[0], 5, 0).save(args.output / "installation-poster.webp", quality=85)
    if args.preview:
        sheet = Image.new("RGB", (640, 360 * len(SCENES)), "white")
        for index, scene in enumerate(SCENES):
            thumbnail = frame(scene, 4, scene[0] / 50).resize((640, 360))
            sheet.paste(thumbnail, (0, index * 360))
        sheet.save(args.preview)
    print(f"Rendered 50 seconds, 1280x720, {FPS} fps: {destination.stat().st_size:,} bytes")


if __name__ == "__main__":
    main()
