class software():
    '''
    класс що описує нам головне про дане програмне забеспечення
    name - назва програмного забезпечення
    version - версія програмного забезпечення
    developer - розробник програмного забезпечення
    function - фугкція програмного забеспечення
    '''
    def __init__(self, name, version, developer, function):
        self.name = name
        self.versionn = version
        self.developer = developer
        self.function = function
    def information(self):
        print(f"Назва: {self.name}")
        print(f"Версія: {self.version}")
        print(f"Розробник: {self.developer}")
        print(f"Функція: {self.function}")
class OperatingSystem(software):
    '''
    класс нащадок який успадкував атрибути та методи класу software
    а також має додаткові атрибути та методи, які описують специфічні характеристики операційних систем
    kernel_type - тип ядра
    interface - інтерфейс
    n_program() - запуск програми
    memory_management()	- Управляє пам'яттю
    '''

    def __init__(self, name, version, developer, function, kernel_type, interface):
        super().__init__(name, version, developer, function)
        self.kernel_type = kernel_type
        self.interface = interface

    def run_program(self, program):
        print(f"Запуск програми {program} на {self.name}")

    def memory_management(self):
        print(f"Управління пам'яттю в {self.name}")


# Приклад використання
os = OperatingSystem("Windows 11", "22H2", "Microsoft", "Операційна система", "Мікроядро", "GUI")

os.information()
os.run_program("Notepad")
os.memory_management()

