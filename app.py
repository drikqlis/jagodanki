from datetime import datetime

from flask import Flask, render_template

app = Flask(__name__)

BIO = {
    "name": "Jagoda Skorupa",
    "tagline": "Dziennikarka · Reporterka · Studentka",
    "description": (
        "Jestem początkującą dziennikarką z pasją do opowiadania historii, "
        "które mają znaczenie. Specjalizuję się w reportażach społecznych "
        "i tematyce kulturalnej. Wierzę, że dobry tekst może zmienić "
        "sposób, w jaki patrzymy na świat wokół nas."
    ),
}

PROJECTS = [
    {
        "title": "Młodzi w wielkim mieście",
        "role": "Autorka reportażu",
        "date": "2025",
        "description": (
            "Cykl reportaży o codziennym życiu studentów w Krakowie — "
            "o wyzwaniach, marzeniach i poszukiwaniu swojego miejsca. "
            "Opublikowany w uczelnianym magazynie."
        ),
        "image": "placeholder-1.svg",
        "url": "#",
    },
    {
        "title": "Festiwal Kultury Niezależnej",
        "role": "Relacja i wywiady",
        "date": "2025",
        "description": (
            "Relacja z festiwalu kultury niezależnej w Warszawie. "
            "Rozmowy z artystami, muzykami i organizatorami o tym, "
            "czym jest niezależność w sztuce."
        ),
        "image": "placeholder-2.svg",
        "url": "#",
    },
    {
        "title": "Zielone miasto — ekologia w przestrzeni miejskiej",
        "role": "Autorka tekstu",
        "date": "2024",
        "description": (
            "Artykuł o inicjatywach ekologicznych w polskich miastach. "
            "Od ogrodów społecznych po zielone dachy — jak mieszkańcy "
            "zmieniają swoje otoczenie."
        ),
        "image": "placeholder-3.svg",
        "url": "#",
    },
    {
        "title": "Rozmowy z debiutantami",
        "role": "Prowadząca wywiady",
        "date": "2024",
        "description": (
            "Seria wywiadów z młodymi autorami debiutującymi na polskim "
            "rynku literackim. O procesie tworzenia, odrzuceniach "
            "i pierwszych sukcesach."
        ),
        "image": "placeholder-4.svg",
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
