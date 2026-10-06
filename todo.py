class Task:
    def __init__(self, title):
        self.title = title
        self.done = False

    def mark_done(self):
        self.done = True

    def __str__(self):
        mark = "x" if self.done else " "
        return f"[{mark}] {self.title}"


class TaskManager:
    def __init__(self):
        self.tasks = []

    def add_task(self, title):
        task = Task(title)
        self.tasks.append(task)
        print(f"تمت إضافة: {task}")

    def show_tasks(self):
        if len(self.tasks) == 0:
            print("ما في مهام")
        else:
            for i, task in enumerate(self.tasks, 1):
                print(f"{i}. {task}")

    def delete_task(self, number):
        if 0 < number <= len(self.tasks):
            removed = self.tasks.pop(number - 1)
            print(f"تم حذف: {removed}")
        else:
            print("رقم غلط!")

    def complete_task(self, number):
        if 0 < number <= len(self.tasks):
            self.tasks[number - 1].mark_done()
            print(f"تم إنجاز: {self.tasks[number - 1]}")
        else:
            print("رقم غلط!")

        
manager = TaskManager()

while True:
    print("\n--- To-Do List ---")
    print("1. إضافة مهمة")
    print("2. عرض المهام")
    print("3. حذف مهمة")
    print("4. خروج")
    print("5. إنجاز مهمة")

    choice = input("اختر رقم: ")

    if choice == "1":
        title = input("اكتب المهمة: ")
        manager.add_task(title)
    elif choice == "2":
        manager.show_tasks()
    elif choice == "3":
        manager.show_tasks()
        try:
            number = int(input("رقم المهمة: "))
        except ValueError:
            print("لازم تكتبين رقم!")
            continue
        manager.delete_task(number)
    elif choice == "4":
        break
    elif choice == "5":
        manager.show_tasks()
        try:
            number = int(input("رقم المهمة: "))
        except ValueError:
            print("لازم تكتبين رقم!")
            continue
        manager.complete_task(number)
    else:
        print("خيار غلط!")