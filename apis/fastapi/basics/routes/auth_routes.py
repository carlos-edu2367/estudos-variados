from fastapi import APIRouter

# Criando o roteador (quem gerencia as rotas) e adicionando as rotas desse roteador 
# o prefixo auth, ou seja, quando definir uma rota ela sempre vai ter /auth antes
# ex: criei a rota /login, ela na verdade é /auth/login
# E a "tags=" é só um titulo de organização da documentação da api
# Para que as rotas que criarmos aqui ficarem organizadas em auth na documentação
auth_router = APIRouter(prefix="auth", tags="auth")