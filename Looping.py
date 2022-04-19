
#Hernanda Anggara Putra
#191011401959
#05TPLM002
#TUGAS UTS KECERDASAN BUATAN

#for loop
ulang = 7

for i in range (ulang):
    print(f"loop ke-{1}")

#while loop
print("Program Bilangan Bulat 1 hingga x")
i = 1
x = int (input("Masukkan bilangan bulat x = "));

while i <= x:
    print(i);
    i=i+1;

#nested loop
for i in range(3):
    print("Perulangan Luar [i]= ", i)

    for j in range(10):
        print("Perulangan dalam [i,j] = ", str(i)+","+str(j))