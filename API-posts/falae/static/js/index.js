document.addEventListener('DOMContentLoaded', function() {
    const textInput = document.querySelector('.text-input');
    const listenBtn = document.querySelector('.listen-btn');
    const downloadBtn = document.querySelector('.download-btn');
    const languageSelect = document.getElementById('language');

    // Mapeamento de códigos de idioma para códigos da Web Speech API
    const speechLangMap = {
        'pt': 'pt-BR',
        'en': 'en-US',
        'es': 'es-ES',
        'fr': 'fr-FR',
        'it': 'it-IT',
        'de': 'de-DE',
        'ja': 'ja-JP'
    };

    listenBtn.addEventListener('click', function() {
        const text = textInput.value;
        const langCode = languageSelect.value;

        if (text.trim() !== '') {
            if ('speechSynthesis' in window) {
                const utterance = new SpeechSynthesisUtterance(text);
                utterance.lang = speechLangMap[langCode] || 'pt-BR';

                // Carrega as vozes disponíveis
                const voices = window.speechSynthesis.getVoices();
                if (voices.length > 0) {
                    // Tenta encontrar uma voz adequada para o idioma selecionado
                    const preferredVoice = voices.find(v => v.lang.startsWith(langCode)) ||
                                         voices.find(v => v.lang.startsWith('pt')) ||
                                         voices[0];
                    utterance.voice = preferredVoice;
                }

                speechSynthesis.speak(utterance);
            } else {
                alert('Seu navegador não suporta síntese de voz. Use a opção de download.');
            }
        } else {
            alert('Por favor, digite algum texto para ouvir.');
        }
    });

    downloadBtn.addEventListener('click', async function() {
        const text = textInput.value;
        const lang = languageSelect.value;

        if (text.trim() !== '') {
            try {
                const response = await fetch('/download', {
                    method: 'POST',
                    headers: {
                        'Content-Type': 'application/json',
                    },
                    body: JSON.stringify({
                        text: text,
                        lang: lang
                    })
                });

                if (response.ok) {
                    const blob = await response.blob();
                    const url = window.URL.createObjectURL(blob);
                    const a = document.createElement('a');
                    a.href = url;
                    a.download = `audio_${lang}.mp3`;
                    document.body.appendChild(a);
                    a.click();
                    a.remove();
                } else {
                    const error = await response.json();
                    alert(error.error || 'Erro ao gerar áudio');
                }
            } catch (error) {
                alert('Erro ao conectar com o servidor');
                console.error('Error:', error);
            }
        } else {
            alert('Por favor, digite algum texto para converter.');
        }
    });

    // Carrega as vozes quando a página é carregada
    if ('speechSynthesis' in window) {
        speechSynthesis.onvoiceschanged = function() {
            console.log('Vozes carregadas:', speechSynthesis.getVoices());
        };
        // Força o carregamento das vozes em alguns navegadores
        speechSynthesis.getVoices();
    }
});