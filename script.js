function cariObat() {
    let input = document.getElementById("namaObat").value.trim().toLowerCase();
    let hasilPencarian = document.getElementById("hasilPencarian");

    let obatDitemukan = databaseObat.find(obat => obat.nama.toLowerCase() === input);

    if (obatDitemukan) {
        hasilPencarian.innerHTML = `<b>${obatDitemukan.nama}:</b> ${obatDitemukan.fungsi}`;
    } else {
        hasilPencarian.innerHTML = "Obat tidak ditemukan. Coba lagi!";
    }
}

