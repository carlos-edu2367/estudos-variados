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
from apis.fastapi.basics.routes.auth_routes import auth_router
from apis.fastapi.basics.routes.order_routes import order_router

# Depois de importar os roteadores precisamos avisar a Api que eles podem ser utilizados
# ou seja, vamos incluí-los

app.include_router(auth_router)
app.include_router(order_router)