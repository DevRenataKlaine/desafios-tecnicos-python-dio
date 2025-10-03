# Desafios Técnicos em Python com a DIO

Este repositório contém alguns dos desafios técnicos do Bootcamp Suzano - Python Developer #2, disponível na plataforma DIO.

Os dasafios consistem em:

## Desafio 1 - Criando um Sistema Bancário com Python

Um simulador simples de sistema bancário em Python, que oferece um menu interativo para o usuário realizar operações básicas.

🔹 O que ele faz:

Menu de opções: apresenta quatro escolhas — Depositar, Sacar, Extrato e Sair.
Depósito: permite adicionar um valor positivo ao saldo e registra no extrato.
Saque: permite retirar dinheiro, mas com regras:
- Não pode sacar mais do que o saldo disponível.
- Não pode sacar acima do limite de R$ 500 por vez.
Só é permitido até 3 saques diários.
Extrato: mostra todas as movimentações realizadas (depósitos e saques) e o saldo atual.
Encerramento: quando o usuário escolhe Sair, o programa termina.

## Desafio 2 - Otimizando o Sistema Bancário com Funções Python

é uma simulação de sistema bancário mais avançado em Python, estruturado em funções para organizar melhor as operações.

🔹 O que ele faz:

Menu interativo com opções de depósito, saque, extrato, criação e listagem de contas, criação de usuários e saída.
Depósito (depositar): adiciona valor ao saldo e registra no extrato, se for válido.
Saque (sacar): permite retirar valores, respeitando: saldo disponível, limite de R$ 500 por saque, máximo de 3 saques por dia.
Extrato (exibir_extrato): mostra movimentações realizadas e saldo final.
Gerenciamento de usuários (criar_usuario e filtrar_usuario): permite cadastrar clientes com CPF, nome, data de nascimento e endereço.
Gerenciamento de contas (criar_conta e listar_contas): cria novas contas vinculadas a um usuário e exibe as contas existentes.
Função principal (main): controla o loop do programa e chama as funções de acordo com a opção escolhida pelo usuário.
