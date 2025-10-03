import textwrap
from abc import ABC, abstractmethod
from datetime import datetime
from typing import TypeVar, Type, List, Optional

# ========================
# CLASSES DE CLIENTE
# ========================
class Cliente:
    def __init__(self, endereco: str):
        self.endereco = endereco
        self.contas: List["Conta"] = []

    def realizar_transacao(self, conta: "Conta", transacao: "Transacao"):
        transacao.registrar(conta)

    def adicionar_conta(self, conta: "Conta"):
        self.contas.append(conta)


class PessoaFisica(Cliente):
    def __init__(self, nome: str, data_nascimento: str, cpf: str, endereco: str):
        super().__init__(endereco)
        self.nome = nome
        self.data_nascimento = data_nascimento
        self.cpf = cpf


# ========================
# CLASSES DE CONTA
# ========================
T = TypeVar("T", bound="Conta")

class Conta:
    def __init__(self, numero: int, cliente: PessoaFisica):
        self._saldo: float = 0
        self._numero: int = numero
        self._agencia: str = "0001"
        self._cliente: PessoaFisica = cliente
        self._historico: Historico = Historico()

    @classmethod
    def nova_conta(cls: Type[T], cliente: PessoaFisica, numero: int) -> T:
        return cls(numero, cliente)

    @property
    def saldo(self) -> float:
        return self._saldo

    @property
    def numero(self) -> int:
        return self._numero

    @property
    def agencia(self) -> str:
        return self._agencia

    @property
    def cliente(self) -> PessoaFisica:
        return self._cliente

    @property
    def historico(self) -> "Historico":
        return self._historico

    def sacar(self, valor: float) -> bool:
        if valor <= 0:
            print("\n@@@ Operação falhou! Valor inválido. @@@")
            return False
        if valor > self._saldo:
            print("\n@@@ Operação falhou! Saldo insuficiente. @@@")
            return False
        self._saldo -= valor
        print("\n=== Saque realizado com sucesso! ===")
        return True

    def depositar(self, valor: float) -> bool:
        if valor <= 0:
            print("\n@@@ Operação falhou! Valor inválido. @@@")
            return False
        self._saldo += valor
        print("\n=== Depósito realizado com sucesso! ===")
        return True


class ContaCorrente(Conta):
    def __init__(self, numero: int, cliente: PessoaFisica, limite: float = 500, limite_saques: int = 3):
        super().__init__(numero, cliente)
        self._limite = limite
        self._limite_saques = limite_saques

    def sacar(self, valor: float) -> bool:
        numero_saques = sum(1 for t in self.historico.transacoes if t["tipo"] == Saque.__name__)
        if valor > self._limite:
            print("\n@@@ Operação falhou! Limite de saque excedido. @@@")
            return False
        if numero_saques >= self._limite_saques:
            print("\n@@@ Operação falhou! Número máximo de saques excedido. @@@")
            return False
        return super().sacar(valor)

    def __str__(self) -> str:
        return f"Agência:\t{self.agencia}\nC/C:\t\t{self.numero}\nTitular:\t{self.cliente.nome}"

# ========================
# HISTÓRICO
# ========================
class Historico:
    def __init__(self):
        self._transacoes: List[dict] = []

    @property
    def transacoes(self) -> List[dict]:
        return self._transacoes

    def adicionar_transacao(self, transacao: "Transacao"):
        self._transacoes.append({
            "tipo": transacao.__class__.__name__,
            "valor": transacao.valor,
            "data": datetime.now().strftime("%d-%m-%Y %H:%M:%S"),
        })


# ========================
# TRANSAÇÕES
# ========================
class Transacao(ABC):
    @property
    @abstractmethod
    def valor(self) -> float:
        pass

    @abstractmethod
    def registrar(self, conta: Conta):
        pass


class Saque(Transacao):
    def __init__(self, valor: float):
        self._valor = valor

    @property
    def valor(self) -> float:
        return self._valor

    def registrar(self, conta: Conta):
        if conta.sacar(self.valor):
            conta.historico.adicionar_transacao(self)


class Deposito(Transacao):
    def __init__(self, valor: float):
        self._valor = valor

    @property
    def valor(self) -> float:
        return self._valor

    def registrar(self, conta: Conta):
        if conta.depositar(self.valor):
            conta.historico.adicionar_transacao(self)


# ========================
# FUNÇÕES AUXILIARES
# ========================
def menu() -> str:
    menu_text = """
    ================ MENU ================
    [d] Depositar
    [s] Sacar
    [e] Extrato
    [nc] Nova conta
    [lc] Listar contas
    [nu] Novo cliente
    [q] Sair
    => """
    return input(textwrap.dedent(menu_text))


def filtrar_cliente(cpf: str, clientes: List[PessoaFisica]) -> Optional[PessoaFisica]:
    return next((cliente for cliente in clientes if cliente.cpf == cpf), None)


def recuperar_conta_cliente(cliente: Cliente) -> Optional[Conta]:
    if not cliente.contas:
        print("\n@@@ Cliente não possui conta! @@@")
        return None
    if len(cliente.contas) > 1:
        print("\nCliente possui mais de uma conta. Escolha:")
        for i, conta in enumerate(cliente.contas, start=1):
            print(f"[{i}] Conta {conta.numero} - Agência {conta.agencia}")
        try:
            escolha = int(input("Selecione: "))
            return cliente.contas[escolha - 1]
        except (ValueError, IndexError):
            print("\n@@@ Seleção inválida! @@@")
            return None
    return cliente.contas[0]


# ========================
# OPERAÇÕES
# ========================
def depositar(clientes: List[PessoaFisica]):
    cpf = input("CPF do cliente: ")
    cliente = filtrar_cliente(cpf, clientes)
    if not cliente:
        print("\n@@@ Cliente não encontrado! @@@")
        return
    try:
        valor = float(input("Valor do depósito: "))
    except ValueError:
        print("\n@@@ Valor inválido! @@@")
        return
    conta = recuperar_conta_cliente(cliente)
    if conta:
        cliente.realizar_transacao(conta, Deposito(valor))


def sacar(clientes: List[PessoaFisica]):
    cpf = input("CPF do cliente: ")
    cliente = filtrar_cliente(cpf, clientes)
    if not cliente:
        print("\n@@@ Cliente não encontrado! @@@")
        return
    try:
        valor = float(input("Valor do saque: "))
    except ValueError:
        print("\n@@@ Valor inválido! @@@")
        return
    conta = recuperar_conta_cliente(cliente)
    if conta:
        cliente.realizar_transacao(conta, Saque(valor))


def exibir_extrato(clientes: List[PessoaFisica]):
    cpf = input("CPF do cliente: ")
    cliente = filtrar_cliente(cpf, clientes)
    if not cliente:
        print("\n@@@ Cliente não encontrado! @@@")
        return
    conta = recuperar_conta_cliente(cliente)
    if not conta:
        return
    print("\n================ EXTRATO ================")
    if not conta.historico.transacoes:
        print("Não foram realizadas movimentações.")
    else:
        for t in conta.historico.transacoes:
            print(f"{t['tipo']}: R$ {t['valor']:.2f} - {t['data']}")
    print(f"\nSaldo atual: R$ {conta.saldo:.2f}")
    print("===========================================")


def criar_cliente(clientes: List[PessoaFisica]):
    cpf = input("CPF (somente números): ")
    if filtrar_cliente(cpf, clientes):
        print("\n@@@ Já existe cliente com esse CPF! @@@")
        return
    nome = input("Nome completo: ")
    data_nascimento = input("Data de nascimento (dd-mm-aaaa): ")
    endereco = input("Endereço (logradouro, nro - bairro - cidade/sigla estado): ")
    clientes.append(PessoaFisica(nome, data_nascimento, cpf, endereco))
    print("\n=== Cliente criado com sucesso! ===")


def criar_conta(numero_conta: int, clientes: List[PessoaFisica], contas: List[ContaCorrente]):
    cpf = input("CPF do cliente: ")
    cliente = filtrar_cliente(cpf, clientes)
    if not cliente:
        print("\n@@@ Cliente não encontrado! @@@")
        return
    conta = ContaCorrente.nova_conta(cliente, numero_conta)
    contas.append(conta)
    cliente.adicionar_conta(conta)
    print("\n=== Conta criada com sucesso! ===")


def listar_contas(contas: List[ContaCorrente]):
    for conta in contas:
        print("=" * 40)
        print(conta)


# ========================
# MAIN LOOP
# ========================
def main():
    clientes: List[PessoaFisica] = []
    contas: List[ContaCorrente] = []

    while True:
        opcao = menu()
        match opcao:
            case "d": depositar(clientes)
            case "s": sacar(clientes)
            case "e": exibir_extrato(clientes)
            case "nu": criar_cliente(clientes)
            case "nc": criar_conta(len(contas) + 1, clientes, contas)
            case "lc": listar_contas(contas)
            case "q": break
            case _: print("\n@@@ Opção inválida, tente novamente. @@@")

if __name__ == "__main__":
    main()
