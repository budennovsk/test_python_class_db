class MyExeption(Exception):
    """ Создание собственного класса ошибок, наследованного от базового"""
    pass


class Validator:
    """ Создание собственного класса с валидацией"""

    # protected метод, служит для обращения внутри класса и во всех его дочерних классах
    def _is_valid(self, value: str) -> str:
        """ Проверка вводимых значений на String"""
        if isinstance(value, (int, float, dict)):
            raise TypeError('Неверный тип данных, необходим String')
        return value


class ProductsImpl(Validator):
    """ Класс с методами CRUD и наследником от Validator """

    # Переменная хранит в себе список словарей, данный вариант имеет удобочитаемый формат \
    # с точки зрения big О, имеет сложность O(1) на получение элемента в словаре. \
    # формат легко сериализуется в JSON.

    product_list = []

    def __init__(self, id_name: str, name: str) -> None:
        """ Инициализация переменных, метод вызывается автоматически при создании экземпляра класса"""
        # хранение данных в момент создания экземпляра
        self.product_dict_nested = {}
        self.id_name = id_name
        self.name = name

    # Dunder methods вызывается автоматически при создании или изменении свойств класса
    def __setattr__(self, key: str, value: str) -> None:
        """ Валидация свойств класса проверка на String"""

        if (key == "id_name" and type(value) != str) or (key == "id_name" and value.isalpha()):
            raise MyExeption('Неверный тип данных, необходим String')
        if key == "name" and type(value) != str or (key == "name" and value.isdigit()):
            raise MyExeption('Неверный тип данных, необходим String')

        object.__setattr__(self, key, value)

    # статический метод не привязан к экземпляру класса, а только к классу и не может изменить его
    @staticmethod
    def get_repeat(id_name: str) -> list:
        """ Поиск в базе данных значения по id, при нахождении возвращает True"""
        list_data = []
        for items in ProductsImpl.product_list:
            if items.get('id_name') == id_name:
                list_data.append(True)
        return list_data

    def addProduct(self):
        """ Метод по добавлению пользователей в БД """
        if not self.get_repeat(self.id_name):
            self.product_dict_nested['id_name'] = self.id_name
            self.product_dict_nested['name'] = self.name
            self.product_list.append(self.product_dict_nested)
            return f' Пользователь создан : {True}'
        return f' Пользователь с таким id существует: {False}'

    def deleteProduct(self, id_name: str) -> str:
        """ Удаления пользователей из Бд по id """
        self._is_valid(id_name)
        for item in range(len(self.product_list)):
            if self.product_list[item]['id_name'] != id_name:
                continue
            del self.product_list[item]
            return f' Пользователь был удален: {True}'
        return f' Пользователь с таким id не существует: {False}'

    def getName(self, id_name: str) -> str:
        """ Получение пользователей из Бд с именем """
        self._is_valid(id_name)
        get_name = [item.get('name') for item in self.product_list if item.get('id_name') == id_name]
        if get_name:
            return f'Пользователь с именем: {str(*get_name)}'
        return f'Пользователь с таким именем не найден: {""}'

    def List_findByName(self, name: str) -> str:
        """ Получение списка id пользователей из Бд, с одинаковыми именами """
        self._is_valid(name)
        get_id_name = [item.get('id_name') for item in self.product_list if item.get('name') == self.name]
        if get_id_name:
            return f'Список индетификаторов с одинаковыми именами: {get_id_name}'
        return f'Индетификаторов с одинаковыми именами не найдено: {[]}'


# Выполняет данный скрипт только при запуске этого модуля
if __name__ == '__main__':
    # Создание экземпляра класса со свойствами
    data = ProductsImpl('1', 'Anna')
    # Добавление пользователей в список
    print(data.addProduct())
    # --//--
    data = ProductsImpl('2', 'Victory')
    print(data.addProduct())
    # --//--
    data = ProductsImpl('3', 'Andrey')
    print(data.addProduct())
    # --//--
    data = ProductsImpl('4', 'Anna')
    print(data.addProduct())
    # Вывод все БД с пользователями перед удалением
    print(ProductsImpl.product_list)
    # Удаление пользователя по id
    print(data.deleteProduct('3'))
    # Вывод все БД с пользователями после удаления
    print(ProductsImpl.product_list)
    # Получение имени пользователя по id
    print(data.getName('1'))
    # Получение списка id пользователей с одинаковыми именами
    print(data.List_findByName('Anna'))
