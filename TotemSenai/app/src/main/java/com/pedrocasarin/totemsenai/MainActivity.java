package com.pedrocasarin.totemsenai;

import android.annotation.SuppressLint;
import android.graphics.SurfaceTexture;
import android.media.MediaPlayer;
import android.net.Uri;
import android.os.Bundle;
import android.view.Surface;
import android.view.TextureView;
import android.view.View;
import androidx.appcompat.app.AppCompatActivity;

public class MainActivity extends AppCompatActivity {

    private TextureView textureView;
    private MediaPlayer mediaPlayer;

    @SuppressLint("MissingInflatedId")
    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        hideSystemUI(); // modo tela cheia
        setContentView(R.layout.activity_main);

        textureView = findViewById(R.id.textureView);

        textureView.setSurfaceTextureListener(new TextureView.SurfaceTextureListener() {
            @Override
            public void onSurfaceTextureAvailable(SurfaceTexture surface, int width, int height) {
                playVideo(new Surface(surface));
            }

            @Override public void onSurfaceTextureSizeChanged(SurfaceTexture surface, int width, int height) {}
            @Override public boolean onSurfaceTextureDestroyed(SurfaceTexture surface) { return false; }
            @Override public void onSurfaceTextureUpdated(SurfaceTexture surface) {}
        });
    }

    private void playVideo(Surface surface) {
        mediaPlayer = MediaPlayer.create(this, Uri.parse("android.resource://" + getPackageName() + "/" + R.raw.fundo));
        mediaPlayer.setSurface(surface);
        mediaPlayer.setLooping(true);
        mediaPlayer.setVolume(0f, 0f); // mudo

        mediaPlayer.setOnPreparedListener(mp -> {
            // FORÇAR O STRETCH — ajusta o TextureView ao tamanho da tela (distorcendo, se necessário)
            int videoWidth = mp.getVideoWidth();
            int videoHeight = mp.getVideoHeight();

            float scaleX = (float) textureView.getWidth() / videoWidth;
            float scaleY = (float) textureView.getHeight() / videoHeight;

            // Aplica stretch (não mantém proporção!)
            textureView.setScaleX(scaleX);
            textureView.setScaleY(scaleY);

            mediaPlayer.start();
        });
    }

    private void hideSystemUI() {
        getWindow().getDecorView().setSystemUiVisibility(
                View.SYSTEM_UI_FLAG_IMMERSIVE_STICKY
                        | View.SYSTEM_UI_FLAG_FULLSCREEN
                        | View.SYSTEM_UI_FLAG_HIDE_NAVIGATION
                        | View.SYSTEM_UI_FLAG_LAYOUT_FULLSCREEN
                        | View.SYSTEM_UI_FLAG_LAYOUT_HIDE_NAVIGATION
                        | View.SYSTEM_UI_FLAG_LAYOUT_STABLE
        );
    }

    @Override
    protected void onResume() {
        super.onResume();
        hideSystemUI();
    }
}
