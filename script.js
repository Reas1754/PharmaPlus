function cariObat() {
    let namaObat = document.getElementById("namaObat").value.toLowerCase();
    let hasil = document.getElementById("hasilPencarian");

    if (databaseObat[namaObat]) {
        hasil.innerHTML = `<strong>${namaObat}:</strong> ${databaseObat[namaObat]}`;
    } else {
        hasil.innerHTML = "Obat tidak ditemukan. Coba lagi!";
    }
}
