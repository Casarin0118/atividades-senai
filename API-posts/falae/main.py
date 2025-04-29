from flask import Flask, render_template, request, jsonify, send_file
from gtts import gTTS
import os
from io import BytesIO

app = Flask(__name__)

# Lista de idiomas suportados
LANGUAGES = {
    'pt': 'Português',
    'en': 'Inglês',
    'es': 'Espanhol',
    'fr': 'Francês',
    'it': 'Italiano',
    'de': 'Alemão',
    'ja': 'Japonês'
}


@app.route('/')
def index():
    return render_template('index.html', languages=LANGUAGES)


@app.route('/speak', methods=['POST'])
def speak():
    data = request.json
    text = data.get('text', '')
    lang = data.get('lang', 'pt')

    if not text:
        return jsonify({'error': 'Nenhum texto fornecido'}), 400

    return jsonify({'message': 'Use a Web Speech API no navegador'})


@app.route('/download', methods=['POST'])
def download():
    data = request.json
    text = data.get('text', '')
    lang = data.get('lang', 'pt')

    if not text:
        return jsonify({'error': 'Nenhum texto fornecido'}), 400

    try:
        tts = gTTS(text=text, lang=lang)
        audio_file = BytesIO()
        tts.write_to_fp(audio_file)
        audio_file.seek(0)

        return send_file(
            audio_file,
            mimetype='audio/mpeg',
            as_attachment=True,
            download_name=f'audio_{lang}.mp3'
        )
    except Exception as e:
        return jsonify({'error': str(e)}), 500


if __name__ == '__main__':
    app.run(debug=True)