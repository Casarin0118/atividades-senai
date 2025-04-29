package com.example.cep.service;

import com.example.cep.model.Logradouro;
import retrofit2.Call;
import retrofit2.http.GET;
import retrofit2.http.Path;
import retrofit2.http.Query;

public interface InvertextoApi {
    @GET("v1/cep/{numero}")
    static // Corrigido endpoint
    Call<Logradouro> getEndereco(
            @Path("numero") String numero,
            @Query("token") String token
    ) {
        return null;
    }
}
