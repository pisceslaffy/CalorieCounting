import streamlit as st

def hitung_bmr(jenis_kelamin, berat_kg, tinggi_cm, usia_tahun, tingkat_aktivitas):
    """Menghitung Basal Metabolic Rate (BMR) dan kebutuhan kalori harian.

    Args:
        jenis_kelamin (str): 'laki-laki' atau 'perempuan'.
        berat_kg (float): Berat badan dalam kilogram.
        tinggi_cm (float): Tinggi badan dalam sentimeter.
        usia_tahun (int): Usia dalam tahun.
        tingkat_aktivitas (str): Tingkat aktivitas (ringan, sedang, berat, sangat berat).

    Returns:
        tuple: Tuple berisi BMR (float) dan perkiraan kebutuhan kalori harian (float).
               Mengembalikan None jika jenis kelamin tidak valid.
    """
    if jenis_kelamin.lower() == 'laki-laki':
        bmr = 88.362 + (13.397 * berat_kg) + (4.799 * tinggi_cm) - (5.677 * usia_tahun)
    elif jenis_kelamin.lower() == 'perempuan':
        bmr = 447.593 + (9.247 * berat_kg) + (3.098 * tinggi_cm) - (4.330 * usia_tahun)
    else:
        return None, None

    if tingkat_aktivitas.lower() == 'ringan':
        kebutuhan_kalori = bmr * 1.2
    elif tingkat_aktivitas.lower() == 'sedang':
        kebutuhan_kalori = bmr * 1.375
    elif tingkat_aktivitas.lower() == 'berat':
        kebutuhan_kalori = bmr * 1.55
    elif tingkat_aktivitas.lower() == 'sangat berat':
        kebutuhan_kalori = bmr * 1.725
    else:
        kebutuhan_kalori = bmr * 1.2  # Default jika tingkat aktivitas tidak valid

    return bmr, kebutuhan_kalori

# Contoh Penggunaan (dapat dihapus atau dikomentari untuk Streamlit)
if __name__ == "__main__":
    jenis_kelamin_input = input("Masukkan jenis kelamin (laki-laki/perempuan): ")
    berat_input = float(input("Masukkan berat badan (kg): "))
    tinggi_input = float(input("Masukkan tinggi badan (cm): "))
    usia_input = int(input("Masukkan usia (tahun): "))
    tingkat_aktivitas_input = input("Masukkan tingkat aktivitas (ringan, sedang, berat, sangat berat): ")

    bmr_hasil, kebutuhan_hasil = hitung_bmr(jenis_kelamin_input, berat_input, tinggi_input, usia_input, tingkat_aktivitas_input)

    if bmr_hasil is not None:
        print(f"\nBasal Metabolic Rate (BMR) Anda adalah: {bmr_hasil:.2f} kalori.")
        print(f"Perkiraan kebutuhan kalori harian Anda adalah: {kebutuhan_hasil:.2f} kalori.")
    else:
        print("Jenis kelamin tidak valid.")
