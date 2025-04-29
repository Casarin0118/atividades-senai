package com.example.buscaendereco.service;

import com.example.buscaendereco.model.logradouro;

import retrofit2.Call;
import retrofit2.http.GET;
import retrofit2.http.Path;
import retrofit2.http.Query;

public interface invertextoApi {
    @GET("/v1/cep/{numero}")
    Call<logradouro> getEndereco(
            @Path("numero") String numero,
            @Query("token") String token
    );
}
