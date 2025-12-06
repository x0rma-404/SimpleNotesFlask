from flask import Flask, render_template, jsonify, request
import json
import os

app = Flask(__name__)
NOTES_FILE = 'notes.json'

# Dosyadan notları oku veya yoksa oluştur
def load_notes():
    if os.path.exists(NOTES_FILE):
        with open(NOTES_FILE, 'r') as f:
            return json.load(f)
    else:
        # Dosya yoksa oluştur ve boş liste yaz
        with open(NOTES_FILE, 'w') as f:
            json.dump([], f)
        return []

# Dosyaya kaydet
def save_notes(notes):
    with open(NOTES_FILE, 'w') as f:
        json.dump(notes, f)

notes = load_notes()

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/add', methods=['POST'])
def add_note():
    data = request.get_json()
    notes.append(data['note'])
    save_notes(notes)
    return jsonify(notes)

@app.route('/delete/<int:index>', methods=['DELETE'])
def delete_note(index):
    if 0 <= index < len(notes):
        notes.pop(index)
        save_notes(notes)
    return jsonify(notes)

@app.route('/notes', methods=['GET'])
def get_notes():
    return jsonify(notes)

if __name__ == '__main__':
    app.run(debug=True)
