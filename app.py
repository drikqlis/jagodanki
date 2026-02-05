import os
from datetime import datetime

import markdown
from flask import Flask, render_template
from markupsafe import Markup

app = Flask(__name__)

BIO = {
    "name": "Jagoda Skorupa",
    "tagline": "Dziennikarka · Artystka · Szponcicielka",
    "description": (
        "Jestem początkującą dziennikarką z pasją do opowiadania historii, "
        "które nie trzymają się kupy. Specjalizuję się w szponceniu "
        "i rysowankach. Wierzę, że każdy tekst może mieć jakiś podtekst "
        "jeśli jest się wystarczająco horny."
    ),
}

# Project types: video, graphic, text, audio
PROJECTS = [
    # VIDEO
    {
        "title": "Sesja Q&A",
        "role": "Filmik informacyjny",
        "date": "2025",
        "description": "Filmik informacyjny opublikowany na Instagramie Samorządu Studentów UWr.",
        "image": "sesja_qa.jpg",
        "color": "#2E5080",
        "url": "https://www.instagram.com/reel/DFa0rfboZB8/",
        "type": "video",
    },
    {
        "title": "Jazda po zdrowie",
        "role": "Przygotowanie materiału",
        "date": "2024",
        "description": "Przygotowanie materiału do programu na żywo realizowanego na studiach licencjackich.",
        "image": "jazda_po_zdrowie.jpg",
        "color": "#3D8280",
        "url": "https://youtu.be/dJLoeOW6V0I?t=2770",
        "type": "video",
    },
    # GRAPHICS
    {
        "title": "Krasnalcon 2024",
        "role": "Plakat",
        "date": "2024",
        "description": "Plakat na wydarzenie Krasnalcon 2024.",
        "image": "krasnalcon_plakat.png",
        "color": "#2E8A8C",
        "url": None,
        "type": "graphic",
    },
    {
        "title": "Teatralne Horyzonty",
        "role": "Plakat",
        "date": "2024",
        "description": "Plakat na wydarzenie Teatralne Horyzonty.",
        "image": "teatralne_horyzonty_plakat.png",
        "color": "#4968A5",
        "url": None,
        "type": "graphic",
    },
    {
        "title": "Aktywny Student",
        "role": "Grafika wydarzenia",
        "date": "2024",
        "description": "Zdjęcie w tle wydarzenia na Facebooku.",
        "image": "aktywny_student.jpg",
        "color": "#A83D7E",
        "url": "https://www.facebook.com/events/437915598720573",
        "type": "graphic",
    },
    {
        "title": "Rozgrywki Tajniaków",
        "role": "Grafika wydarzenia",
        "date": "2024",
        "description": "Zdjęcie w tle wydarzenia na Facebooku.",
        "image": "rozgrywki_tajniakow.jpg",
        "color": "#A52828",
        "url": "https://www.facebook.com/events/1657167788319637",
        "type": "graphic",
    },
    {
        "title": "Nieturystyka",
        "role": "Grafika wydarzenia",
        "date": "2024",
        "description": "Grafika na wydarzenie Nieturystyka oraz projekt logo.",
        "image": "nie_turystyka.jpg",
        "color": "#ed7d49",
        "url": "https://www.facebook.com/events/1712438526119606",
        "type": "graphic",
    },
    {
        "title": "Muzeum Przyrodnicze",
        "role": "Grafika",
        "date": "2024",
        "description": "Grafiki przygotowane na podstawie zdjęć zrobionych w Muzeum Przyrodniczym.",
        "image": "grafika_muzeum_combined.jpg",
        "images": ["grafika_muzeum_1.jpg", "grafika_muzeum_2.jpg", "grafika_muzeum_3.jpg"],
        "color": "#655890",
        "url": None,
        "type": "graphic",
    },
    # TEXTS
    {
        "title": '"Amsterdam" - recenzja',
        "role": "Recenzja filmu",
        "date": "2022",
        "description": "Recenzja filmu Davida O. Russella z gwiazdorską obsadą.",
        "image": "placeholder-1.svg",
        "color": "#EF4444",
        "url": "/tekst/amsterdam",
        "type": "text",
    },
    {
        "title": '"1899" - recenzja',
        "role": "Recenzja serialu",
        "date": "2022",
        "description": "Recenzja serialu twórców Dark na platformie Netflix.",
        "image": "placeholder-2.svg",
        "color": "#3B82F6",
        "url": "/tekst/1899",
        "type": "text",
    },
    {
        "title": "Pleśń na herbacie",
        "role": "Reportaż",
        "date": "2023",
        "description": "Reportaż o osobach transpłciowych w Polsce.",
        "image": "placeholder-3.svg",
        "color": "#649b11",
        "url": "/tekst/plesn-na-herbacie",
        "type": "text",
    },
    # AUDIO
    {
        "title": "Pomoc, która pachnie kawą",
        "role": "Reportaż audio",
        "date": "2024",
        "description": "Reportaż audio.",
        "image": "placeholder-4.svg",
        "color": "#D946EF",
        "url": "/audio/pomoc-ktora-pachnie-kawa",
        "type": "audio",
    },
]

ARTICLES = {
    "amsterdam": {
        "title": '"Amsterdam" - recenzja',
        "file": "amsterdam.md",
    },
    "1899": {
        "title": '"1899" - recenzja',
        "file": "1899.md",
    },
    "plesn-na-herbacie": {
        "title": "Pleśń na herbacie",
        "file": "plesn-na-herbacie.md",
    },
}

AUDIO_PAGES = {
    "pomoc-ktora-pachnie-kawa": {
        "title": "Pomoc, która pachnie kawą",
        "description": "Reportaż audio.",
        "audio_file": "pomoc_ktora_pachnie_kawa.mp3",
    },
}


def load_markdown(filename):
    content_dir = os.path.join(os.path.dirname(__file__), "content")
    filepath = os.path.join(content_dir, filename)
    with open(filepath, "r", encoding="utf-8") as f:
        text = f.read()
    return markdown.markdown(text)


@app.context_processor
def inject_year():
    return {"current_year": datetime.now().year}


@app.route("/")
def index():
    return render_template("index.html", bio=BIO, projects=PROJECTS)


@app.route("/tekst/<slug>")
def article(slug):
    if slug not in ARTICLES:
        return "Nie znaleziono artykułu", 404
    article_data = ARTICLES[slug]
    content = load_markdown(article_data["file"])
    return render_template(
        "article.html",
        title=article_data["title"],
        content=Markup(content),
    )


@app.route("/audio/<slug>")
def audio(slug):
    if slug not in AUDIO_PAGES:
        return "Nie znaleziono strony", 404
    audio_data = AUDIO_PAGES[slug]
    return render_template(
        "audio.html",
        title=audio_data["title"],
        description=audio_data["description"],
        audio_file=audio_data["audio_file"],
    )


if __name__ == "__main__":
    app.run(debug=True, port=5000)
