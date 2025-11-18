<div align="center">

# 🚀 GS – Dynamic Programming  
## **Otimização de Portfólio de Projetos – Mochila 0/1 (FIAP)**  

### 👨‍💻 Integrantes  
**Rickelmyn de Souza Ruescas – RM 556055**  
**Vitor Couto Victorino – RM 554965**  
**Fabrini Soares – RM 557813**  

---

### 🧠 Algoritmos Implementados  
Greedy • Recursivo Puro • Memoization • Bottom-Up  

</div>

---

# 📘 **Sobre o Projeto**

Este trabalho implementa quatro abordagens clássicas para resolver o **Problema da Mochila 0/1**, aplicadas ao contexto de seleção de projetos em uma empresa.

Cada projeto possui:
- **Valor gerado**
- **Horas necessárias**
- **Nome identificador**

O objetivo é **maximizar o valor total sem ultrapassar a capacidade de horas disponível**.

---

# 🧠 **Abordagens Utilizadas**

## 1️⃣ Greedy (Guloso)
Escolhe projetos pela melhor razão **valor ÷ horas**.  
✔ Muito rápido  
✘ *Não garante a solução ótima*

---

## 2️⃣ Recursiva Pura
Explora todas as possibilidades.  
✔ Garante o ótimo  
✘ *Exponencialmente lenta*

---

## 3️⃣ Programação Dinâmica – Memoization (Top-Down)
Variante da recursiva que armazena subproblemas resolvidos.  
✔ Muito mais eficiente  
✔ Garante o ótimo

---

## 4️⃣ Programação Dinâmica – Bottom-Up (Tabela)
Constrói uma tabela com todas as soluções parciais.  
✔ Melhor equilíbrio entre velocidade e eficiência  
✔ Permite reconstruir os itens escolhidos

---

# 🧪 **Casos Testados**

---

## ✅ **Caso Oficial (Enunciado FIAP)**

| Projeto | Valor | Horas |
|--------|-------|--------|
| A | 12 | 4 |
| B | 10 | 3 |
| C | 7  | 2 |
| D | 4  | 3 |

**Capacidade:** 10 horas  
🎯 **Resultado ótimo: 29 (C, B, A)**

✔ Todas as abordagens encontram o mesmo valor.

---

## ❌ **Caso Onde o Greedy Falha**  
*(Obrigatório segundo o enunciado)*

| Projeto | Valor | Horas |
|--------|-------|--------|
| A | 100 | 5 |
| B | 60  | 3 |
| C | 50  | 3 |

**Capacidade:** 6 horas  

⚠ Greedy escolhe → **A (100)**  
🏆 Solução ótima → **B + C = 110**

Este cenário evidencia um dos pontos mais importantes da GS:  
> *Nem sempre o método guloso encontra a melhor solução.*

---

# 🖥 **Como Executar**

Execute no terminal:
```bash
python LaborFuture.py

