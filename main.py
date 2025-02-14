from task1 import kwargsAcceptFun
from task2 import typeBasedTransformer
from task3 import func, funx


if __name__ == "__main__":
    kwargsAcceptFun(name="Elyor", car = "BWM", phone = "IPhone")  #Task1

    output = typeBasedTransformer(int_type=3, text_type="Data", boolen_type=True, list_type=[1, 2, 3])  #Task2
    print(output)

    func()      #Task3
    funx()
    func()
    funx()
    func()
  
