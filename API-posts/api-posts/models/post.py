class Post:
    def __init__(self, post_id, author, title, ):
        self.post_id = post_id
        self.author = author
        self.title = title

    def to_json(self):
        return {
            "post_id": self.post_id,
            "author": self.author,
            "title": self.title,
        }

class Comentario:
    def __init__(self, id_com, nome, comentario, post_id):
        self.id_com = id_com
        self.nome = nome
        self.comentario = comentario
        self.post_id = post_id

    def to_json(self):
        return {
            "id_com": self.id_com,
            "nome":self.nome,
            "comentario": self.comentario,
            "post_id": self.post_id
        }