class Train: 
    def book_ticket(self, name, source, destination):
        self.name = name
        self.source = source
        self.destination = destination
        print(name,source,destination)
    
    def get_status(self):
        no_of_seats = 12
        return no_of_seats
    
    def get_fare_info(self, type='basic'):
        if(type == 'basic'):
            return 1200
        else:
            return 3000        


train_1 = Train()
print(train_1.get_fare_info('business'))
train_1.book_ticket('abdullah','karachi','lahore')
print(train_1.get_status())




# random integers can be added by using import random then using random.randint(12,222)

# better syntax is to do this from random import randint --> randint(12,222)