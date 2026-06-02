# 🍽️ Cardápio Inteligente

Sistema desenvolvido em Python para recomendar pratos personalizados com base nas preferências alimentares do cliente. O programa realiza sugestões inteligentes, permite múltiplos pedidos, calcula descontos conforme a forma de pagamento e gera um cupom fiscal ao final da compra.

---

## 📖 Sobre o Projeto

O objetivo deste projeto é simular o atendimento de um restaurante de forma automatizada, utilizando conceitos fundamentais de lógica de programação.

Durante a execução, o sistema identifica o perfil do cliente através de perguntas simples e recomenda pratos adequados às suas preferências alimentares.

---

## 🚀 Funcionalidades

- Cadastro do nome do cliente
- Identificação de cliente vegetariano
- Identificação de cliente que faz dieta
- Recomendação personalizada de pratos
- Escolha entre diferentes opções de refeições
- Possibilidade de adicionar mais pratos ao pedido
- Controle do valor total da compra
- Aplicação automática de descontos
- Geração de cupom fiscal

---

## 🥗 Regras de Recomendação

### Vegetariano

| Opção | Prato | Valor |
|---------|---------|---------|
| 1 | Risoto de Cogumelo Trufado | R$ 44,90 |
| 2 | Lasanha de Berinjela | R$ 39,90 |

---

### Faz Dieta

| Opção | Prato | Valor |
|---------|---------|---------|
| 1 | Filé de Frango Grelhado com Legumes | R$ 38,90 |
| 2 | Salmão ao Limão Siciliano | R$ 64,90 |

---

### Não é Vegetariano e Não Faz Dieta

| Opção | Prato | Valor |
|---------|---------|---------|
| 1 | Medalhão de Mignon ao Molho Madeira | R$ 62,90 |
| 2 | Fettuccine Alfredo com Filé Mignon | R$ 54,90 |

---

### Vegetariano e Faz Dieta

| Opção | Prato | Valor |
|---------|---------|---------|
| 1 | Bowl Fit Mediterrâneo | R$ 32,90 |
| 2 | Salada Proteica de Quinoa | R$ 34,90 |

---

## 💳 Formas de Pagamento

| Método | Desconto |
|----------|----------|
| Dinheiro | 5% |
| Cartão | Sem desconto |
| Pix | 10% |

---

## 🛠️ Tecnologias Utilizadas

<div align="left">

<img src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/python/python-original.svg" width="60"/>

</div>

- Python 3
- Estruturas Condicionais (`if`, `elif`, `else`)
- Estruturas de Repetição (`while`)
- Listas
- Variáveis Acumuladoras
- Entrada e Saída de Dados

---

## 📂 Estrutura do Projeto

```text
📦 Cardapio-Inteligente
 ┣ 📜 cardapio.py
 ┣ 📜 README.md
 ┗ 📂 assets
```

---

## ▶️ Como Executar

Clone o repositório:

```bash
git clone https://github.com/seu-usuario/cardapio-inteligente.git
```

Acesse a pasta do projeto:

```bash
cd cardapio-inteligente
```

Execute o programa:

```bash
python cardapio.py
```

---

## 💻 Exemplo de Execução

```text
===== CARDÁPIO INTELIGENTE =====

Digite seu nome: Bárbara

Você é vegetariano? (sim/nao): sim
Você faz dieta? (sim/nao): nao

Pratos recomendados:

1 - Risoto de Cogumelo Trufado
2 - Lasanha de Berinjela

Escolha um prato: 1

Risoto de Cogumelo Trufado adicionado ao pedido!

Deseja pedir mais algum prato? (sim/nao): nao

===== PAGAMENTO =====

1 - Dinheiro
2 - Cartão
3 - Pix

Escolha a forma de pagamento: 3

TOTAL A PAGAR: R$40,41
```

---

## 🎓 Conceitos Trabalhados

Este projeto foi desenvolvido para praticar:

- Lógica de Programação
- Tomada de decisão
- Estruturas condicionais
- Estruturas de repetição
- Manipulação de listas
- Acumuladores
- Organização de código
- Simulação de sistemas reais

---

## 📈 Possíveis Melhorias Futuras

- Interface gráfica com Tkinter
- Integração com banco de dados
- Sistema de login para clientes
- Histórico de pedidos
- Programa de fidelidade
- Exportação do cupom em PDF
- Cardápio dinâmico carregado por arquivo JSON

---

## 👩‍💻 Desenvolvedora

### Bárbara P. Sherveninas

Estudante de Desenvolvimento de Sistemas com foco em:

- Python
- Inteligência Artificial
- Automações com n8n
- APIs
- Desenvolvimento de Software


---



⭐ Se este projeto foi interessante para você, considere deixar uma estrela no repositório!
