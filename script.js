document.getElementById("search-btn").addEventListener("click", cariObat);

function cariObat() {
    let query = document.getElementById("namaObat").value.trim().toLowerCase();
    let hasil = document.getElementById("hasilPencarian");

    if (query === "") {
        hasil.innerHTML = "Masukkan nama obat terlebih dahulu.";
        return;
    }

    let obatDitemukan = databaseObat.find(obat => obat.nama.toLowerCase() === query);

    if (obatDitemukan) {
        hasil.innerHTML = `<b>${obatDitemukan.nama}:</b> ${obatDitemukan.fungsi}`;
    } else {
        hasil.innerHTML = "Obat tidak ditemukan. Coba lagi!";
    }
}
