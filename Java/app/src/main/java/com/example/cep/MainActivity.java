package com.example.cep;

import android.os.Bundle;
import android.widget.Button;
import android.widget.EditText;
import android.widget.TextView;
import android.widget.Toast;

import androidx.activity.EdgeToEdge;
import androidx.annotation.NonNull;
import androidx.appcompat.app.AppCompatActivity;
import androidx.core.graphics.Insets;
import androidx.core.view.ViewCompat;
import androidx.core.view.WindowInsetsCompat;

import com.example.cep.model.Logradouro;
import com.example.cep.service.InvertextoApi;

import retrofit2.Call;
import retrofit2.Callback;
import retrofit2.Response;
import retrofit2.Retrofit;
import retrofit2.converter.gson.GsonConverterFactory;

public class MainActivity extends AppCompatActivity {

    private TextView tvInformacoes; // TextView para exibir os dados
    private EditText edtCep; // Campo de entrada do CEP

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        EdgeToEdge.enable(this);
        setContentView(R.layout.activity_main);

        // Inicializando os componentes da interface
        tvInformacoes = findViewById(R.id.tvInformacoes);
        edtCep = findViewById(R.id.edtCep);
        // Botão para consultar o CEP
        Button btnBuscar = findViewById(R.id.btnBuscar);

        // Ajuste para as bordas do sistema
        ViewCompat.setOnApplyWindowInsetsListener(findViewById(R.id.main), (v, insets) -> {
            Insets systemBars = insets.getInsets(WindowInsetsCompat.Type.systemBars());
            v.setPadding(systemBars.left, systemBars.top, systemBars.right, systemBars.bottom);
            return insets;
        });

        // Configurar ação do botão
        btnBuscar.setOnClickListener(v -> {
            String cep = edtCep.getText().toString();
            if (!cep.isEmpty()) {
                consultar(cep);
            } else {
                Toast.makeText(this, "Digite um CEP válido", Toast.LENGTH_SHORT).show();
            }
        });
    }

    private void consultar(String numeroCep) {
        Retrofit retrofit = new Retrofit.Builder()
                .baseUrl(Constantes.url)
                .addConverterFactory(GsonConverterFactory.create())
                .build();

        InvertextoApi invertextoApi = retrofit.create(InvertextoApi.class);

        Call<Logradouro> call = InvertextoApi.getEndereco(numeroCep, Constantes.TOKEN);

        assert call != null;
        call.enqueue(new Callback<Logradouro>() {
            @Override
            public void onResponse(@NonNull Call<Logradouro> call, @NonNull Response<Logradouro> response) {
                if (response.isSuccessful() && response.body() != null) {
                    Logradouro logradouro = response.body();
                    tvInformacoes.setText(logradouro.toString());
                } else {
                    Toast.makeText(MainActivity.this, "Erro ao converter resposta da API", Toast.LENGTH_LONG).show();
                }
            }

            @Override
            public void onFailure(@NonNull Call<Logradouro> call, @NonNull Throwable throwable) {
                Toast.makeText(MainActivity.this, "Erro ao realizar consulta na API", Toast.LENGTH_LONG).show();
            }
        });
    }
}
