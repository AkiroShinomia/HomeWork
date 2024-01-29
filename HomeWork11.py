import os
import shutil
import subprocess

def create_file(filename):
    with open(filename, 'w') as f:
        pass

def delete_file(filename):
    os.remove(filename)

def move_file(src, dest):
    shutil.move(src, dest)

def copy_file(src, dest):
    shutil.copy(src, dest)

def git_add(filename):
    subprocess.run(['git', 'add', filename])

def git_commit(message):
    subprocess.run(['git', 'commit', '-m', message])

def main():
    subprocess.run(['git', 'init'])

    while True:
        print("\n1. Создать файл")
        print("2. Удалить файл")
        print("3. Переместить файл")
        print("4. Скопировать файл")
        print("5. Выход")

        choice = input("\nВыберите действие: ")

        if choice == '1':
            filename = input("Введите имя файла для создания: ")
            create_file(filename)
            git_add(filename)
            git_commit("Добавлен файл: " + filename)
        elif choice == '2':
            filename = input("Введите имя файла для удаления: ")
            delete_file(filename)
            git_commit("Удален файл: " + filename)
        elif choice == '3':
            src = input("Введите путь к файлу для перемещения: ")
            dest = input("Введите путь назначения: ")
            move_file(src, dest)
            git_commit("Перемещен файл из {} в {}".format(src, dest))
        elif choice == '4':
            src = input("Введите путь к файлу для копирования: ")
            dest = input("Введите путь назначения: ")
            copy_file(src, dest)
            git_commit("Скопирован файл из {} в {}".format(src, dest))
        elif choice == '5':
            break
        else:
            print("Неверный ввод. Попробуйте снова.")

if __name__ == "__main__":
    main()
