"""
Exercício - Lista de tarefas com desfazer e refazer
todo = [] -> lista de tarefas
todo = ['fazer café'] -> adicionar fazer café
todo = ['fazer café', 'caminhar'] -> adicionar caminhar
desfazer = ['fazer café'] -> refazer ['caminhar']
desfazer = [] -> refazer ['caminhar', 'fazer café']
refazer = todo ['fazer café']
refazer = todo ['fazer café', 'caminhar']

Etapa 2:
trabalhar essa lista de tarefas com um arquivo JSON
"""

import os
from pathlib import Path
import json


PATH_FILE = Path(__file__).parent / "to-do-list.json"


# JSON Manipulation Functions
def write_file(to_do):
    with open(PATH_FILE, 'w', encoding="utf-8") as f:
        json.dump(to_do, f, ensure_ascii=False, indent=4)

def read_file():
    to_do = []
    try:
        with open(PATH_FILE, 'r', encoding="utf-8") as f:
            return json.load(f)
    except FileNotFoundError:
        print("Arquivo não encontrado. Criando lista vazia.")
        write_file(to_do)
    return to_do


def list_tasks(to_do):
    print("\nTasks:")
    for i, task in enumerate(to_do):
        print(f"task {i+1}: {task}")
    print()


to_do = read_file()
tasks_removed = []


while True:
    write_file(to_do)

    print("Menu: \n- list\n- remake\n- undo\n- Exit\n")
    command = (input("Digite um comando ou tarefa: ")).strip()

    if command.lower() == "exit":
        break

    match command.lower():
        case "list":
            list_tasks(to_do)
        
        case "remake":
            if tasks_removed:
                to_do.append(tasks_removed.pop())
                list_tasks(to_do)
            else:
                print("Nothing to remake")

        case "undo":
            if to_do:
                task_exclude = to_do.pop()
                tasks_removed.append(task_exclude)
                list_tasks(to_do)
            else: 
                print("Nothing to undo")

        case "clear":
            os.system("cls")
            continue

        case _:
            to_do.append(command)
            tasks_removed.clear()
            list_tasks(to_do)
            continue

