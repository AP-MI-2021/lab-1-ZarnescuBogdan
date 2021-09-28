'''
Returneaza true daca n este prim si false daca nu.
'''
def is_prime(n):
  # codul vostru aici
    int(n,k,ok)
    k = 2
    ok = 0
    while k < n:
    {
        if n % k == 0
        {
            ok = 1
            break
        }
        k++
    }
    if ok == 1
    {
      print("n = ")
      print(n)
      print(" nu este prim")
      return True
    }
    else
    {
      print("n = ")
      print(n)
      print(" este prim")
      return False
    }
  
'''
Returneaza produsul numerelor din lista lst.
'''
def get_product(lst):
  # codul vostru aici
    int(n,p)
    p = 1
    int(v[n+1],i)
    for i in range(1,n):
      {
        p *= v[i]
      }
    print("produsul este ")
    print(p)
  
'''
Returneaza CMMDC a doua numere x si y folosind primul algoritm.
'''
def get_cmmdc_v1(x, y):
  # codul vostru aici
  int(a,b)
    while a != b:
    {
        if a < b
            b -= a
        else
            a -= b
    }
    print(a)
  
'''
Returneaza CMMDC a doua numere x si y folosind al doilea algoritm.
'''
def get_cmmdc_v2(x, y):
  # codul vostru aici
  int(a,b,r)
    while b != 0:
    {
        r = a%b
        a = b
        b = r
    }
    print(a)
  
def main():
  # interfata de tip consola aici

if __name__ == '__main__':
  main()
