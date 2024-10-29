class calculator:
    def __init__(self, a, b, c) -> None:
        self.a = a
        self.b = b
        self.c = c
    def sum(self):
        print(f'The Sum of a, b, c is {self.a + self.b + self.c}')
    def fectorial(self):
        fectorial = 1
        if self.b < 0:
            print(f"sorry we can not fectorial of negative number")
        elif self.b == 0:
            print('The fectorial of 0 is 1')
        else:
            for i in range(1, self.b +1):
                fectorial =  fectorial * i
            print(f'The fectorial of b is {fectorial}')
                
        

Number = calculator(3, 5, 9)
Number.sum()
Number.fectorial()