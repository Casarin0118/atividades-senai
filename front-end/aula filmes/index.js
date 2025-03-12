class Carro {
    constructor(marca, modelo, ano, potencia, torque) {
        this.marca = marca;
        this.modelo = modelo;
        this.ano = ano;
        this.potencia = potencia;
        this.torque = torque;
    }
}

class CarroCadastro {
    constructor() {
        this.carros = [];
        this.indiceEdicao = null;
    }

    adicionarCarro(carro) {
        if (this.indiceEdicao !== null) {
            this.atualizarCarro(carro);
        } else {
            this.carros.push(carro);
            this.atualizartabela();
            this.limparFormulario();
        }
    }

    removerCarro(indice) {
        this.carros.splice(indice, 1);
        this.atualizartabela();
    }

    editarCarro(indice) {
        const carro = this.carros[indice];

        document.getElementById('marca').value = carro.marca;
        document.getElementById('modelo').value = carro.modelo;
        document.getElementById('ano').value = carro.ano;
        document.getElementById('potencia').value = carro.potencia;
        document.getElementById('torque').value = carro.torque;

        this.indiceEdicao = indice;
        this.alternarBotoes(true);
    }

    atualizarCarro(carro) {
        if (this.indiceEdicao !== null) {
            this.carros[this.indiceEdicao] = carro;
            this.indiceEdicao = null;
            this.alternarBotoes(false);
            this.atualizartabela();
            this.limparFormulario();
        }
    }

    atualizartabela() {
        const tabela = document.getElementById('tabela');
        tabela.innerHTML = '';

        this.carros.forEach((carro, i) => {
            const linha = document.createElement('tr');
            linha.innerHTML = `
                <td>${carro.marca}</td>
                <td>${carro.modelo}</td>
                <td>${carro.ano}</td>
                <td>${carro.potencia}</td>
                <td>${carro.torque}</td>
                <td>
                    <button onclick="carroCadastro.editarCarro(${i})" class="btn btn-warning">Editar</button>
                    <button onclick="carroCadastro.removerCarro(${i})" class="btn btn-danger">Excluir</button>
                </td>
            `;
            tabela.appendChild(linha);
        });
    }

    limparFormulario() {
        document.getElementById('carroForm').reset();
    }

    alternarBotoes(editando) {
        document.getElementById('adicionarBtn').style.display = editando ? 'none' : 'inline-block';
        document.getElementById('atualizarBtn').style.display = editando ? 'inline-block' : 'none';
    }
}

const carroCadastro = new CarroCadastro();

document.getElementById('carroForm').addEventListener('submit', function (evento) {
    evento.preventDefault();

    const marca = document.getElementById('marca').value;
    const modelo = document.getElementById('modelo').value;
    const ano = document.getElementById('ano').value;
    const potencia = document.getElementById('potencia').value;
    const torque = document.getElementById('torque').value;

    const novoCarro = new Carro(marca, modelo, ano, potencia, torque);
    carroCadastro.adicionarCarro(novoCarro);
});

document.getElementById('atualizarBtn').addEventListener('click', function () {
    const marca = document.getElementById('marca').value;
    const modelo = document.getElementById('modelo').value;
    const ano = document.getElementById('ano').value;
    const potencia = document.getElementById('potencia').value;
    const torque = document.getElementById('torque').value;

    const carroAtualizado = new Carro(marca, modelo, ano, potencia, torque);
    carroCadastro.atualizarCarro(carroAtualizado);
});
