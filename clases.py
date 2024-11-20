
class Item:
    def __init__(self, item_id, name, quantity, price):
        self.item_id = item_id
        self.name = name
        self.quantity = quantity
        self.price = price

    def update_stock(self, amount):
        self.quantity += amount


    def get_info(self):
        return {
            'id': self.item_id,
            'name': self.name,
            'quantity': self.quantity,
            'price': self.price
        }



class PhysicalItem(Item):
    def __init__(self, item_id, name, quantity, price, weight, dimensions):
        super().__init__(item_id, name, quantity, price)
        self.weight = weight
        self.dimensions = dimensions

    def get_info(self):
        info = super().get_info()
        info.update({
            'weight': self.weight,
            'dimensions': self.dimensions
        })
        return info


class DigitalItem(Item):
    def __init__(self, item_id, name, quantity, price, file_size, download_link):
        super().__init__(item_id, name, quantity, price)
        self.file_size = file_size
        self.download_link = download_link

    def get_info(self):
        info = super().get_info()
        info.update({
            'file_size': self.file_size,
            'download_link': self.download_link
        })
        return info
