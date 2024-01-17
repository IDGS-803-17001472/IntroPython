class OperaBas:
    #Declaracion de propiedades de clase
    num1=0
    num2=0
    res=0

    #Declaracion de constructor
    def __init__(self,a,b) :
        self.n1 = a
        self.n2 = b

    #declaracion de metodos de clase
    def suma(self):
        self.res = self.n1 + self.n2
        print("La suma es: {}".format(self.res))


def main():
    obj=OperaBas(3,4)
    obj.suma()

if __name__ == "__main__":
    main()