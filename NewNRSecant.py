import numpy as np

# Mendefinisikan matriks A dan vektor b (Anda dapat mengubahnya sesuai kebutuhan)
A = np.array([[1, -1, 1],
              [2, 6, 0],
              [0, 6, 8]])

b = np.array([0, 12, 20])

# Mendefinisikan jumlah iterasi maksimum dan toleransi untuk konvergensi
max_iter = 1000
toleransi = 1e-6

# Minta pengguna untuk memilih metode
metode = int(input("Pilih metode:\n1. Newton-Raphson\n2. Secant\nMasukkan 1 atau 2: "))

if metode == 1:
    # Mendefinisikan tebakan awal untuk vektor solusi x_nr
    x_nr = np.zeros_like(b, dtype=float)
    
    # Metode Newton-Raphson
    print("Metode Newton-Raphson:")
    for i in range(max_iter):
        # Hitung residual untuk x_nr
        residual_nr = np.dot(A, x_nr) - b
        
        # Hitung matriks Jacobian (A)
        Jacobian = A
        
        # Hitung vektor pembaruan menggunakan rumus Newton-Raphson
        delta_x = np.linalg.solve(Jacobian, -residual_nr)
        
        # Perbarui x_nr untuk iterasi berikutnya
        x_nr = x_nr + delta_x  # Konversi eksplisit ke float
        
        # Cetak kemajuan untuk iterasi saat ini
        print(f"Iterasi {i + 1}:")
        print("x_nr:", x_nr)
        print("Residual:", residual_nr)
        
        # Periksa konvergensi
        if np.linalg.norm(delta_x) < toleransi:
            break

    print("\nSolusi yang Konvergen (Metode Newton-Raphson):", x_nr)

elif metode == 2:
    # Mendefinisikan tebakan awal untuk vektor solusi x_secant
    x0 = np.zeros_like(b)
    x1 = np.ones_like(b)
    
    # Metode Secant
    print("Metode Secant:")
    for i in range(max_iter):
        # Hitung residual untuk x0 dan x1
        residual0 = np.dot(A, x0) - b
        residual1 = np.dot(A, x1) - b
    
        # Hitung kemiringan secant (Jacobian perkiraan)
        kemiringan_secant = (residual1 - residual0) / (x1 - x0)
    
        # Hitung vektor pembaruan menggunakan metode secant
        delta_x = -residual1 / kemiringan_secant
    
        # Perbarui x0 dan x1 untuk iterasi berikutnya
        x0, x1 = x1, x1 + delta_x
    
        # Cetak kemajuan untuk iterasi saat ini
        print(f"Iterasi {i + 1}:")
        print("x_secant:", x1)
        print("Residual:", residual1)
    
        # Periksa konvergensi
        if np.linalg.norm(delta_x) < toleransi:
            break

    print("\nSolusi yang Konvergen (Metode Secant):", x1)

else:
    print("Pilihan tidak valid. Harap pilih 1 untuk Newton-Raphson atau 2 untuk metode Secant.")
