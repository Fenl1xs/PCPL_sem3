import sys
import math
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

def get_roots(a, b, c):
    result=[]
    D=b*b-4*a*c
    if D<0.0:
        return result
    if D==0.0:
        t_list=[-b/(2.0*a)]
    else:
        sqD=math.sqrt(D)
        t_list=[(-b+sqD)/(2.0*a),
                (-b-sqD)/(2.0*a)]
    for t in t_list:
        if t>0.0:
            sq=math.sqrt(t)
            result.append(sq)
            result.append(-sq)
        elif t==0.0:
            result.append(0.0)
    unique=[]
    for r in result:
        if r not in unique:
            unique.append(r)
    return unique
def main():
    a=get_coef(1,'Введите число а:')
    b=get_coef(2,'Введите число b:')
    c=get_coef(3,'Введите число c:')
    roots=get_roots(a,b,c)
    len_roots=len(roots)
    if len_roots==0:
        print('Корней нет')
    elif len_roots==1:
        print('Один корень: "{}"'.format(roots[0]))
    elif len_roots==2:
            print('Два кореня: "{}","{}"'.format(roots[0],roots[1]))
    elif len_roots==3:
            print('Три кореня:"{}","{}", "{}"'.format(roots[0],roots[1],roots[2]))
    else:
        print('Четыре корня:"{}","{}","{}", "{}"'.format(roots[0],roots[1],roots[2],roots[3]))

if __name__=="__main__":
    main()
    
    
