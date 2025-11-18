# 🚀 GS – Dynamic Programming  
## Otimização de Portfólio de Projetos – Problema da Mochila 0/1 (FIAP)

<div align="center">

### 👨‍💻 **Integrantes**
**Rickelmyn de Souza Ruescas – RM 556055**  
**Vitor Couto Victorino – RM 554965**  
**Fabrini Soares – RM 557813**

---

### 🧠 *Algoritmos Implementados*  
Greedy • Recursivo Puro • Memoization • Bottom-Up

</div>

---

# 📘 Sobre o Projeto

Este trabalho implementa quatro abordagens clássicas para resolver o **Problema da Mochila 0/1**, aplicado ao contexto de **seleção de projetos** em uma empresa com capacidade limitada de horas.

Cada projeto possui:

- 💰 **Valor gerado**
- ⏱ **Horas necessárias**
- 🏷 **Identificação (nome)**

🎯 O objetivo é:  
> **Maximizar o valor total sem exceder a capacidade de horas.**

---

# 🧠 Abordagens Utilizadas

## 1️⃣ Greedy (Guloso)
Seleciona projetos com base na melhor razão **valor ÷ horas**.  
✔ Extremamente rápido  
✘ Não garante o melhor resultado global

---

## 2️⃣ Recursiva Pura
Explora todas as combinações possíveis.  
✔ Sempre encontra a solução ótima  
✘ Complexidade exponencial (**2ⁿ**)

---

## 3️⃣ Programação Dinâmica – Memoization (Top-Down)
Versão otimizada da recursiva, armazenando subproblemas.  
✔ Muito eficiente  
✔ Garante a solução ótima  
✔ Evita recomputações

---

## 4️⃣ Programação Dinâmica – Bottom-Up (Tabela)
Cria uma tabela de subsoluções até chegar à solução ótima final.  
✔ Excelente custo-benefício  
✔ Garante ótima solução  
✔ Permite reconstrução dos itens escolhidos

---

# 📦 Requisitos e Dependências

### ✔ Requisitos
- Python **3.8 ou superior**
- Compatível com Windows, Mac e Linux

### ✔ Dependências
Nenhuma.  
O projeto utiliza apenas bibliotecas nativas do Python.

---

# 🧪 Casos Testados

## ✅ Caso Oficial (Enunciado FIAP)

| Projeto | Valor | Horas |
|--------|-------|--------|
| A | 12 | 4 |
| B | 10 | 3 |
| C | 7  | 2 |
| D | 4  | 3 |

📌 Capacidade: **10 horas**  
🎯 Melhor solução: **29 (C, B, A)**  
✔ Todas as abordagens encontraram o valor ótimo.

---

## ❌ Caso Onde o Greedy Falha (Exigido no enunciado)

| Projeto | Valor | Horas |
|--------|-------|--------|
| A | 100 | 5 |
| B | 60  | 3 |
| C | 50  | 3 |

📌 Capacidade: **6 horas**

⚠ Greedy seleciona → **A = 100**  
🏆 Melhor solução → **B + C = 110**

> Demonstra que o Greedy não garante a solução ótima no Problema da Mochila.

---

# 📊 Análise de Complexidade

| Método | Complexidade | Ótimo Garantido | Observações |
|--------|--------------|------------------|-------------|
| Greedy | O(n log n) | ❌ | Muito rápido, mas limitado |
| Recursiva | O(2ⁿ) | ✔ | Impraticável para n grande |
| Memoization | O(n · capacidade) | ✔ | Mais eficiente que recursiva pura |
| Bottom-Up | O(n · capacidade) | ✔ | Método clássico e mais usado |

---

# 📝 Conclusão

O projeto demonstra o funcionamento completo das abordagens de Programação Dinâmica, destacando:

- Diferenças entre heurísticas e PD  
- Importância da reconstrução do caminho ideal  
- Por que o Greedy falha  
- Como DP encontra a solução ótima  
- Evolução de eficiência entre os métodos  

É uma solução robusta, completa e alinhada ao enunciado da FIAP.

---
