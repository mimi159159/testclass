
from comp import *
from simp import *
def check():
    if adding() or subtract() :
        return True
def first():
  if check== True:
      pass
  else: raise Exception("Function cannot be called without calling the simp functions first")
def main():
    print(adding(3,5),subtract(8,9),sumofdigits(987), ispal(9889))  
if __name__ =='__main__':
       main()