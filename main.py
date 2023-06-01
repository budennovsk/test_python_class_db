class ProductsImpl:
    product_list = []

    def __init__(self):
        self.product_dict_nested = {}

    @staticmethod
    def get_repeat(id_name):
        list_data = []
        for items in ProductsImpl.product_list:
            if items.get('id_name') == id_name:
                list_data.append(True)
        return list_data

    def addProduct(self, id_name, name):
        if not self.get_repeat(id_name):
            self.product_dict_nested['id_name'] = id_name
            self.product_dict_nested['name'] = name
            ProductsImpl.product_list.append(self.product_dict_nested)
        else:
            raise BaseException('Дубликат')

    def deleteProduct(self, id_name):
        self.product_list[:] = [items for items in self.product_list if items.get('id_name') != id_name]
        print(self.product_list)

    def getName(self, id_name):
        get_name = [i for i in self.product_list if i.get('id_name') == id_name]
        print(get_name[0]['name'])

    def List_findByName(self, name):
        get_name = [i for i in self.product_list if i.get('name') == name]
        print(get_name)


if __name__ == '__main__':
    data = ProductsImpl()

    data.addProduct(22, 'serga')


    data1 = ProductsImpl()
    data1.addProduct(1, 'serga')
    data2 = ProductsImpl()
    data2.addProduct(2, 'serga')

    data3 = ProductsImpl()
    data3.deleteProduct(2)

    print(ProductsImpl.product_list)
