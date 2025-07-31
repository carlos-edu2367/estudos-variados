from fastapi import APIRouter
#criando um dicionario com dados de teste
pedidos = {
        1: {
            "itens": [1,4,8],
            "valor": 49.50,
            "cliente": 2
        },
        2: {
            "itens": [1,2,5],
            "valor": 30.25,
            "cliente": 1
        },
        3: {
            "itens": [2,2,9],
            "valor": 16.50,
            "cliente": 3
        },
        4: {
            "itens": [1,4,8],
            "valor": 49.50,
            "cliente": 1
        }
    }

# Criando o roteador (quem gerencia as rotas) e adicionando as rotas desse roteador 
# o prefixo order, ou seja, quando definir uma rota ela sempre vai ter /order antes
# ex: criei a rota /login, ela na verdade é /order/login
# E a "tags=" é só um titulo de organização da documentação da api (que deve estar em lista [])
# Para que as rotas que criarmos aqui ficarem organizadas em order na documentação
order_router = APIRouter(prefix="/order", tags=["order"])

@order_router.get("/")
async def listar_pedidos():
    return pedidos

@order_router.get("/especifico/{id_pedido}")
async def listar_pedido_especifico(id_pedido: int):
    """ Essa rota retorna as informações de um pedido em específico """
    if id_pedido in pedidos:
        return pedidos[id_pedido]
    else:
        return {"ERRO": "Cliente não encontrado"}