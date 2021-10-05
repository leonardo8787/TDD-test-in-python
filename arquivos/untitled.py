from typing import List, Union, Tuple, Dict, NewType, Callable

# Primitivos
numero: int = 10
flutuante: float = 10.5
booleano: bool = False
string: str = 'Luiz Otávio'

# Sequências
lista: list[int] = [1, 2, 3]
lista_str_int: List[Union[int, str]] = [1, 2, 3, 'Luiz']
tupla: Tuple[int, int, int, str] = (1, 2, 3, 'luiz')

# Dicionários e conjuntos
pessoa: Dict[str, Union[str, int]] = {'nome': 'Luiz Otávio', 'sobrenome': 'Miranda', 'idade': 30}
pessoa2: Dict[str, Union[str, int, List[int]]] = {'nome': 'Luis Otávio', 'sobrenome': 'Miranda', 'idade': 30, 'l': [1, 2]}

# Meu tipo
MeuDict = Dict[str, Union[str, int, List[int]]]
pessoa2: MeuDict = {'nome': 'Luis Otávio', 'sobrenome': 'Miranda', 'idade': 30, 'l': [1, 2]}

# Meu outro tipo
UserId = NewType('UserId', int)
User_id = UserId(123456789)

def executa_funcao(funcao: Callable[[], None]) -> Callable:
    return funcao

def fala_oi():
    print('Oi')

executa_funcao(fala_oi())

class Pessoa:
    def __init__(self, nome: str, sobrenome: str, idade: int) -> None:
        self.nome: str = nome
        self.sobrenome: str = sobrenome
        self.idade: int = idade

    def fala(self) -> None:
        print(f'{self.nome} {self.sobrenome} está falando...')


def interar(sequencia: Sequencia[int]):
    return [x * 2 for x in sequencia]

print(iterar([1, 2, 3]))
print(iterar((1, 2, 3)))