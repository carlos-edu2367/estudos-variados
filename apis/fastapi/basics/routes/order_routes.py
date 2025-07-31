from fastapi import APIRouter

# Criando o roteador (quem gerencia as rotas) e adicionando as rotas desse roteador 
# o prefixo order, ou seja, quando definir uma rota ela sempre vai ter /order antes
# ex: criei a rota /login, ela na verdade é /order/login
# E a "tags=" é só um titulo de organização da documentação da api
# Para que as rotas que criarmos aqui ficarem organizadas em order na documentação
order_router = APIRouter(prefix="order", tags="order")