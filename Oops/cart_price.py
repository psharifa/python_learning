def __init__(self):
        self.items={}
        self.price={"car": 100000,"bike": 50000, "book":30,"pen":20}
    def add_items(self,item_name,quantity):
        self.items[item_name]=quantity
    def get_items(self):
        #lis=list(self.items.items())
        print(self.items)
        #print(lis)
    def up_items(self,item_name,quantity):
        self.items[item_name]=quantity
    def remove_items(self,item_name):
        del self.items[item_name]
    def get_price(self):
        total_price=0 
        for i,j in self.items.items():#i=item_name,j=quantity
            total_price += j*self.price[i]
        return total_price
            
    
        
obj=cart()
obj.add_items("book",50)
obj.get_items()
obj.add_items("car",8)
obj.get_items()
obj.up_items("car",8)
obj.get_items()
#obj.remove_items("car")
#obj.get_items()
obj.add_items("bike",4)
obj.get_items()
obj.add_items("pen",100)
obj.get_items()
total=obj.get_price()
print("Total_price:  "+str(total))



'''
output:

{'book': 50}
{'book': 50, 'car': 8}
{'book': 50, 'car': 8}
{'book': 50, 'car': 8, 'bike': 4}
{'book': 50, 'car': 8, 'bike': 4, 'pen': 100}
Total_price:  1003500

'''
