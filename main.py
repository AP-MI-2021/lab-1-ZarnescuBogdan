'''
Returneaza true daca n este prim si false daca nu.
'''
def is_prime(n):
  '''
  '''
  # codul vostru aici
    n = int(input("Dati un numar: "))
    k = 2
    ok = 0
    if n < 2:
      return False
    while k < n/2:
      if n % k == 0:
        return False
      k++
    return True
  
'''
Returneaza produsul numerelor din lista lst.
'''
def get_product(lst):
  # codul vostru aici
    n = int(input("Dati numarul de numere: "))
    p = 1
    for i in range(n):
      x = int(input("x = "))
      p = p*x
    return p
  
'''
Returneaza CMMDC a doua numere x si y folosind primul algoritm.
'''
def get_cmmdc_v1(x, y):
  # codul vostru aici
  x = int(input("x = "))
  y = int(input("y = "))
  while x != y:
    if x < y
      y = y-x
    else
      x = x-y
  return x
'''
Returneaza CMMDC a doua numere x si y folosind al doilea algoritm.
'''
def get_cmmdc_v2(x, y):
  # codul vostru aici
  x = int(input("x = "))
  y = int(input("y = "))
  while b != 0:
    r = a%b
    a = b
    b = r
  return a
  
def main():
  # interfata de tip consola aici

if __name__ == '__main__':
  main()
