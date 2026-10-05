import sys
import math
class BiquardraticRoots:
    def __init__(self):
        self.coef_a=0.0
        self.coef_b=0.0
        self.coef_c=0.0
        self.num_roots=0.0
        self.roots_list=[]
    def get_coef(self,index,prompt):
        while True:
            try:
                coef_str=sys.argv[index]
            except IndexError:
                print(prompt)
                coef_str=input()
            try:
                return float(coef_str)
            except ValueError:
                print('Невозможно преобразовать "{}" в число.Повторите ввод.'.format(coef_str))
                if index < len(sys.argv):
                    sys.argv.pop(index)
    def get_coefs(self):
        self.coef_a=self.get_coef(1,'Введите число а:')
        self.coef_b=self.get_coef(2,'Введите число b:')
        self.coef_c=self.get_coef(3,'Введите число c:')
    def calculate_roots(self):
        a=self.coef_a
        b=self.coef_b
        c=self.coef_c
        D=b*b-4*a*c
        if D<0.0:
            t_list=[]
        elif D==0.0:
            t_list=[-b/(2.0*a)]
        else:
            sqD=math.sqrt(D)
            t_list=[(-b+sqD)/(2.0*a),
                    (-b-sqD)/(2.0*a)]
        for t in t_list:
            if t>0.0:
                sq=math.sqrt(t)
                self.roots_list.append(sq)
                self.roots_list.append(-sq)
            elif t==0.0:
                self.roots_list.append(0.0)
        unique=[]
        for r in self.roots_list:
            if r not in unique:
                unique.append(r)
        self.roots_list=unique
        self.num_roots=len(self.roots_list)
    def print_roots(self):
        if self.num_roots==0:
            print('Корней нет')
        elif self.num_roots==1:
            print('Один корень: "{}"'.format(self.roots_list[0]))
        elif self.num_roots==2:
            print('Два кореня: "{}","{}"'.format(self.roots_list[0],self.roots_list[1]))
        elif self.num_roots==3:
            print('Три кореня:"{}","{}", "{}"'.format(self.roots_list[0],[1],self.roots_list[2]))
        else:
            print('Четыре корня:"{}","{}","{}", "{}"'.format(self.roots_list[0],self.roots_list[1],self.roots_list[2],self.roots_list[3]))
def main():
    r=BiquardraticRoots()
    r.get_coefs()
    r.calculate_roots()
    r.print_roots()
if __name__=="__main__":
    main()