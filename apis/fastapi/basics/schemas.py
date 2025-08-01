# Já que python é uma linguagem fraca em tipagem, nós precisamos criar manualmente
# Pois assim garantimos uma maior velocidade da Api e evitamos muitos erros
# Pra isso servem os schemas, nós vamos definir classes que serão utilizadas (como o models)
# mas obrigando o python a seguir os tipos de dados que aqui definimos
# pra isso, usamos o Pydantic com typing.

from pydantic import BaseModel
from typing import Optional

class UsuarioSchema(BaseModel):
    nome: str
    email: str
    senha: str
    ativo: Optional[bool]
    admin: Optional[bool]

    class Config:
        from_attributes = True

    # Primeiro definimos o Schema (o modelo de dados)
    # depois configuramos esse modelo de dados para ser tratado como ORM no sqlalchemy
    # por isso definimos from_attributes = True