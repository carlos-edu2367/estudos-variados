from sqlalchemy import create_engine, Column, String, Integer, Boolean, Float, ForeignKey
from sqlalchemy.orm import declarative_base
from sqlalchemy_utils.types import ChoiceType # para definir valores possiveis para
# determinadas colunas (coluna tipo só pode ter admin e cliente, coisa do tipo)

# Cria a conexão com o banco de dados
db = create_engine("sqlite:///banco.db") # quando fizer deploy é só colocar a váriavel do .env aqui

# Cria a base do banco de dados
Base = declarative_base()

# Cria as classes (Tabelas) do banco de dados

# Toda tabela que for criar a base deve ser passada como argumento
class Usuario(Base):
    __tablename__ = "usuarios"  # Definindo o nome da tabela

    # Agora estamos definindo as colunas dessa tabela, (tem praticamente as mesmas coisas
    # de um sql normal)
    id = Column("id", Integer, primary_key=True, autoincrement=True)
    nome = Column("nome", String, nullable=False)
    email = Column("email", String, unique=True, nullable=False)
    senha = Column("senha", String, nullable=False)
    ativo = Column("ativo", Boolean)
    admin = Column("admin", Boolean, default=False)

    # Depois de criar as tabelas precisamos definir uma função para iniciar um usuário

    def __init__(self, nome, email, senha, ativo=True, admin=False):
        self.nome = nome
        self.email = email
        self.senha = senha
        self.ativo = ativo
        self.admin = admin
    # o Self aqui faz referência as variaveis da classe (ou seja, as colunas)



class Pedido(Base):
    __tablename__ = "pedidos"

# Estamos definindo a tupla de tuplas com as opções de status dos pedidos
# Não sei pq, mas o sqlalchemy não aceita dicionários nisso, então faz com tupla
# É uma boa prática de padronização, apesar de ser possível padronizar de outras formas
    STATUS_PEDIDOS = (
        ("PENDENTE", "PENDENTE"),
        ("CANCELADO", "CANCELADO"),
        ("FINALIZADO", "FINALIZADO")
    ) 

    id = Column("id", Integer, primary_key=True, autoincrement=True)
    status = Column("status", ChoiceType(choices=STATUS_PEDIDOS)) # PENDENTE, CANCELADO, FINALIZADO
    usuario = Column("usuario", ForeignKey("usuarios.id"))
    preco = Column("preco", Float)
    #itens = 

    def __init__(self, usuario, status="PENDENTE", preco=0):
        self.usuario = usuario
        self. status = status
        self.preco = preco


class ItemPedido(Base):
    __tablename__ = 'itens_pedido'

    id = Column("id", Integer, primary_key=True, autoincrement=True)
    quantidade = Column("quantidade", Integer)
    sabor = Column("sabor", String)
    tamanho = Column("tamanho", String)
    preco_unitario = Column("preco_unitario", Float)
    pedido = Column("pedido", ForeignKey("pedidos.id"))

    def __init__(self, quantidade, sabor, tamanho, preco_unitario, pedido):
        self.quantidade = quantidade
        self.sabor = sabor
        self.tamanho = tamanho
        self.preco_unitario = preco_unitario
        self.pedido = pedido