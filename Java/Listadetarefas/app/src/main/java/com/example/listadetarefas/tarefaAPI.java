package com.example.listadetarefas;
import  java.util.List;
import retrofit2.Call;
import retrofit2.http.GET;

public interface tarefaAPI {
    @GET("/tasks")
    Call<List<tarefa>>getTarefas();
}