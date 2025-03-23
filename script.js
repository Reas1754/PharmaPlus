document.addEventListener("DOMContentLoaded", function () {
    console.log("Script berjalan...");

    document.getElementById("search-btn").addEventListener("click", searchObat);
    document.getElementById("search").addEventListener("keypress", function (event) {
        if (event.key === "Enter") {
            searchObat();
        }
    });
});

function searchObat() {
    let query = document.getElementById("search").value.trim().toLowerCase();
    console.log("Pencarian:", query);

    let resultDiv = document.getElementById("results");

    if (query === "") {
        resultDiv.innerHTML = "<p class='not-found'>Masukkan nama obat terlebih dahulu.</p>";
        return;
    }

    if (typeof databaseObat === "undefined") {
        console.error("databaseObat tidak terdeteksi!");
        resultDiv.innerHTML = "<p class='not-found'>Data obat tidak ditemukan.</p>";
        return;
    }

    let hasil = databaseObat.filter(obat => obat.nama.toLowerCase().includes(query));
    console.log("Hasil pencarian:", hasil);

    resultDiv.innerHTML = "";
    if (hasil.length === 0) {
        resultDiv.innerHTML = "<p class='not-found'>Obat tidak ditemukan.</p>";
    } else {
        hasil.forEach(obat => {
            resultDiv.innerHTML += `<p class="result-item"><b>${obat.nama}</b>: ${obat.fungsi}</p>`;
        });
    }
}
