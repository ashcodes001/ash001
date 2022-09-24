
rates=input ("hourly rate: ")
hours=input ("time worked:")
hours=int(hours)
rates=int(rates)


def computepay (hours, rates):
  if int (hours)>=40:
    hay=int(hours)-40
    j=int (rates)*1.5
    l=int (hay)*int (j)
    k=40*int (rates)+int(l)
    print ("the salary is ",k)
  else:
    print (int(rates) *int(hours)) 
computepay(int (hours), int(rates))            


