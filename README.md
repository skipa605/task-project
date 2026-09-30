# Task Project

Приложение для учёта задач.

## Запуск

python task_app.py

## Формат данных

Файл tasks.json — массив объектов:
{ "title": "строка", "done": true/false }

## Команды

- python task_app.py — показать все задачи
- python task_app.py add "текст" — добавить задачу
- python task_app.py done N — отметить задачу N выполненной
- python task_app.py list open — показать открытые
- python task_app.py list done — показать выполненные

## Приоритеты

- high — высокий
- normal — обычный (по умолчанию)
- low — низкий

Задачи сортируются: high → normal → low.
