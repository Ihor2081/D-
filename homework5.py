def show_notes():
    try:
        with open("notes.txt", "r", encoding="utf-8") as file:
            notes = file.readlines()

        if not notes:
            print("🗒Нотаток ще немає.")
        else:
            print("📘Список нотаток: ")
            for note in notes:
                # print("-", note.strip())
                print(note.strip())
    except FileNotFoundError:
        print("Файл ще не створений.")


def add_note():
    note = input("Введіть нову нотатку: ")
    with open("notes.txt", "a", encoding="utf-8") as file:
        file.write(note + "\n")
    print("✅Нотатку збережено!")


def clear_notes():
    with open("notes.txt", "w", encoding="utf-8") as file:
        pass
    print("🧹Усі нотатки видалено!")

def number_delete():
        try:
            with open("notes.txt", "r", encoding="utf-8") as file:
                notes = file.read().splitlines()

            a = int(input("Введіть порядковий номер нотатки для видалення: ")) - 1

            if a < 0 or a >= len(notes):
                print("Нотатки з таким номером не існує")
                return

            deleted_note = notes.pop(a)

            with open("notes.txt", "w", encoding="utf-8") as file:
                file.write("\n".join(notes))

            print("Нотатку видалено:", deleted_note)

        except ValueError:
            print("Некоректний ввід! Введіть число.")

def export_notes():
    content=" "
    with open("notes.txt", "r", encoding="utf-8") as file:
        content=file.read()
    with open("backup.txt", "w", encoding="utf-8") as file:
        file.write(content)
    print("Нотатки перенесено до резервного файлу!")

while True:
    print("\n — Меню —")
    print("1. Додати нотатку")
    print("2. Показати нотатки")
    print("3. Очистити нотатки")
    print("4. Видалити нотатку за порядковим номером")
    print("5. Експортувати нотатки до резервного файлу")
    print("6. Вихід")

    choice = input("Оберіть дію: ")

    if choice == "1":
        add_note()
    elif choice == "2":
        show_notes()
    elif choice == "3":
        clear_notes()
    elif choice == "4":
        number_delete()
    elif choice == "5":
        export_notes()
    elif choice == "6":
        print("До побачення!")
        break
    else:
        print("❌Невірна команда.")



# Спробуй записати дані у CSV-файл (через кому).
# with open("notes.txt", "r", encoding="utf-8") as file:
#      notes=file.read().strip()
# with open("data.csv", "w", encoding="utf-8") as file:
#      print(",".join(notes.split(',')))
#      file.write(",".join(notes.split(',')))
# split - до рядка
# join - зэднує масив