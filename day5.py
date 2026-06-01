tasks = []

def add_task(task):
    tasks.append(task)
    print(f"تمت إضافة: {task}")

def show_tasks():
    if len(tasks) == 0:
        print("ما في مهام")
    else:
        for i, task in enumerate(tasks, 1):
            print(f"{i}. {task}")

def delete_task(number):
    if number <= len(tasks) and number > 0:
        removed = tasks.pop(number - 1)
        print(f"تم حذف: {removed}")
    else:
        print("رقم غلط!")

while True:
    print("\n--- To-Do List ---")
    print("1. إضافة مهمة")
    print("2. عرض المهام")
    print("3. حذف مهمة")
    print("4. خروج")
    
    choice = input("اختر رقم: ")
    
    if choice == "1":
        task = input("اكتب المهمة: ")
        add_task(task)
    elif choice == "2":
        show_tasks()
    elif choice == "3":
        show_tasks()
        number = int(input("اكتب رقم المهمة: "))
        delete_task(number)
    elif choice == "4":
        print("مع السلامة!")
        break
    else:
        print("اختيار غلط!")
# تجربة
add_task("مذاكرة Python")
add_task("رياضة")
add_task("قراءة")
show_tasks()
delete_task(2)
show_tasks()

