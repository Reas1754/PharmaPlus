from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

# 📌 Database Dummy: 50 Obat dan Fungsinya
data_obat = [
    {"nama": "Paracetamol", "fungsi": "Meredakan demam dan nyeri ringan"},
    {"nama": "Ibuprofen", "fungsi": "Mengurangi peradangan dan nyeri"},
    {"nama": "Amoxicillin", "fungsi": "Antibiotik untuk infeksi bakteri"},
    {"nama": "Cetirizine", "fungsi": "Mengobati alergi"},
    {"nama": "Omeprazole", "fungsi": "Mengatasi asam lambung berlebih"},
    {"nama": "Ranitidine", "fungsi": "Mengurangi produksi asam lambung"},
    {"nama": "Aspirin", "fungsi": "Mengurangi nyeri, demam, dan peradangan"},
    {"nama": "Loratadine", "fungsi": "Mengobati alergi"},
    {"nama": "Dexamethasone", "fungsi": "Obat antiinflamasi steroid"},
    {"nama": "Metformin", "fungsi": "Mengontrol kadar gula darah pada diabetes"},
    {"nama": "Simvastatin", "fungsi": "Menurunkan kadar kolesterol dalam darah"},
    {"nama": "Amlodipine", "fungsi": "Mengobati tekanan darah tinggi"},
    {"nama": "Captopril", "fungsi": "Mengatasi hipertensi dan gagal jantung"},
    {"nama": "Losartan", "fungsi": "Menurunkan tekanan darah tinggi"},
    {"nama": "Furosemide", "fungsi": "Diuretik untuk mengatasi edema"},
    {"nama": "Spironolactone", "fungsi": "Mengurangi retensi cairan"},
    {"nama": "Hydrochlorothiazide", "fungsi": "Diuretik untuk hipertensi"},
    {"nama": "Warfarin", "fungsi": "Mencegah pembekuan darah"},
    {"nama": "Clopidogrel", "fungsi": "Mencegah pembekuan darah setelah serangan jantung"},
    {"nama": "Digoxin", "fungsi": "Mengatasi gagal jantung dan aritmia"},
    {"nama": "Salbutamol", "fungsi": "Mengatasi asma dan sesak napas"},
    {"nama": "Budesonide", "fungsi": "Mengobati asma dan penyakit paru obstruktif kronik (PPOK)"},
    {"nama": "Fluticasone", "fungsi": "Mengatasi alergi dan gangguan pernapasan"},
    {"nama": "Prednisone", "fungsi": "Mengatasi peradangan dan gangguan autoimun"},
    {"nama": "Methylprednisolone", "fungsi": "Steroid untuk peradangan"},
    {"nama": "Diazepam", "fungsi": "Mengatasi kecemasan dan gangguan tidur"},
    {"nama": "Lorazepam", "fungsi": "Mengatasi kecemasan dan gangguan tidur"},
    {"nama": "Alprazolam", "fungsi": "Obat anti-kecemasan"},
    {"nama": "Fluoxetine", "fungsi": "Mengobati depresi dan gangguan kecemasan"},
    {"nama": "Sertraline", "fungsi": "Mengatasi depresi dan gangguan panik"},
    {"nama": "Risperidone", "fungsi": "Obat antipsikotik untuk skizofrenia"},
    {"nama": "Haloperidol", "fungsi": "Mengatasi gangguan psikotik"},
    {"nama": "Carbamazepine", "fungsi": "Mengontrol kejang epilepsi"},
    {"nama": "Valproic Acid", "fungsi": "Obat epilepsi dan gangguan bipolar"},
    {"nama": "Gabapentin", "fungsi": "Mengatasi nyeri saraf dan epilepsi"},
    {"nama": "Pregabalin", "fungsi": "Mengobati nyeri neuropatik"},
    {"nama": "Metronidazole", "fungsi": "Antibiotik untuk infeksi bakteri dan parasit"},
    {"nama": "Ciprofloxacin", "fungsi": "Antibiotik spektrum luas"},
    {"nama": "Doxycycline", "fungsi": "Mengobati infeksi bakteri"},
    {"nama": "Azithromycin", "fungsi": "Antibiotik untuk infeksi pernapasan"},
    {"nama": "Ketoconazole", "fungsi": "Antijamur untuk infeksi kulit"},
    {"nama": "Fluconazole", "fungsi": "Mengobati infeksi jamur"},
    {"nama": "Itraconazole", "fungsi": "Mengatasi infeksi jamur sistemik"},
    {"nama": "Aciclovir", "fungsi": "Mengobati infeksi virus herpes"},
    {"nama": "Oseltamivir", "fungsi": "Obat antivirus untuk flu"},
    {"nama": "Chlorpheniramine", "fungsi": "Antihistamin untuk alergi"},
    {"nama": "Diphenhydramine", "fungsi": "Obat alergi dan antihistamin"},
    {"nama": "Mebendazole", "fungsi": "Obat cacing untuk infeksi parasit"},
    {"nama": "Albendazole", "fungsi": "Mengobati infeksi cacing"},
]

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/search")
def search():
    query = request.args.get("q", "").lower()
    hasil = [obat for obat in data_obat if query in obat["nama"].lower()]
    return jsonify(hasil)

if __name__ == "__main__":
    app.run(debug=True)
