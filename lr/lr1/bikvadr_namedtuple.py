import sys 
import math
from typing import NamedTuple
class BiquadraticResult:
    NoRoots=NamedTuple("NoRoots",[])
    OneRoot=NamedTuple("OneRoot",[("root",float)])
    TwoRoots=NamedTuple("TwoRoots",[("root1",float),
                                    ("root2",float)])
    ThreeRoots=NamedTuple("ThreeRoots",[("root1",float),
                                   ("root2",float),
                                   ("root3",float)])
    FourRoots=NamedTuple("FourRoots",[("root1",float),
                                       ("root2",float),
                                       ("root3",float),
                                       ("root4",float)])
def get_coef(index,prompt):
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

def get_roots(a,b,c):
    D=b*b-4*a*c
    if D<0.0:
        t_list=[]
    elif D==0.0:
        t_list=[-b/(2.0*a)]
    else:
        sqD=math.sqrt(D)
        t_list=[(-b+sqD)/(2.0*a),
                (-b-sqD)/(2.0*a)]
    roots=[]
    for t in t_list:
        if t>0.0:
            sq=math.sqrt(t)
            roots.append(sq)
            roots.append(-sq)
        elif t==0.0:
            roots.append(0.0)
    unique=[]
    for r in roots:
        if r not in unique:
            unique.append(r)
    match unique:
        case[]:
            return BiquadraticResult.NoRoots()
        case [r]:
            return BiquadraticResult.OneRoot(r)
        case [r1,r2]:
            return BiquadraticResult.TwoRoots(r1,r2)
        case [r1,r2,r3]:
            return BiquadraticResult.ThreeRoots(r1,r2,r3)
        case[r1,r2,r3,r4]:
            return BiquadraticResult.FourRoots(r1,r2,r3,r4)
def print_roots(result):
    match result:
        case BiquadraticResult.NoRoots():
            print('Корней нет')
        case BiquadraticResult.OneRoot(root):
            print('Oдин корень: "{}"'.format(root))
        case BiquadraticResult.ThreeRoots(root1,root2):
            print('Два корня: "{}","{}"'.format(root1,root2))
        case BiquadraticResult.ThreeRoots(root1,root2,root3):
            print('Три корня: "{}","{}","{}"'.format(root1,root2,root3))
        case BiquadraticResult.FourRoots(root1,root2,root3,root4):
            print('Четыре корня: "{}","{}","{}","{}"'.format(root1,root2,root3,root4))
def main():
    a=get_coef(1,'Введите число а:')
    b=get_coef(2,'Введите число b:')
    c=get_coef(3,'Введите число c:')
    result=get_roots(a,b,c)
    print_roots(result)

if __name__=="__main__":
    main()