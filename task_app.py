import json
import sys

DATA_FILE = "tasks.json"

DEFAULT_PRIORITY = "normal"
PRIORITY_ORDER = {"high": 0, "normal": 1, "low": 2}


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


def add_task(title, priority="normal"):
    """Добавляет новую задачу с приоритетом."""
    tasks = load_tasks()
    tasks.append({"title": title, "done": False, "priority": priority})
    save_tasks(tasks)
    print(f"Задача добавлена: {title} ({priority})")


def mark_done(index):
    """Отмечает задачу выполненной по номеру."""
    tasks = load_tasks()
    if 0 <= index < len(tasks):
        tasks[index]["done"] = True
        save_tasks(tasks)
        print(f"Задача {index + 1} отмечена выполненной.")
    else:
        print("Неверный номер задачи.")


def sort_by_priority(tasks):
    """Сортирует задачи по приоритету."""
    return sorted(tasks, key=lambda t: PRIORITY_ORDER.get(t.get("priority", "normal"), 1))


def list_tasks(status=None):
    """Выводит задачи, опционально фильтруя по статусу."""
    tasks = sort_by_priority(load_tasks())
    if status == "done":
        tasks = [t for t in tasks if t.get("done")]
    elif status == "open":
        tasks = [t for t in tasks if not t.get("done")]
    if not tasks:
        print("Нет задач по фильтру.")
        return
    for i, task in enumerate(tasks, 1):
        mark = "✓" if task.get("done") else " "
        print(f"{i}. [{mark}] {task['title']} ({task.get('priority', 'normal')})")


if __name__ == "__main__":
    import argparse

    parser = argparse.ArgumentParser()
    parser.add_argument("command", nargs="?", default="list",
                        choices=["list", "add", "done"])
    parser.add_argument("args", nargs="*")
    parser.add_argument("--priority", choices=["low", "normal", "high"],
                        default=DEFAULT_PRIORITY)
    parsed = parser.parse_args()

    if parsed.command == "add":
        add_task(" ".join(parsed.args), parsed.priority)
    elif parsed.command == "done" and parsed.args:
        mark_done(int(parsed.args[0]) - 1)
    elif parsed.command == "list":
        status = parsed.args[0] if parsed.args else None
        list_tasks(status)
    else:
        list_tasks()