package com.example.listadetarefas;

import com.google.gson.annotations.SerializedName;

public class tarefa {
    @SerializedName("title")
    private String titulo;
    @SerializedName("description")
    private String descricao;
    @SerializedName("done")
    private boolean finalizada;

    public tarefa(String titulo, String descricao, boolean finalizada){
        this.titulo = titulo;
        this.descricao = descricao;
        this.finalizada = finalizada;
    }

    public String getDescricao() {
        return descricao;
    }

    public boolean isFinalizada() {
        return finalizada;
    }

    public String getTitulo() {
        return titulo;
    }
}