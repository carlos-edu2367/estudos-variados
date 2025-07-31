from fastapi import APIRouter

# Criando o roteador (quem gerencia as rotas) e adicionando as rotas desse roteador 
# o prefixo auth, ou seja, quando definir uma rota ela sempre vai ter /auth antes
# ex: criei a rota /login, ela na verdade é /auth/login
# E a "tags=" é só um titulo de organização da documentação da api (deve estar em lista [])
# Para que as rotas que criarmos aqui ficarem organizadas em auth na documentação
auth_router = APIRouter(prefix="/auth", tags=["auth"])

@auth_router.get("/login/{email}/{senha}")
async def login(email: str, senha: str):

    return {"e-mail": email, "senha": senha}

# Destrinchando esta end point:
# Primeiro como decorator (@ acima da função) nós setamos que é uma rota referente ao
# Roteador, que é um endpoint do tipo get e que espera 2 variaveis (email e senha)
# e depois criamos a função, que consome desses mesmos e-mail e senha
# IMPORTANTE: devemos sempre passar o modelo de dados (schemas ou padrões)