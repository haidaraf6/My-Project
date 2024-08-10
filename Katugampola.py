import numpy as np

def katugampola_fourier(f, alpha, num_points=1000):
    """
    Transformasi Fourier Katugampola diskret dari fungsi f dengan parameter alpha.

    Parameters:
    f : function
        Fungsi yang akan ditransformasikan.
    alpha : float
        Parameter orde parsial dari transformasi.
    num_points : int
        Jumlah titik diskret dalam domain waktu dan frekuensi.

    Returns:
    array_like
        Hasil transformasi Fourier Katugampola untuk setiap nilai k.
    """
    if not (alpha > int(alpha) and alpha <= int(alpha) + 1):
        raise ValueError("Alpha harus berada di dalam interval (n, n+1] dengan n adalah bilangan bulat.")

    n = int(np.floor(alpha))
    large_value = 1e6  
    x_values = np.linspace(-large_value, large_value, num_points)
    k_values = np.linspace(-large_value, large_value, num_points)
    dx = x_values[1] - x_values[0]  # Asumsikan x_values memiliki jarak yang sama

    results = []
    for k in k_values:
        integrand = x_values**(alpha-n-1) * f(x_values) * np.exp(-1j * k * (x_values**(alpha-n) / (alpha-n)))
        result = np.sum(integrand) * dx  
        results.append(result / np.sqrt(2 * np.pi))

    return np.array(results), k_values
