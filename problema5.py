with open("caractere.txt","w")as f:
    s=input("dati sirul de caractere: ")
   
count = 0
vowels = set("aeiouAEIOU")
for letter in s:
    if letter in vowels:
        count += 1
print("Numarul de vocale")
print(count)