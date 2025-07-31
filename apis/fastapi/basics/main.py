from fastapi import FastAPI

app = FastAPI()
# para rodar o código insira no terminal:
# python -m uvicorn apis.fastapi.basics.main:app --reload (o caminho:app e o --reload)

# endpoint:
# /nomedarota

# Rest Apis:
""" GET - Pegar uma informação
    Post - Enviar uma informação
    Put/Patch - Editar uma informação
    Delete - Deletar uma informação """

# a maioria das REST Apis não usam put nem delete, muitas englobam essas
# funcionalidades no Post


# Importando os roteadores das rotas (lembrar de importar depois da inicialização do app 
# (app = FastAPI())
from routes.auth_routes import auth_router
from routes.order_routes import order_router