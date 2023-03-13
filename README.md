---
title: Flask
description: A popular minimal server framework for Python
tags:
  - python
  - flask
---

# REST API que criptografa e decifra mensagens

## Rotas disponíveis

#### `POST: /enigma/` 

Criptografa sua mensagem.

A string deve ser passada como valor de um objeto com chave "msg".

Exemplo:
```
{
  msg: "mensagem criptogradfada"
}
```

#### `GET: /denigma/<mensagem>/` 

Decifra sua mensagem.

A string deve ser passada como parâmetro.

Exemplo:
```
/denigma/asldbcahnsecasec/
```


## Para rodar localmente:

Digite os seguintes comandos no terminal:
```
python3 -m venv env
pip install -r requirements.txt
flask run
```

## URL do projeto no Railway:

https://enigma-sigma.up.railway.app/