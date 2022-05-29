# denemek için variable tanımlanacak veri dizisi oluşturuluyor.
from functools import total_ordering


customerName ="çağrı"
customerSurname ="şimşek"
customerNameSurname=customerName+" "+customerSurname
customerGender= True #erkek
customerID="TCNO:1234121112"
customerBirthDate=1991
customerAdress="Beykoz / İSTANBUL"
customerAge=str(2022-customerBirthDate)
customerDescription=customerNameSurname+ "  "+customerAge+" "+customerAdress+ " "+customerID
print(customerDescription)

# order1=110
# order2=1100.5
# order3=356.95
# total= order3+order1+order2
# print (total)
# '''
