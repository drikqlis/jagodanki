from datetime import datetime

from flask import Flask, render_template

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

PROJECTS = [
    {
        "title": "Szponcenie w wielkim mieście",
        "role": "Autorka reportażu",
        "date": "2025",
        "description": (
            "Cykl reportaży o codziennym życiu Wrocławskich szponcicieli — "
            "o wyzwaniach, marzeniach i poszukiwaniu swojego miejsca. "
            "Opublikowany gdzieś w mojej szufladzie."
        ),
        "image": "placeholder-1.svg",
        "color": "#A855F7",
        "url": "#",
    },
    {
        "title": "Memiczne Podsumowania Sesji",
        "role": "Relacja i wywiady",
        "date": "2025",
        "description": (
            "Skromnie mówiąc arcydzieła współczesnego kina mówiące o sytuacjach zabawnych, smutnych czy pojebanych, które odbyły się na sesji."
        ),
        "image": "placeholder-2.svg",
        "color": "#F97316",
        "url": "#",
    },
    {
        "title": "Blogaski o niczym konkretnym",
        "role": "Autorka tekstu",
        "date": "2024",
        "description": (
            "Opowiadania o tym co mi akurat przyjdzie do głowy z nieregularną częstotliwością (choć się staram). Głównie o całym tym otaczającym nas świecie i Jagodzie wokół którego się kręci."
        ),
        "image": "placeholder-3.svg",
        "color": "#22D3EE",
        "url": "#",
    },
    {
        "title": "Malunki różnorakie",
        "role": "Artystka",
        "date": "2024",
        "description": (
            "Rysunki i sztuka przy której Idzi widzi, że lepiej się tego odjebać nie dało. Zapierająca dech w piersiach tak, że trzeba usiąść i się powachlować. Nie dla osób ze słabym sercem."
        ),
        "image": "placeholder-4.svg",
        "color": "#F43F5E",
        "url": "#",
    },
]


@app.context_processor
def inject_year():
    return {"current_year": datetime.now().year}


@app.route("/")
def index():
    return render_template("index.html", bio=BIO, projects=PROJECTS)


if __name__ == "__main__":
    app.run(debug=True, port=5000)
