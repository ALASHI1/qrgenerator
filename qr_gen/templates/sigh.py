

class Dog:
    def __init__(self,age,name):
        self.age = age
        self.name = name
        
    def __repr__(self):
    	return f" {self.name},{self.age} "
    
def oldest_dog(dog_list):
    dog_list.sort(key=lambda x:x.age, reverse=True)
    print(dog_list)
    print(f"The oldest dog is {dog_list[0].name},its age is {dog_list[0].age} years old")
    
dog_list = [Dog(15,"jack"),Dog(18,"billy"),Dog(13,"Bingo")]
oldest_dog(dog_list)
    
    
