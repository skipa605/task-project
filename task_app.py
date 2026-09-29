import json
import sys

DATA_FILE = "tasks.json"


def load_tasks():
    """Загружает список задач из файла."""
    try:
        with open(DATA_FILE, encoding="utf-8") as f:
            return json.load(f)
    except FileNotFoundError:
        return []


def save_tasks(tasks):
    """Сохраняет список задач в файл."""
    with open(DATA_FILE, "w", encoding="utf-8") as f:
        json.dump(tasks, f, ensure_ascii=False, indent=2)


def list_tasks():
    """Выводит все задачи."""
    tasks = load_tasks()
    if not tasks:
        print("Список задач пуст.")
        return
    for i, task in enumerate(tasks, 1):
        status = "✓" if task.get("done") else " "
        print(f"{i}. [{status}] {task['title']}")


if __name__ == "__main__":
    list_tasks()