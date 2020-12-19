import sys

f=lambda x: x**2 if x>0 else None
a = int(sys.argv[1])
print(f(a))
print('exemple de fonction lambda')
