import sympy as sp

# Fungsi untuk metode Newton-Raphson
def newtonR(f, x0):
    x = sp.symbols('x')
    df = sp.diff(f, x)
    e = 10**-6
    N = 100
    for i in range(N):
        f_x0 = f.subs(x, x0)
        print("Metode Newton-Raphson | Iterasi %d   | x0 = %f    | f(x0) = %f    " % (i, x0, f_x0))
        if abs(f_x0) < e:
            return x0, i
        df_x0 = df.subs(x, x0)
        if df_x0 == 0:
            print("Turunan nol pada Metode Newton-Raphson")
            return None
        x0 = x0 - f_x0 / df_x0
    print("Maksimum iterasi pada Metode Newton-Raphson")
    return x0, i

# Fungsi untuk metode Secant berdasarkan Metode Newton-Raphson
def secant(f, x0, x1):
    x = sp.symbols('x')
    e = 10**-6
    N = 100
    for i in range(N):
        f_x0 = f.subs(x, x0)
        f_x1 = f.subs(x, x1)
        print("Metode Secant | Iterasi %d   | x0 = %f    | f(x0) = %f    " % (i, x0, f_x0))
        if abs(f_x1) < e:
            return x1, i
        if abs(f_x0 - f_x1) < e:
            print("Metode Secant tidak konvergen")
            return None
        x2 = x1 - f_x1 * (x1 - x0) / (f_x1 - f_x0)
        x0, x1 = x1, x2

# Definisikan simbol 'x'
x = sp.symbols('x')

# Definisikan fungsi 'f'
f = x**2-4*x

# Meminta input pengguna untuk memilih metode
print("Pilih metode:")
print("1. Metode Newton-Raphson")
print("2. Metode Secant")
choice = int(input("Masukkan pilihan (1/2): "))

if choice == 1:
    # Set nilai tebakan awal untuk Metode Newton-Raphson
    x0_newton = float(input("Masukkan tebakan awal untuk Metode Newton-Raphson: "))
    
    # Hitung akar menggunakan Metode Newton-Raphson
    x_root_newton, iterasi_newton = newtonR(f, x0_newton)
    
    # Hasil untuk Metode Newton-Raphson
    print('Hasil Metode Newton-Raphson : ', x_root_newton)
    print('Dalam %d iterasi' % iterasi_newton)
elif choice == 2:
    # Set nilai tebakan awal untuk Metode Secant
    x0_secant = float(input("Masukkan tebakan awal x0 untuk Metode Secant: "))
    x1_secant = float(input("Masukkan tebakan awal x1 untuk Metode Secant: "))
    
    # Hitung akar menggunakan Metode Secant
    secant_result = secant(f, x0_secant, x1_secant)
    
    # Cetak hasil atau pesan jika Metode Secant tidak konvergen
    if secant_result is not None:
        x_root_secant, iterasi_secant = secant_result
        print('Hasil Metode Secant : ', x_root_secant)
        print('Dalam %d iterasi' % iterasi_secant)
else:
    print("Pilihan tidak valid. Pilih 1 untuk Metode Newton-Raphson atau 2 untuk Metode Secant.")
