from models import db
from sqlalchemy.orm import sessionmaker


# Precisamos criar uma função que gerencie a sessão de conexão com o banco de dados
# usando yield para um "return" sem interromper o código
# e usando o finally para independente se deu erro, se deu certo, a conexão fechar

def pegar_sessao():
    try:
        Session = sessionmaker(bind=db)
        session = Session()
        yield session
    finally:
        session.close()

