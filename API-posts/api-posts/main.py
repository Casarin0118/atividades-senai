from flask import Flask, request
from controller.post_controller import get_posts_ctrl, get_comentario_ctrl, get_comentarios_by_post_id_ctrl
from controller.post_controller import get_posts_by_id_ctrl
from werkzeug.utils import secure_filename
import os

app = Flask(__name__)

UPLOAD_PHOTO = 'photos'
app.config['UPLOAD_FOLDER'] = UPLOAD_PHOTO

ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg', 'gif'}

def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

if not os.path.exists(UPLOAD_PHOTO):
    os.makedirs(UPLOAD_PHOTO)

@app.route('/posts', methods=['GET'])
def get_posts():
    return get_posts_ctrl()

@app.route('/posts/<int:post_id>', methods=['GET'])
def get_posts_by_id(post_id):
    return get_posts_by_id_ctrl(post_id)

@app.route('/posts/comentarios', methods=['GET'])
def get_comentario():
    return get_comentario_ctrl()

@app.route('/posts/<int:post_id>/comentarios', methods=['GET'])
def get_comentarios_by_post_id(post_id):
    return get_comentarios_by_post_id_ctrl(post_id)

@app.route('/posts', methods=['POST'])
def create_post():
    if 'photo_post' in request.files:
        photo = request.files['photo_post']
        if photo and allowed_file(photo.filename):
            photo_name = secure_filename(photo.filename)
            photo_path = os.path.join(app.config['UPLOAD_FOLDER'], photo_name)
            photo.save(photo_path)
            return 'Post criado com sucesso!', 201
        else:
            return 'Tipo de arquivo inválido. Por favor, envie uma imagem.', 400
    else:
        return 'Arquivo não encontrado no post.', 400

if __name__ == '__main__':
    app.run(debug=True)
