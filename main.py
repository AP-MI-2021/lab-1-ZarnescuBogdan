'''
Returneaza true daca n este prim si false daca nu.
'''
def is_prime(n):
  '''
  Input:
  - n: int
  Output:
  - primalitatea lui n
  '''
  # codul vostru aici
  if n < 2:
    return False
  for i in range(2, n): # 2, 3, 4, ..., n-1
    if n % i == 0:
      return False
  return True
'''
Returneaza produsul numerelor din lista lst.
'''
def get_product(lst):
  '''
  Input:
  - lst[]: int
  Output:
  - produsul numerelor din lista
  '''
  # codul vostru aici
  n = int(input('Dati numarul de elemente: '))
  p = 1
  for i in range(0,n):
    x = int(input("x = "))
    lst.append(x)
    p = p * x
  return p
  
'''
Returneaza CMMDC a doua numere x si y folosind primul algoritm.
'''
def get_cmmdc_v1(x, y):
  '''
  Input:
  - x, y: int
  Output:
  - cel mai mic divizor comun al numerelor x si y
  '''
  # codul vostru aici
  while x != y:
    if x < y:
      y = y-x
    else:
      x = x-y
  return x
'''
Returneaza CMMDC a doua numere x si y folosind al doilea algoritm.
'''
def get_cmmdc_v2(x, y):
  '''
  Input:
  - x, y: int
  Output:
  - cel mai mic divizor comun al numerelor x si y
  '''
  # codul vostru aici
  while y != 0:
    r = x % y
    x = y
    y = r
  return a

def test_is_prime():
  assert is_prime(3) == True
  assert is_prime(4) == False

def main():
  # interfata de tip consola aici
  while True:
    print('1. Determinarea primalitatii.')
    print('2. Determinarea produsului numerelor.')
    print('3. Determinarea celui mai mic divizor comun - varianta 1.')
    print('4. Determinarea celui mai mic divizor comun - varianta 2.')
    print('x. Iesire din program - exit.')
    optiune = input('Alege optiunea: ')
    if optiune == '1':
      n = int(input("Dati un numar:"))
      if is_prime(n):
        print('Numarul dat este prim.')
      else:
        print('Numarul dat nu este prim.')
    elif optiune == '2':
      lst = []
      print(get_product(lst))
    elif optiune == '3':
      x = int(input("x = "))
      y = int(input("y = "))
      print(get_cmmdc_v1(x, y))
    elif optiune == '4':
      x = int(input("x = "))
      y = int(input("y = "))
      print(get_cmmdc_v2(x, y))
    elif optiune == 'x':
      break
    else:
      print('Optiune invalida.')

test_is_prime()
if __name__ == '__main__':
  main()
