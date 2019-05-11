def f(x):
    return x**3 - 2*x

i=-1.0
while i<=1.0:
    print([round(i*0.6, 4), round(f(i)*0.6, 4), round((i/2+0.5), 4)],",")
    i+=0.1