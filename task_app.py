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

def add_task(title):
    """Добавляет новую задачу."""
    tasks = load_tasks()
    tasks.append({"title": title, "done": False})
    save_tasks(tasks)
    print(f"Задача добавлена: {title}")

def list_tasks():
    """Выводит все задачи."""
    tasks = load_tasks()
    if not tasks:
        print("Список задач пуст.")
        return
    for i, task in enumerate(tasks, 1):
        status = "✓" if task.get("done") else " "
        print(f"{i}. [{status}] {task['title']}")

def mark_done(index):
    """Отмечает задачу выполненной по номеру."""
    tasks = load_tasks()
    if 0 <= index < len(tasks):
        tasks[index]["done"] = True
        save_tasks(tasks)
        print(f"Задача {index + 1} отмечена выполненной.")
    else:
        print("Неверный номер задачи.")

if __name__ == "__main__":
    if len(sys.argv) > 1 and sys.argv[1] == "add":
        add_task(" ".join(sys.argv[2:]))
    elif len(sys.argv) > 2 and sys.argv[1] == "done":
        mark_done(int(sys.argv[2]) - 1)
    else:
        list_tasks()