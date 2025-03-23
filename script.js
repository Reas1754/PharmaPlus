function cariObat() {
    let input = document.getElementById("search").value.trim().toLowerCase();
    let hasil = databaseObat.find(obat => obat.nama.toLowerCase() === input);

    if (hasil) {
        document.getElementById("result").innerText = hasil.fungsi;
    } else {
        document.getElementById("result").innerText = "Obat tidak ditemukan. Coba lagi!";
    }
}
