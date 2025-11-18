import json
import os


# ============================================================
#   CLASSE PROJECT
#   Representa um projeto com nome, valor e horas
# ============================================================
class Project:
    def __init__(self, name, value, hours):
        self.name = name
        self.value = value
        self.hours = hours

    def ratio(self):
        return self.value / self.hours

    def as_dict(self):
        return {"name": self.name, "value": self.value, "hours": self.hours}

    def __str__(self):
        return f"{self.name} (Valor={self.value}, Horas={self.hours})"


# ============================================================
#   RESULTADO FINAL DE UMA SOLUÇÃO
# ============================================================
class Result:
    def __init__(self, total_value, chosen_items):
        self.total_value = total_value
        self.chosen_items = chosen_items

    def as_dict(self):
        return {"total_value": self.total_value, "chosen_items": self.chosen_items}

    def __str__(self):
        return f"Valor Total: {self.total_value} | Itens: {self.chosen_items}"


# ============================================================
#   SISTEMA DE LOG SIMPLES PARA APLICAR EM QUALQUER PARTE
# ============================================================
class Logger:
    @staticmethod
    def info(text):
        print(f"\033[96m[INFO]\033[0m {text}")

    @staticmethod
    def warn(text):
        print(f"\033[93m[ATENÇÃO]\033[0m {text}")

    @staticmethod
    def error(text):
        print(f"\033[91m[ERRO]\033[0m {text}")

    @staticmethod
    def success(text):
        print(f"\033[92m[OK]\033[0m {text}")


# ============================================================
#   CARREGADOR DE PROJETOS (via arquivo ou lista)
# ============================================================
class ProjectLoader:
    @staticmethod
    def from_list(raw_list):
        projects = []
        for item in raw_list:
            projects.append(Project(item[0], item[1], item[2]))
        return projects

    @staticmethod
    def from_json(path):
        if not os.path.exists(path):
            Logger.error("Arquivo não encontrado.")
            return []

        with open(path, "r") as f:
            data = json.load(f)

        projects = []
        for obj in data["projects"]:
            projects.append(Project(obj["name"], obj["value"], obj["hours"]))

        Logger.success("Projetos carregados via JSON.")
        return projects


# ============================================================
#   CLASSE PRINCIPAL QUE RESOLVE O KNAPSACK
# ============================================================
class KnapsackSolver:
    def __init__(self, projects, capacity):
        self.projects = projects
        self.capacity = capacity
        self.count = len(projects)

    # ========================================================
    #   FASE 1 — GREEDY
    # ========================================================
    def greedy(self):
        Logger.info("Executando método GREEDY...")

        ordered = sorted(self.projects, key=lambda p: p.ratio(), reverse=True)

        total_value = 0
        chosen = []
        used = 0

        for p in ordered:
            if used + p.hours <= self.capacity:
                used += p.hours
                total_value += p.value
                chosen.append(p.name)

        return Result(total_value, chosen)

    # ========================================================
    #   FASE 2 — RECURSIVO PURO
    # ========================================================
    def recursive(self, index=None, remaining=None):
        if index is None:
            index = self.count
        if remaining is None:
            remaining = self.capacity

        if index == 0 or remaining == 0:
            return 0

        p = self.projects[index - 1]

        if p.hours > remaining:
            return self.recursive(index - 1, remaining)

        include = p.value + self.recursive(index - 1, remaining - p.hours)
        exclude = self.recursive(index - 1, remaining)

        return max(include, exclude)

    # ========================================================
    #   FASE 3 — TOPO (MEMOIZATION)
    # ========================================================
    def memoization(self, index=None, remaining=None, memo=None):
        if index is None:
            index = self.count
        if remaining is None:
            remaining = self.capacity
        if memo is None:
            memo = {}

        key = (index, remaining)

        if key in memo:
            return memo[key]

        if index == 0 or remaining == 0:
            memo[key] = 0
            return 0

        p = self.projects[index - 1]

        if p.hours > remaining:
            memo[key] = self.memoization(index - 1, remaining, memo)
            return memo[key]

        include = p.value + self.memoization(index - 1, remaining - p.hours, memo)
        exclude = self.memoization(index - 1, remaining, memo)

        memo[key] = max(include, exclude)
        return memo[key]

    # ========================================================
    #   FASE 4 — BOTTOM-UP COM TABELA + RECONSTRUÇÃO
    # ========================================================
    def bottom_up(self):
        Logger.info("Construindo tabela da DP...")

        table = [[0 for _ in range(self.capacity + 1)] for _ in range(self.count + 1)]

        for i in range(1, self.count + 1):
            p = self.projects[i - 1]

            for c in range(1, self.capacity + 1):
                if p.hours > c:
                    table[i][c] = table[i - 1][c]
                else:
                    include = p.value + table[i - 1][c - p.hours]
                    exclude = table[i - 1][c]
                    table[i][c] = max(include, exclude)

        chosen = self.reconstruct(table)

        return Result(table[self.count][self.capacity], chosen), table

    # ========================================================
    #   RECONSTRÓI OS ITENS A PARTIR DA TABELA
    # ========================================================
    def reconstruct(self, table):
        chosen = []
        i = self.count
        c = self.capacity

        while i > 0:
            if table[i][c] != table[i - 1][c]:
                chosen.append(self.projects[i - 1].name)
                c -= self.projects[i - 1].hours
            i -= 1

        chosen.reverse()
        return chosen


# ============================================================
#   FUNÇÃO PARA MOSTRAR RESULTADOS DE FORMA BONITA
# ============================================================
def show_results(title, solver):
    print(f"\n\033[95m===== {title} =====\033[0m")

    greedy = solver.greedy()
    print("Greedy:", greedy)

    recursive_value = solver.recursive()
    print("Recursiva:", recursive_value)

    memo = solver.memoization()
    print("Memoization:", memo)

    bottom, _ = solver.bottom_up()
    print("Bottom-Up:", bottom)


# ============================================================
#   MÓDULO PRINCIPAL
# ============================================================
if __name__ == "__main__":

    Logger.info("Iniciando execução...")

    # --------------------- CASO OFICIAL FIAP ---------------------
    official_data = [
        ("A", 12, 4),
        ("B", 10, 3),
        ("C", 7, 2),
        ("D", 4, 3),
    ]
    official_projects = ProjectLoader.from_list(official_data)

    solver1 = KnapsackSolver(official_projects, 10)
    show_results("CASO OFICIAL DO ENUNCIADO", solver1)

    # ------------------ CASO ONDE O GREEDY FALHA ------------------
    failing_data = [
        ("A", 100, 5),
        ("B", 60, 3),
        ("C", 50, 3),
    ]
    failing_projects = ProjectLoader.from_list(failing_data)

    solver2 = KnapsackSolver(failing_projects, 6)
    show_results("CASO ONDE O GREEDY FALHA", solver2)

    Logger.success("Execução finalizada com sucesso!")
