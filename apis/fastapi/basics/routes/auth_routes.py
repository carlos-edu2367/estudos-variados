from fastapi import APIRouter, Depends, HTTPException
from dependecies import pegar_sessao
from models import Usuario
from main import bcrypt_context
from schemas import UsuarioSchema, LoginSchema
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
        raise HTTPException(status_code=400, detail="E-mail já cadastrado") 
        # raise é pra retornar erros
    
        # utilizamos o HTTPException para enviar um status de erro para api
        # ou seja, caso algo de errado enviamos um status com codigo e detalhes do erro
        # Erros geralmente vão ser 400 ou 401
    else:
        senha_criptografada = bcrypt_context.hash(usuario_schema.senha)
        novoUsuario = Usuario(usuario_schema.nome, usuario_schema.email, senha_criptografada, usuario_schema.ativo, usuario_schema.admin) # deve ser na ordem do init
        session.add(novoUsuario)
        session.commit()
        return {"mensagem": f"Cadastro realizado {usuario_schema.email}"}

# Com isso o cadastro está finalizado de forma segura, vou explicar o que foi feito em etapas:
# 1- decorator com o roteador e o caminho da rota
# 2- Definimos uma função assincrona de cadastro (função inteligente, a mágica do fastapi)
    # uma função assíncrona faz o seguinte: 
    # se enviarem 100 requisições para a api ela vai fazer quase que todas ao mesmo tempo
    # usando o espaço de tempo de processamento de uma para iniciar outra
    # EX: um endpoint precisa de uma api externa, em uma api com flask ou django
    # todas as outras requisições ficariam em "espera" até essa retornar um resultado
    # mas como o FASTApI é assincrono ele durante a espera realiza os outros
    # assim nunca travando o servidor
# 3- Definimos que a função espera receber uma classe que siga as regras do schema criado
# 4- definimos a sessão dependente da sessão com fechamento automático em dependencies
# 5- Fazemos uma query na classe usuarios, procurando se algum usuário já utiliza esse e-mail
    # Se já existe
        # Retorna um erro usando HTTPException, erro 400 com os detalhes
    # Se não existe
        # Iniciamos a criptografia da senha usando bcrypt
        # instanciamos um novo usuario com as informações fornecidas
        # damos um session.add para adicionar o usuario instanciado
        # retornamos uma mensagem de sucesso (por padrão acompanhada do cod 200)

# Agora precisamos criar a função de criar os tokens jwt

def criar_token(id_usuario):
    return f"klsd989w23eydsqjd8e37und{id_usuario}"
# vamos desenvolver essa função da forma certa logo



# Agora vamos desenvolver o login
@auth_router.post("/login")
async def login(login_schema: LoginSchema, session: Session = Depends(pegar_sessao)):
    """
    Essa rota é responsável por gerenciar o login do usuário, Retorna um token JWT

    Erros: 401 - Não autorizado, 400 - E-mail não cadastrado
    """
    # pegando usuario pelo e-mail
    usuario = session.query(Usuario).filter(Usuario.email == login_schema.email).first()

    # Verificando se algum usuario foi localizado
    if usuario:
        # Existe usuario com esse e-mail

        # Verificando se a senha está correta
        senha_correta = bcrypt_context.verify(login_schema.senha, usuario.senha)

        if senha_correta:
            # Senha correta
            return {
                "acess_token": criar_token(usuario.id),
                "toker_type": "Bearer"
            }
        
        else:
            #senha incorreta
            raise HTTPException(status_code=400, detail="Não autorizado")
    else:
        # Não existe um usuário com esse e-mail
        raise HTTPException(status_code=400, detail="Usuário não existe")
