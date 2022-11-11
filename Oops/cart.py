class cart:
    def __init__(self):
        self.items={}
    def add_items(self,item_name,quantity):
        self.items[item_name]=quantity
    def get_items(self):
        lis=list(self.items.items())
        print(self.items)
        print(lis)
    def up_items(self,item_name,quantity):
        self.items[item_name]=quantity
    def remove_items(self,item_name):
        del self.items[item_name]
      
      
        
obj=cart()
obj.add_items("book",50)
obj.get_items()
obj.add_items("car",1000)
obj.get_items()
obj.up_items("car",800)
obj.get_items()
obj.remove_items("car")
obj.get_items()
obj.add_items("bike",4000)
obj.get_items()
obj.add_items("pen",10)
obj.get_items()


'''
output:

{'book': 50}
[('book', 50)]
{'book': 50, 'car': 1000}
[('book', 50), ('car', 1000)]
{'book': 50, 'car': 800}
[('book', 50), ('car', 800)]
{'book': 50}
[('book', 50)]
{'book': 50, 'bike': 4000}
[('book', 50), ('bike', 4000)]
{'book': 50, 'bike': 4000, 'pen': 10}
[('book', 50), ('bike', 4000), ('pen', 10)]

'''
