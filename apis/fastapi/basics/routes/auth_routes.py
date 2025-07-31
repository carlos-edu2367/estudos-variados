from fastapi import APIRouter, Depends
from dependecies import pegar_sessao
from models import Usuario



# Criando o roteador (quem gerencia as rotas) e adicionando as rotas desse roteador 
# o prefixo auth, ou seja, quando definir uma rota ela sempre vai ter /auth antes
# ex: criei a rota /login, ela na verdade é /auth/login
# E a "tags=" é só um titulo de organização da documentação da api (deve estar em lista [])
# Para que as rotas que criarmos aqui ficarem organizadas em auth na documentação
auth_router = APIRouter(prefix="/auth", tags=["auth"])

@auth_router.get("/login/{email}/{senha}")
async def login(email: str, senha: str, session = Depends(pegar_sessao)):
    resposta = session.query(Usuario).filter(Usuario.email == email).first()
    if resposta:
        if senha == resposta.senha:
            return {"id": resposta.id}
        else:
            return {"erro": "Senha incorreta"}
    else:
        return {"mensagem": "email não encontrado"}

# Destrinchando esta end point:
# Primeiro como decorator (@ acima da função) nós setamos que é uma rota referente ao
# Roteador, que é um endpoint do tipo get e que espera 2 variaveis (email e senha)
# e depois criamos a função, que consome desses mesmos e-mail e senha
# IMPORTANTE: devemos sempre passar o modelo de dados (schemas ou padrões)

@auth_router.post("/cadastro")
async def cadastro( email:str, senha:str, nome:str, session = Depends(pegar_sessao) ):
    """
    Esta rota espera receber as informações do usuário para realizar o cadastro
    """
    usuario = session.query(Usuario).filter(Usuario.email == email).first()
    if usuario:
        # ja existe um usuario cadastrado com esse e-mail
        return {"mensagem": "E-mail já cadastrado"}
    else:
        novoUsuario = Usuario(nome, email, senha) # deve ser na ordem do init
        session.add(novoUsuario)
        session.commit()
        return {"mensagem": "Cadastro realizado"}

