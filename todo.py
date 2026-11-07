"""Simple in-memory to-do list checker (terminal menu)."""

from __future__ import annotations


def add_task(tasks: list[dict], text: str) -> dict | None:
    cleaned = text.strip()
    if not cleaned:
        return None
    task = {"id": len(tasks) + 1, "text": cleaned, "done": False}
    tasks.append(task)
    return task


def toggle_task(tasks: list[dict], number: int) -> dict | None:
    if number < 1 or number > len(tasks):
        return None
    task = tasks[number - 1]
    task["done"] = not task["done"]
    return task


def delete_task(tasks: list[dict], number: int) -> dict | None:
    if number < 1 or number > len(tasks):
        return None
    removed = tasks.pop(number - 1)
    for index, task in enumerate(tasks, start=1):
        task["id"] = index
    return removed


def format_task(task: dict) -> str:
    mark = "x" if task["done"] else " "
    return f"{task['id']}. [{mark}] {task['text']}"


def format_list(tasks: list[dict]) -> str:
    if not tasks:
        return "No tasks yet."
    return "\n".join(format_task(task) for task in tasks)


def read_choice(prompt: str) -> str:
    return input(prompt).strip()


def read_number(prompt: str) -> int | None:
    raw = read_choice(prompt)
    if not raw.isdigit():
        return None
    return int(raw)


def run() -> None:
    tasks: list[dict] = []
    actions = {
        "1": "add",
        "2": "list",
        "3": "toggle",
        "4": "delete",
        "5": "quit",
    }

    while True:
        print("\n--- To-do list ---")
        print("1) Add task")
        print("2) List tasks")
        print("3) Check off / uncheck")
        print("4) Delete task")
        print("5) Quit")
        choice = read_choice("Choose 1-5: ")
        action = actions.get(choice)

        if action == "add":
            created = add_task(tasks, read_choice("Task: "))
            print("Added." if created else "Task cannot be empty.")
        elif action == "list":
            print(format_list(tasks))
        elif action == "toggle":
            if not tasks:
                print("No tasks yet.")
                continue
            print(format_list(tasks))
            updated = toggle_task(tasks, read_number("Task number: ") or 0)
            print("Updated." if updated else "That number is not on the list.")
        elif action == "delete":
            if not tasks:
                print("No tasks yet.")
                continue
            print(format_list(tasks))
            removed = delete_task(tasks, read_number("Task number: ") or 0)
            print("Deleted." if removed else "That number is not on the list.")
        elif action == "quit":
            print("Bye.")
            return
        else:
            print("Please choose 1, 2, 3, 4, or 5.")


if __name__ == "__main__":
    run()
