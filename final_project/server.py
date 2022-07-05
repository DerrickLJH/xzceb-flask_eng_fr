import json
import machinetranslation
from machinetranslation.translator import english_to_french, french_to_english
from flask import Flask, render_template, request

app = Flask("Web Translator", template_folder='templates')

@app.route("/englishToFrench")
def englishToFrench():
    textToTranslate = request.args.get('textToTranslate')
    french_text = english_to_french(textToTranslate)
    print(french_text)
    return "Translated text to French"

@app.route("/frenchToEnglish")
def frenchToEnglish():
    textToTranslate = request.args.get('textToTranslate')
    english_text = french_to_english(textToTranslate)
    print(english_text)
    return "Translated text to English"

@app.route("/")
def renderIndexPage():
    return render_template("index.html", index = True)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)
