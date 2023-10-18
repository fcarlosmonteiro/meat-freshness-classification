import os
from werkzeug.utils import secure_filename
from PIL import Image
import numpy as np

UPLOAD_FOLDER = os.path.join(os.getcwd(), 'upload')
ALLOWED_EXTENSIONS = set(['jpg'])

def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

def load_and_preprocess_image(file, upload_folder):
    if file and allowed_file(file.filename):
        filename = secure_filename(file.filename)
        file_path = os.path.join(upload_folder, filename)
        file.save(file_path)
        return file_path
    else:
        return None

def preprocess_image_for_model(image_path):
    img = Image.open(image_path)
    img = img.convert('RGB')
    img = img.resize((100, 100))
    img_array = np.array(img) / 255.0
    return img_array.reshape(1, -1)

def predict_meat_class(image_array, model):
    classe_predita = model.predict(image_array)
    return classe_predita[0]

def classify_meat(image_path, model):
    image_array = preprocess_image_for_model(image_path)
    if image_array is not None:
        classe_predita = predict_meat_class(image_array, model)
        result = {
            'classification': 'Carne estragada!' if classe_predita == 1 else 'Carne Fresca!',
            'image_filename': os.path.basename(image_path),
            'success': True
        }
    else:
        result = {'error': 'Erro ao processar a imagem', 'success': False}
    
    return result
