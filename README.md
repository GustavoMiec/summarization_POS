# 📄 Resumidor Automático de Documentos DOCX com IA

Este projeto é um script em **Python** que lê um arquivo `.docx`, gera
um **resumo automático usando Inteligência Artificial** (Hugging Face
Transformers) e salva o resultado em um arquivo `.txt`.

## 🚀 Funcionalidades

-   Leitura de arquivos `.docx`
-   Geração de resumo automático com IA
-   Salvamento do resumo em arquivo `.txt`

## 🛠️ Tecnologias

-   Python
-   python-docx
-   transformers (Hugging Face)
-   torch

## 📦 Instalação

``` bash
pip install python-docx transformers torch
```

## ▶️ Uso

1.  Coloque o arquivo `documento.docx` na pasta do projeto\
2.  Execute:

``` bash
python main.py
```

3.  O resumo será salvo em `resumo.txt`

## 📌 Observações

-   Textos longos podem precisar ser divididos
-   O primeiro uso baixa o modelo automaticamente
