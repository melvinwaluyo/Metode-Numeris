def gauss_seidel(A, b, x0, tol, max_iter):
    n = len(A)
    x = x0.copy()
    iteration = 0
    while iteration < max_iter:
        print(f"Iterasi {iteration + 1}:")
        for i in range(n):
            # Hitung nilai xi baru menggunakan metode Gauss-Seidel
            new_xi = (b[i] - sum(A[i][j] * x[j] for j in range(n) if j != i)) / A[i][i]
            x[i] = new_xi
            print(f"x{i+1} = {new_xi:.6f}")
        
        # Hitung norma kesalahan
        error_norm = max(abs(x[i] - x0[i]) for i in range(n))
        print(f"Norma Kesalahan: {error_norm:.6f}")
        
        # Cek apakah sudah mencapai toleransi
        if error_norm < tol:
            print("Konvergen! Berhenti.")
            break
        
        x0 = x.copy()
        iteration += 1
    
    return x

# Matriks koefisien A
A = [[1, -1],
     [2, 6]]

# Vektor konstanta b
b = [-1.157895, 12]

# Tebakan awal x
x0 = [0, 0]

# Toleransi dan jumlah maksimum iterasi
tolerance = 1e-6
max_iterations = 100

# Panggil fungsi Gauss-Seidel untuk menyelesaikan sistem persamaan
result = gauss_seidel(A, b, x0, tolerance, max_iterations)
