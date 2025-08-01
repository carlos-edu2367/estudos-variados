from fastapi import APIRouter, Depends, HTTPException
from dependecies import pegar_sessao
from models import Usuario
from main import bcrypt_context
from schemas import UsuarioSchema
from sqlalchemy.orm import Session




# Criando o roteador (quem gerencia as rotas) e adicionando as rotas desse roteador 
# o prefixo auth, ou seja, quando definir uma rota ela sempre vai ter /auth antes
# ex: criei a rota /login, ela na verdade é /auth/login
# E a "tags=" é só um titulo de organização da documentação da api (deve estar em lista [])
# Para que as rotas que criarmos aqui ficarem organizadas em auth na documentação
auth_router = APIRouter(prefix="/auth", tags=["auth"])

# Destrinchando esta end point:
# Primeiro como decorator (@ acima da função) nós setamos que é uma rota referente ao
# Roteador, que é um endpoint do tipo post e que espera 3 variaveis (nome, e-mail e senha)
# e depois criamos a função, que consome desses mesmos nome, e-mail e senha
# IMPORTANTE: devemos sempre passar o modelo de dados (schemas ou padrões)

@auth_router.post("/cadastro")
async def cadastro( usuario_schema: UsuarioSchema, session: Session = Depends(pegar_sessao) ):
    """
    Esta rota espera receber as informações do usuário para realizar o cadastro

    Possiveis erros: 
    400 - E-mail já existe no banco de dados
    """
    usuario = session.query(Usuario).filter(Usuario.email == usuario_schema.email).first()
    if usuario:
        # ja existe um usuario cadastrado com esse e-mail
        return HTTPException(status_code=400, detail="E-mail já cadastrado")
    
        # utilizamos o HTTPException para enviar um status de erro para api
        # ou seja, caso algo de errado enviamos um status com codigo e detalhes do erro
        # Erros geralmente vão ser 400 ou 401
    else:
        senha_criptografada = bcrypt_context.hash(usuario_schema.senha)
        novoUsuario = Usuario(usuario_schema.nome, usuario_schema.email, senha_criptografada, usuario_schema.ativo, usuario_schema.admin) # deve ser na ordem do init
        session.add(novoUsuario)
        session.commit()
        return {"mensagem": f"Cadastro realizado {usuario_schema.email}"}

