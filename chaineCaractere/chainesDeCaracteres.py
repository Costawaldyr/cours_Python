s = 'bonjour'
print(s[0])
ch = s.replace("jour", "bon")
print(ch)

ch2 = "bonjour"
print(ch2[0])
print(len(ch2))
print(ch2.find('o')) # Si la methode find retourne -1 ca veut dire qu'il existe pas dans la chaine
print(ch2.find('O'))
print(ch2.rfind('o'))

print(ch2.upper()) #tous en maiscule
print(ch2[0].upper() + ch[1:].lower())

ch3= " IODA"
print(ch3)
print(ch3.lower()) # tous en minuscule

ch4 = ch2 + ch3 + " 2024"
print(ch4)

ch5 = ch3 * 4
print(ch5)




