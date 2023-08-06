def gcd(x,y):
  if x%y == 0: return y
  return gcd(y,x%y)

class Fraction:
  def __init__(self,a,b):
    self.numerator = a; self.denominator = b

  def __str__(self):
    return str(self.numerator)+'/'+str(self.denominator)

  def simplify(self):
    g = gcd(self.numerator,self.denominator)
    return Fraction(self.numerator//g,self.denominator//g)
  
  def __add__(self,other):
    ans_numerator = self.numerator*other.denominator+other.numerator*self.denominator
    ans_denominator = self.denominator*other.denominator
    g = gcd(ans_numerator,ans_denominator)
    return Fraction(ans_numerator//g,ans_denominator//g)

  def __sub__(self,other):
    ans_numerator = self.numerator*other.denominator-other.numerator*self.denominator
    ans_denominator = self.denominator*other.denominator
    g = gcd(ans_numerator,ans_denominator)
    return Fraction(ans_numerator//g,ans_denominator//g)

  def __mul__(self,other):
    ans_numerator = self.numerator*other.numerator
    ans_denominator = self.denominator*other.denominator
    g = gcd(ans_numerator,ans_denominator)
    return Fraction(ans_numerator//g,ans_denominator//g)

  def __truediv__(self,other):
    new_other = Fraction(other.denominator,other.numerator)
    return Fraction.__mul__(self,new_other)

if __name__ == '__main__':
    a,b,c,d = [int(e) for e in input().split()]
    fraction1 = Fraction(a,b)
    fraction2 = Fraction(c,d)
    print(f"fraction1 = {fraction1}")
    print(f"fraction2 = {fraction2}")
    print(f"fraction1+fraction2 = {fraction1+fraction2}")
    print(f"fraction1-fraction2 = {fraction1-fraction2}")
    print(f"fraction1*fraction2 = {fraction1*fraction2}")
    print(f"fraction1/fraction2 = {fraction1/fraction2}")
