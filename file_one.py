from file_two import function_three
from file_two import function_four

print("__name__ no arquivo um está definido como: {}" .format(__name__))

def function_one():
   print("Função um é executada")

def function_two():
   print("Função dois é executada")

if __name__ == "__main__":
   print("Arquivo um executado quando rodou diretamente")
   function_two()
   function_three()
   function_four()
else:
   print("Arquivo um executado ao ser importado")