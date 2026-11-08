# 🎂 Parabéns Pedro Coelho

Página de aniversário (tema Lidl, ESJA, Mercedes e dívidas por pagar), partilhada por um link público do Cloudflare que aponta para o teu PC.

## Estrutura

```
pedro/
├── index.html           ← a página toda (HTML + CSS + JS)
├── img/                 ← turma.jpeg, nos.jpeg (e teste.jpeg, opcional)
├── audio/               ← musica.mp3 (opcional)
├── docs/                ← notas (briefing e rascunhos)
│   ├── info.md          ← o briefing original com as ideias e memes
│   └── final_text.md    ← rascunho original da carta final
├── serve.py             ← servidor local + túnel Cloudflare
├── .env/                ← ambiente Python (uv), ignorado pelo git
└── .gitignore
```

As fotos só existem em `img/`. Não há cópias noutro sítio.

## Requisitos

- [uv](https://docs.astral.sh/uv/) instalado
- Ligação à internet (para o túnel e para as fontes da página)

## Primeira vez (só se a pasta `.env` não existir)

```powershell
uv venv .env
uv pip install --python .env pycloudflared
```

## Executar

Na pasta `pedro`, num terminal (PowerShell):

```powershell
.env\Scripts\python serve.py
```

Aparece algo assim:

```
Local:  http://localhost:8080
Público: https://algumas-palavras-aleatorias.trycloudflare.com
```

- **Local**: para veres no teu PC.
- **Público**: o link para mandares ao Pedro (funciona em qualquer telemóvel ou PC).

Para parar, carrega em `Ctrl + C`.

Para usar outra porta (por exemplo, se a 8080 estiver ocupada):

```powershell
.env\Scripts\python serve.py 8090
```

## Importante

- **O link só funciona enquanto o `serve.py` estiver a correr** e o PC estiver ligado e com internet. Se fechares o terminal, o Pedro deixa de conseguir abrir a página.
- **O link muda sempre que reinicias o `serve.py`.** Manda o link novo depois de reiniciar.
- No primeiro arranque, o `pycloudflared` descarrega o `cloudflared` para dentro da `.env`. Pode demorar uns segundos.
- O `serve.py` serve a raiz do repositório (o mesmo que o GitHub Pages publica).
- Podes editar o `index.html` com o servidor a correr. Basta fazer refresh no browser.

## Personalizar

- **Música**: por defeito toca um jingle original estilo anúncio de supermercado, gerado no browser. Para usares outra música, grava-a como `audio/musica.mp3` e a página passa a tocar esse ficheiro em loop. O botão 🎵 liga e desliga a música; o 🔊 corta todo o som.
- **Foto do teste de Português verdadeiro**: grava-a como `img/teste.jpeg`. Aparece sozinha no separador "Português". Se não existir, a secção esconde-se.
- **Texto da carta final**: procura `id="letter"` em `index.html`.
- **Formas de pagamento (terminal da caixa)**: em `index.html`, procura `const PAY = {` e preenche os teus dados:
  ```js
  const PAY = {
    mbway: '912345678',
    ibanTitular: 'Nome', iban: 'PT50 ...',
    revolut: 'utilizador',   // sem @
    paypal: 'utilizador'     // de paypal.me/utilizador
  };
  ```

  Métodos com valor vazio não aparecem. Os métodos a gozar (dinheiro vivo, contactless, prestações, gomas, Mercedes) aparecem sempre.
- **Intro**: a primeira visita mostra a cena nocturna do Lidl (cerca de 13 segundos). Há um botão "Saltar intro" no canto superior direito.

## Dicas para o Pedro

- Entrar na loja ativa o som. Há um botão 🔊/🔇 no canto inferior direito.
- Quase tudo é clicável: o Mercedes do topo, os separadores dos processos, os carros da autoestrada, o Rush Team, os talões, o terminal de pagamento, o exame de código e o envelope no fim.
