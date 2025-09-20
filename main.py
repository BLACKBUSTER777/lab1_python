#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import importlib
import sys
import pkgutil
import lab01


def list_tasks():
    """Возвращает список доступных заданий (task01..task11)."""
    return [name for _, name, _ in pkgutil.iter_modules(lab01.__path__) if name.startswith("task")]


def run_task(name: str):
    """Импортирует и выполняет solve() из модуля lab01.taskNN."""
    try:
        module = importlib.import_module(f"lab01.{name}")
    except ModuleNotFoundError:
        print(f"Модуль {name} не найден в lab01/")
        return

    if hasattr(module, "solve"):
        result = module.solve()
        print(f"{name}: {result}")
        return result
    else:
        print(f"В модуле {name} нет функции solve()")
        return None


def main():
    if len(sys.argv) < 2:
        print("Использование: python main.py <номер задания|all|list>")
        return

    arg = sys.argv[1]

    if arg == "list":
        print("Доступные задания:", ", ".join(sorted(list_tasks())))
    elif arg == "all":
        for t in sorted(list_tasks()):
            run_task(t)
    else:
        # преобразуем номер в формат taskNN
        try:
            num = int(arg)
            name = f"task{num:02d}"
            run_task(name)
        except ValueError:
            print("Номер задания должен быть числом")


if __name__ == "__main__":
    main()

