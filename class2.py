# hi= 'hello there'
# name='ana'
# greet= hi+name
#print(greet)

# greeting=hi+' '+name
#print(greeting)

#silly=hi+(' '+name)*3
#print (silly) 




x=1
#print(x)
#x_str=str(x)
#print('my fav number is', x, '.', 'x=', x)
#print('my fav cumber is', x_str + '.'+ 'x=' +x_str)
#print('my fav number is' +x_str+'.'+'x='+x_str)
    #con , se dan espacios. con + no. ambas unen lo descrito.   




#text=input('type anything...')
#print(5*text)

#num=int(input('type a number...'))
#print(5*num)
    #imprime numeros tiene que llevar num de lo contrario seria string es decir solo texto



"a" > "b"
#los compara lexicograficamente, viene antes o despues
    #ASK BEN how can I get a true or false result from it?



#x=float(input('Enter a number for x: '))
#y=float(input('Enter a number for Y: '))

#if x == y:
  #  print('x and y are equal')
   # if y!=0:
    #    print('therefore, x/y is', x/y)
#elif x<y:
 #   print('x is smaller')
#else:
#    print('y is smaller')
#print('thanks!')


#while loops
#Example: Zelda game loop, se crea un loop si el jugador sigue llendo a la derecha, si cmabia a la izquierda rompe el cirlo.

#while <exit right>:
 #   <set background to woods_background>
#<set backgound to exit_background>

#Ex 2
#game Lost Forest
#n=input("You're in the Lost Forest. Go left or right?")
#while n=="right":
 #   n=input("You're in the Lost Forest. Go left or right?")
#print("You go out of the Lost Forest!!")

#Ex 2.0
n=input("You're in the Lost Forest.\n**********\n**********\n   :)\n**********\n*********\nGo left or right?")
while n=="right" or n=="Right":
    n=input("You're in the Lost Forest.\n**********\n****   **\n (╯°□°）╯︵ ┻━┻\n**********\n**********\n Go left or right?")
print("\nYou go out of the Lost Forest!!\n\o/")
