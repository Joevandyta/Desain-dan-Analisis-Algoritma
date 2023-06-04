import pandas as pd

#menu utama
def show_menu():
    print("=== TOKOSERBA ===")
    print("1. Tampilkan daftar barang")
    print("2. Sorting barang")
    print("3. Search barang")
    print("0. Keluar")
    print("=================")

# Fungsi untuk menampilkan daftar barang
def show_barang():
    try:
        df = pd.read_excel("tokoserba.xlsx")
        if len(df) == 0:
            print("Tidak ada data barang.")
        else:
            print("\n=== DAFTAR BARANG ===")
            num_records = len(df)
            max_records = int(
                input("Masukkan jumlah data yang ingin ditampilkan (0 untuk semua): "))

            print("{:<15} {:<15} {:<15} {:<15} {:<15}".format(
                "Nama", "Kategori", "Harga", "Tanggal Masuk", "Tanggal Kadaluarsa"))
            print("-" * 80)
            if max_records == 0 or max_records >= num_records:
                max_records = num_records

            for index, row in df.head(max_records).iterrows():
                nama = str(row['Nama Barang'])[:15]
                kategori = str(row['Kategori'])[:15]
                harga = str(row['Harga Barang'])[:15]
                tanggal_masuk = str(row['Tanggal Masuk'].date())[:15]
                tanggal_kadaluarsa = str(row['Tanggal Kadaluarsa'].date())[:15]
                print("{:<15} {:<15} {:<15} {:<15} {:<15}\n".format(
                    nama, kategori, harga, tanggal_masuk, tanggal_kadaluarsa))
            if max_records < num_records:
                print(
                    f"Tampilkan {max_records} dari total {num_records} data.\n")

    except FileNotFoundError:
        print("\nFile tokoserba.xlsx tidak ditemukan.\n")

#simpan ke excel
def save_to_excel(df):
    try:
        df.to_excel("tokoserba.xlsx", index=False)
        print("Data berhasil disimpan ke tokoserba.xlsx.")
    except:
        print("Terjadi kesalahan dalam menyimpan data.")

# Fungsi untuk melakukan Selection Sort
def selection_sort(df, column, ascending=True):
    for i in range(len(df)):
        min_max_index = i
        for j in range(i+1, len(df)):
            if ascending:
                if pd.isnull(df.iloc[j][column]) or (not pd.isnull(df.iloc[min_max_index][column]) and df.iloc[j][column] < df.iloc[min_max_index][column]):
                    min_max_index = j
            else:
                if pd.isnull(df.iloc[min_max_index][column]) or (not pd.isnull(df.iloc[j][column]) and df.iloc[j][column] > df.iloc[min_max_index][column]):
                    min_max_index = j
        if min_max_index != i:
            df.iloc[i], df.iloc[min_max_index] = df.iloc[min_max_index], df.iloc[i]
    return df

# Fungsi untuk melakukan Sorting berdasarkan harga barang
def sorting():
    sort_choice = input(
        "Masukkan pilihan sorting (1: Nama Barang, 2: Kategori, 3: Harga Barang, 4: Tanggal Masuk, 5: Tanggal Kadaluarsa): ")
    if sort_choice in ["1", "2", "3", "4", "5"]:
        try:
            df = pd.read_excel("tokoserba.xlsx")
            sort_order = input("Urutkan secara (A: Ascending, D: Descending): ")
            if sort_order.lower() == "a":
                sorted_df = selection_sort(df, df.columns[int(sort_choice)-1], ascending=True)
            elif sort_order.lower() == "d":
                sorted_df = selection_sort(
                    df, df.columns[int(sort_choice)-1], ascending=False)
            else:
                print("Pilihan urutan tidak valid.")
                return
            save_to_excel(sorted_df)
        except FileNotFoundError:
            print("File tokoserba.xlsx tidak ditemukan.")
    else:
        print("Pilihan sorting tidak valid.")

# Fungsi untuk melakukan Sequential Search
def sequential_search(df, column, keyword):
    results = []
    for index, row in df.iterrows():
        if keyword.lower() in str(row[column]). lower():
            results.append(row)
    return results

# Fungsi untuk mencari data
def search_data():
    try:
        df = pd.read_excel("tokoserba.xlsx")
        if len(df) == 0:
            print("Tidak ada data barang.")
        else:
            keyword = input("Masukkan kata kunci: ")
            search_choice = input(
                "Masukkan pilihan pencarian (1: Nama Barang, 2: Kategori, 3: Harga Barang, 4: Tanggal Masuk, 5: Tanggal Kadaluarsa): ")
            if search_choice in ["1", "2", "3", "4", "5"]:
                search_column = df.columns[int(search_choice)-1]
                results = sequential_search(df, search_column, keyword)
                if len(results) == 0:
                    print("Data tidak ditemukan.")
                else:
                    print("\n=== HASIL PENCARIAN ===")
                    print("{:<15} {:<15} {:<15} {:<15} {:<15}".format(
                        "Nama", "Kategori", "Harga", "Tanggal Masuk", "Tanggal Kadaluarsa"))
                    print("-" * 80)
                    for row in results:
                        nama = str(row['Nama Barang'])[:15]
                        kategori = str(row['Kategori'])[:15]
                        harga = str(row['Harga Barang'])[:15]
                        tanggal_masuk = str(row['Tanggal Masuk'].date())[:15]
                        tanggal_kadaluarsa = str(row['Tanggal Kadaluarsa'].date())[:15]
                        print("{:<15} {:<15} {:<15} {:<15} {:<15}\n".format(
                            nama, kategori, harga, tanggal_masuk, tanggal_kadaluarsa))
            else:
                print("Pilihan pencarian tidak valid.")

    except FileNotFoundError:
        print("File tokoserba.xlsx tidak ditemukan.")


# Fungsi utama
def main():
    while True:
        show_menu()
        choice = input("Masukkan pilihan menu (0-5): ")

        if choice == "1":
            show_barang()
            input()
        elif choice == "2":
            sorting()
            input()

        elif choice == "3":
            search_data()
            input()

        elif choice == "0":
            print("Terima kasih. Program selesai.")
            break
        else:
            print("Pilihan tidak valid. Silakan masukkan pilihan yang benar.\n")
            input()


if __name__ == "__main__":
    main()