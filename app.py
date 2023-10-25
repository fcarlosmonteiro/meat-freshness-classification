from flask import Flask, render_template, jsonify, request, send_from_directory
from api import UPLOAD_FOLDER, allowed_file, load_and_preprocess_image, classify_meat
import pickle

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

app.config['STATIC_UPLOAD_FOLDER'] = 'upload'

model_path = 'classificacao_de_carne_random.pkl'
with open(model_path, 'rb') as model_file:
    try:
        model = pickle.load(model_file)
    except ValueError:
        model_file.seek(0)
        model = pickle.load(model_file, fix_imports=False)

@app.route('/')
def index():
    return render_template('index.html', result=None)

@app.route('/upload/<filename>')
def uploaded_file(filename):
    return send_from_directory(app.config['UPLOAD_FOLDER'], filename)

@app.route('/upload', methods=['POST'])
def upload_media():
    if 'file' not in request.files:
        return jsonify({'error': 'Media não fornecida', 'success': False})

    file = request.files['file']
    file_path = load_and_preprocess_image(file, app.config['UPLOAD_FOLDER'])

    if file_path:
        result = classify_meat(file_path, model)
        return jsonify(result)
    else:
        return jsonify({'error': 'Erro ao processar a imagem', 'success': False})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8081)
