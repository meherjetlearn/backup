shop=True
finalC=0
finalT=0
while shop==True:
    name=input("What is the name of the product that you want to buy?")
    quantity=int(input(f"What is the quantity of {name} that you want to buy?"))
    price=float(input(f"How much does 1 {name} cost?"))
    imp=input("Is this item imported? [y/n]")
    exe=input("Is this item  exempted? [y/n]")
    if imp=="y" and exe=="y":
      tax=0.05
      totalC=((quantity*price)+(quantity*price)*tax)
      finalC+=totalC
      finalT+=totalC-(quantity*price)
      print(f"Your total cost for {quantity} {name} is {totalC}.\n The sales tax on this is {totalC-(quantity*price)}")

    if imp=="n" and exe=="n":
      tax=0.1
      totalC=((quantity*price)+(quantity*price)*tax)
      finalC+=totalC
      finalT+=totalC-(quantity*price)
      print(f"Your total cost for {quantity} {name} is {totalC}.\n The sales tax on this is {totalC-(quantity*price)}")

    if imp=="y" and exe=="n":
      tax=0.05
      totalC=((quantity*price)+(quantity*price)*tax)
      finalC+=totalC
      finalT+=totalC-(quantity*price)
      print(f"Your total cost for {quantity} {name} is {totalC}.\n The sales tax on this is {totalC-(quantity*price)}")

    if imp=="n" and exe=="y":
      tax=0
      totalC=(quantity*price)
      finalC+=totalC
      finalT+=totalC-(quantity*price)
      print(f"Your total cost for {quantity} {name} is {totalC}.\n The sales tax on this is {totalC-(quantity*price)}") 

    more=input("Do you want to add more items? [y/n]")
    if more=="n":
      print(f"Your total cost is {finalC}!\nYou payed {finalT} extra due to tax :(")
      shop=False