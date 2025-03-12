class filme {
    constructor(titulo, episodios, nota, streaming, opniao) {
        this.titulo = titulo
        this.episodios = episodios
        this.nota = nota
        this.streaming = streaming
        this.opniao = opniao
    }
}

class FilmeCadastro {
    constructor() {
        this.filme = []
        this.indiceEdicao = null
    }

    adicionarFilme(filme) {
        if (this.indiceEdicao !== null) {
            this.atualizarFilme(filme)
        } else {
            this.filme.push(filme)
        }
        this.atualizartabela()
        this.limparFormulario()
    }

    removerfilme(indice) {
        this.filme.splice(indice, 1)
        this.atualizartabela()
    }

    editarfilme(indice) {
        const filmes = this.filme[indice]

        document.getElementById('titulo').value = filmes.titulo
        document.getElementById('episodios').value = filmes.episodios
        document.getElementById('nota').value = filmes.nota
        document.getElementById('streaming').value = filmes.streaming
        document.getElementById('opniao').value = filmes.opniao

        this.indiceEdicao = indice;
        this.alternarBotoes(true)
    }

    adicionarFilme(filme) {
        if (this.indiceEdicao !== null) {
            this.filme[this.indiceEdicao] = filme
            this.indiceEdicao = null 
            this.alternarBotoes(false)
        } else {
            this.filme.push(filme)
        }
        this.atualizartabela()
        this.limparFormulario()
    }
    
    atualizartabela() {
        let tabela = document.getElementById('tabela')
        tabela.innerHTML = ''

        for (let i = 0; i < this.filme.length; i++) {
            const filmes = this.filme[i]

            const linha = document.createElement("tr")
            linha.innerHTML = `
            <td>${filmes.titulo}</td>
            <td>${filmes.episodios}</td>
            <td>${filmes.nota}</td>
            <td>${filmes.opniao}</td>
            <td>${filmes.streaming}</td>
            <td>
                <button onclick="filmeCadastro.editarfilme(${i})" class="btn btn-warning">Editar</button>
                <button onclick="filmeCadastro.removerfilme(${i})" class="btn btn-danger">Excluir</button>
            </td>
            `
            tabela.appendChild(linha)
        }
    }

    limparFormulario() {
        document.getElementById('filmeForm').reset()
    }

    alternarBotoes(editando) {
        document.getElementById('adicionarBtn').style.display = editando ? 'none' : 'inline-block'
        document.getElementById('atualizarBtn').style.display = editando ? 'inline-block' : 'none'
    }
}

const filmeCadastro = new FilmeCadastro()

const formulario = document.getElementById('filmeForm')
formulario.addEventListener('submit', function (evento) {
    evento.preventDefault()

    const titulo = document.getElementById('titulo').value
    const episodios = document.getElementById('episodios').value
    const nota = document.getElementById('nota').value
    const streaming = document.getElementById('streaming').value
    const opniao = document.getElementById('opniao').value

    const Filme = new filme(titulo, episodios, nota, streaming, opniao)
    filmeCadastro.adicionarFilme(Filme)
})

document.getElementById('atualizarBtn').addEventListener('click', function () {
    const titulo = document.getElementById('titulo').value
    const episodios = document.getElementById('episodios').value
    const nota = document.getElementById('nota').value
    const streaming = document.getElementById('streaming').value
    const opniao = document.getElementById('opniao').value

    const Filme = new filme(titulo, episodios, nota, streaming, opniao)
    filmeCadastro.atualizarFilme(Filme)
})
