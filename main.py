from json import encoder

from flask import Flask, request, jsonify, render_template, redirect, url_for



app = Flask(__name__)
app.json.ensure_ascii = False

profile_data = {
    "name": "Михайло",
    "age": 17,
    "city": "Франківськ",
    "skills": ["Python", "JS", "HTML/CSS", "Git", "SQL"],
    "projects": [
        {
            "id": 1,
            "title": "Сайт-візитка",
            "description": "Персональний вебсайт на Flask з інформацією про себе та проєкти."
        },
        {
            "id": 2,
            "title": "Телеграм-бот",
            "description": "Бот для автоматизації відповідей та нагадувань."
        },
        {
            "id": 3,
            "title": "Парсер новин",
            "description": "Скрипт для збору та аналізу новин з популярних сайтів."
        }
    ]
}

@app.route("/")
def index():
    return render_template("index.html", data=profile_data)

@app.route("/about")
def about():
    return render_template("about.html", data=profile_data)

@app.route("/skills")
def skills():
    return render_template("skills.html", skills=profile_data["skills"])

@app.route("/project/<int:project_id>")
def project_detail(project_id):
    project = next((p for p in profile_data["projects"] if p["id"] == project_id), None)
    if project is None:
        return render_template("error.html"), 404
    return render_template("project.html", project=project)


if __name__ == '__main__':
    app.run(debug=True)