from os.path import curdir

from database.conexao import get_connection
from models.post import Post, Comentario



def get_posts_ctrl():
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute(
        """SELECT post_id, author, title FROM posts;"""
    )
    resultados = cursor.fetchall()
    if len(resultados) == 0:
        return 'Sem resultados de posts'
    cursor.close()
    conn.close()
    posts=[]

    for i in resultados:
        post = Post(post_id=i[0], author=i[1], title=i[2])
        posts.append(post.to_json())

    return posts

def get_posts_by_id_ctrl(post_id):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute(
        """SELECT post_id, author, title FROM posts WHERE post_id =%s;""", (post_id,)
    )
    resultado = cursor.fetchone()

    if len(resultado) == 0:
        return 'Post não encontrado'

    cursor.close()
    conn.close()

    posts=[]
    post = Post(post_id = resultado[0], author=resultado[1], title=resultado[2])
    posts.append(post.to_json())
    return posts

def get_comentario_ctrl():
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute(
        """SELECT id_com, nome, comentario, post_id FROM  comentarios"""
    )
    resultado = cursor.fetchall()

    if len(resultado) == 0:
        return 'Comentário não encontrado'

    cursor.close()
    conn.close()

    comentarios = []

    for i in resultado:
        comentario = Comentario(id_com=i[0], nome=i[1], comentario=i[2], post_id=i[3])
        comentarios.append(comentario.to_json())
    return comentarios

def get_comentarios_by_post_id_ctrl(post_id):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute(
        """SELECT id_com, nome, comentario, post_id FROM comentarios WHERE post_id = %s;""", (post_id,)
    )
    resultado = cursor.fetchall()

    if len(resultado) == 0:
        return 'Comentários não encontrados para este post'

    cursor.close()
    conn.close()

    comentarios = []
    for i in resultado:
        comentario = Comentario(id_com=i[0], nome=i[1], comentario=i[2], post_id=i[3])
        comentarios.append(comentario.to_json())

    return comentarios

