# Desafios Técnicos em Python com a DIO

Este repositório contém alguns dos desafios técnicos do Bootcamp Suzano - Python Developer #2, disponível na plataforma DIO.

## Desafio 1 - Criando um Sistema Bancário com Python

Um simulador simples de sistema bancário em Python, que oferece um menu interativo para o usuário realizar operações básicas.

🔹 O que ele faz:

Menu de opções: apresenta quatro escolhas — Depositar, Sacar, Extrato e Sair.
Depósito: permite adicionar um valor positivo ao saldo e registra no extrato.
Saque: permite retirar dinheiro, mas com regras: não pode sacar mais do que o saldo disponível, não pode sacar acima do limite de R$ 500 por vez e só é permitido até 3 saques diários.
Extrato: mostra todas as movimentações realizadas (depósitos e saques) e o saldo atual.
Encerramento: quando o usuário escolhe Sair, o programa termina.

## Desafio 2 - Otimizando o Sistema Bancário com Funções Python

Uma simulação de sistema bancário mais avançado em Python, estruturado em funções para organizar melhor as operações.

🔹 O que ele faz:

Menu interativo com opções de depósito, saque, extrato, criação e listagem de contas, criação de usuários e saída.
Depósito (depositar): adiciona valor ao saldo e registra no extrato, se for válido.
Saque (sacar): permite retirar valores, respeitando: saldo disponível, limite de R$ 500 por saque, máximo de 3 saques por dia.
Extrato (exibir_extrato): mostra movimentações realizadas e saldo final.
Gerenciamento de usuários (criar_usuario e filtrar_usuario): permite cadastrar clientes com CPF, nome, data de nascimento e endereço.
Gerenciamento de contas (criar_conta e listar_contas): cria novas contas vinculadas a um usuário e exibe as contas existentes.
Função principal (main): controla o loop do programa e chama as funções de acordo com a opção escolhida pelo usuário.

## Desafio 3 - Modelando o Distema Bancário em POO com Python

Este código implementa um sistema bancário simples em Python utilizando Programação Orientada a Objetos (POO). Ele permite criar clientes, abrir contas correntes, realizar depósitos, saques e consultar extratos.

🔹 O que ele faz:

Este sistema é uma simulação de banco em Python, construída utilizando programação orientada a objetos. Ele permite a criação de clientes do tipo pessoa física, associando a eles uma ou mais contas bancárias, especificamente contas correntes. Cada conta possui saldo, agência, número e um histórico de transações, podendo realizar depósitos e saques. O sistema também impõe regras para saques em contas correntes, como limite máximo por operação e limite de saques por período. Transações, tanto saques quanto depósitos, são registradas automaticamente no histórico, armazenando tipo, valor e data da operação. O sistema oferece uma interface de menu interativo no console, permitindo criar clientes e contas, efetuar transações, consultar extratos e listar contas existentes. Ele ainda realiza validações de entrada do usuário e tratamento de erros para operações inválidas, garantindo que apenas operações válidas sejam executadas.

Padrões e técnicas:

- POO: herança (ContaCorrente → Conta), abstração (Transacao), encapsulamento (_saldo, _cliente).
- Type Hints: Uso extensivo de List, Optional, TypeVar para segurança de tipos.
- Factory Method: Conta.nova_conta genérica para suportar subclasses.
- Tratamento de exceções: entrada de usuário validada (ValueError, IndexError).
