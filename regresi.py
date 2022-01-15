import numpy as np
from numpy.lib.ufunclike import fix

nilx = np.array([1.0, 1.5, 2.0, 2.5, 3.0])
nily = np.array([2.0, 3.2, 4.1, 4.9, 5.9])


# Hitung sigma xi dan yi
signilx = sum(nilx)
print("Sigma nilai xi = ", signilx)
sigmanilxi = signilx ** 2  # Sigma nilai xi dikuadratkan
signily = sum(nily)
print("Sigma nilai xi dikuadratkan = ", sigmanilxi)
print("Sigma nilai yi = ", signily)


# Hitung xi kuadrat dan yi kuadrat
kunilx = [num ** 2 for num in nilx]
sumkunilx = sum(kunilx)
print("Xi kuadrat = ", kunilx)
print("Sigma nilai xi masin-masing dikuadrat = ", sumkunilx)

# Hitung nil xi * nil yi dan sigmanya
cal = nilx * nily
sigmaxiyi = sum(cal)

print("Hasil kali nilai xi dan yi = ", cal)
print("hasil sigma xi * yi = ", sigmaxiyi)

# Nilai n
n = int(input("Masukkan jumlah data = "))

# Hitung b
b1 = n * sigmaxiyi - signilx * signily
b2 = n * sumkunilx - sigmanilxi
b = b1 / b2
print("Hasil dari b = ", b)

# Hitung a
a = signily / n - b * (signilx / n)
print("Hasil dari a = ", a)

# Hitung fx
print(f"Persamaan fx = {a} + {b}x")
