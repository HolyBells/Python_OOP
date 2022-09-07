class File:
    def __init__(self, name):
        self.name = name
        self.in_trash = False
        self.is_deleted = False

    def restore_from_trash(self):
        print(f'Файл {self.name} восстановлен из корзины')
        self.in_trash = False

    def remove(self):
        print(f'Файл {self.name} был удален')
        self.is_deleted = True

    def read(self):
        if self.is_deleted:
            print(f'ErrorReadFileDeleted({self.name})')
            return
        if self.in_trash:
            print(f'ErrorReadFileTrashed({self.name})')
            return
        if not self.is_deleted and not self.in_trash:
            print(f'Прочитали все содержимое файла {self.name}')
            return

    def write(self, content):
        if self.is_deleted:
            print(f'ErrorWriteFileDeleted({self.name})')
            return
        if self.in_trash:
            print(f'ErrorWriteFileTrashed({self.name})')
            return
        if not self.is_deleted and self.in_trash:
            print(f'Записали значение {content} в файл {self.name}')
            return


class Trash:
    content = []

    @staticmethod
    def add(x):
        if not isinstance(x, File):
            print('В корзину добавлять можно только файл')
            return
        else:
            Trash.content.append(x)
            x.in_trash = True
            return

    @staticmethod
    def clear():
        print('Очищаем корзину')
        for elem in Trash.content:
            File.remove(elem)
        Trash.content.clear()  # очищаем список
        print('Корзина пуста')

    @staticmethod
    def restore():
        print('Восстанавливаем файлы из корзины')
        for elem in Trash.content:
            File.restore_from_trash(elem)
        Trash.content.clear()  # очищаем список
        print('Корзина пуста')