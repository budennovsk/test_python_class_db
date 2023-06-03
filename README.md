# Тестовое задание от НОНТОН.РФ 

&ensp; Задание необходимо выполнить на любом C-подобном языке в задаче нельзя использовать базы данных или любые другие бибилиотеки
В целом вы не ограничены в реализации, только использовать стандартные структуры данных sdk.
Необходимо реализовать все 4 функции в классе ProductsImpl реализоцию писать в теле самих функций вы в праве добавлять необходимые вам структуры данных в класс 
структура ``` Product, id ``` - уникальный номер продукта, name - наименование
``` 
class Product {
late String id;
late String name;
}
```
класс для реализации 4 функций
``` class ProductsImpl ``` 
* добавляет новый продукт 
  * возвращает true - если продукта с таким id еще не было
  * возвращает false - если был такой id, вставка отменяется ``` bool addProduct(Product product) ```

* Удаляет продукт
  * возвращает true - если продукт с таким id был
  * возвроащает false - если id не было, (удаления не происходит) ``` bool deleteProduct(Product product) ```

* Получает имя (name) продукта
  * возращает name продукта у которого идентификатор равен (=) id
  * если продукта нет, вернуть пустую строку '' ```  String getName(String id) ```

* возвращает массив (список) идентификаторов (id)
  * У котрых наименование равно (=) name
  * Если таких нет, возвращается пустой массив (список) ``` List findByName(String name) ```



## Stack:
![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54)

___

### Выполнение скрипта без ошибок
![1](https://github.com/budennovsk/test_python_class_db/assets/97764479/cb3c72a8-c20c-40e6-947b-5c8fba7ec3d0)

### Исключения типизации
![2](https://github.com/budennovsk/test_python_class_db/assets/97764479/cc89dd96-1fa3-4390-98dd-2743d620341f)

### Логические ошибки
![3](https://github.com/budennovsk/test_python_class_db/assets/97764479/784306d8-64c6-46ea-af1a-102e7c175abd)

