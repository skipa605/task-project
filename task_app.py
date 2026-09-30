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

def list_tasks(status=None):
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


def sort_by_priority(tasks):
    """Сортирует задачи по приоритету."""
    return sorted(tasks, key=lambda t: PRIORITY_ORDER.get(t.get("priority", "normal"), 1))
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
    elif len(sys.argv) > 2 and sys.argv[1] == "list":
        list_tasks(sys.argv[2])
    else:
        list_tasks()



