package com.calculodeviagem;

import android.os.Bundle;
import android.view.View;
import android.widget.Button;
import android.widget.EditText;
import android.widget.RadioButton;
import android.widget.RadioGroup;
import android.widget.TextView;
import androidx.appcompat.app.AppCompatActivity;

public class calcular extends AppCompatActivity {

    private EditText edtAutonomia, edtDistancia;
    private RadioGroup rgCombustivel;
    private Button btnCalcular;
    private TextView txtResultado;

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.calcular);

        edtAutonomia = findViewById(R.id.autonomia);
        edtDistancia = findViewById(R.id.distanciaDaViagem);
        rgCombustivel = findViewById(R.id.tipoCombustivel);
        btnCalcular = findViewById(R.id.btnCalcular);
        txtResultado = findViewById(R.id.resultado);

        btnCalcular.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View v) {
                calcularConsumo();
            }
        });
    }

    private void calcularConsumo() {
        String autonomiaStr = edtAutonomia.getText().toString();
        String distanciaStr = edtDistancia.getText().toString();

        if (autonomiaStr.isEmpty() || distanciaStr.isEmpty() || rgCombustivel.getCheckedRadioButtonId() == -1) {
            txtResultado.setText("Preencha todos os campos!");
            return;
        }

        double autonomia = Double.parseDouble(autonomiaStr);
        double distancia = Double.parseDouble(distanciaStr);

        int combustivelSelecionado = rgCombustivel.getCheckedRadioButtonId();
        String combustivel;
        float valorComb = 0;

        if (combustivelSelecionado == R.id.gasolina) {
            combustivel = "Gasolina";
            valorComb = 6.30F;
        } else if (combustivelSelecionado == R.id.diesel) {
            combustivel = "Diesel";
            valorComb = 6.50F;
        } else {
            combustivel = "Etanol";
            valorComb = 4.10F;
        }

        double litrosNecessarios = distancia / autonomia;
        double valor = litrosNecessarios * valorComb;
        txtResultado.setText(String.format("Você precisará de %.2f litros de %s.\nIsso dará R$%.2f", litrosNecessarios, combustivel, valor));

    }
}
