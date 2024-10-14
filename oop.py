from flask import Flask, jsonify
from datetime import datetime

app = Flask(__name__)

# Buku class
class Buku:
    def __init__(self, judul, tahun, jumlah_halaman, bahan_material, diskon):
        self.judul = judul
        self.tahun = tahun
        self.jumlah_halaman = jumlah_halaman
        self.bahan_material = bahan_material
        self.diskon = diskon

    def get_judul(self):
        return self.judul

    def get_tahun(self):
        return self.tahun

    def get_jumlah_halaman(self):
        return self.jumlah_halaman

    def get_bahan_material(self):
        return self.bahan_material

    def get_diskon(self):
        return self.diskon

    def set_diskon(self, diskon):
        self.diskon = diskon

    def check_harga(self):
        harga = 0
        usia = datetime.now().year - self.tahun

        if usia <= 5:
            if self.jumlah_halaman <= 100:
                harga = 100000
            elif 100 < self.jumlah_halaman <= 500:
                harga = 300000
            else:
                harga = 500000
        elif 5 < usia <= 10:
            if self.jumlah_halaman <= 100:
                harga = 50000
            elif 100 < self.jumlah_halaman <= 500:
                harga = 150000
            else:
                harga = 250000
        else:
            harga = 10000

        return harga - (harga * self.diskon / 100)

# Komik class, inheriting Buku
class Komik(Buku):
    def __init__(self, judul, tahun, jumlah_halaman, bahan_material, diskon, is_colorful):
        super().__init__(judul, tahun, jumlah_halaman, bahan_material, diskon)
        self.is_colorful = is_colorful

    def get_is_colorful(self):
        return self.is_colorful

# Flask routes
@app.route('/buku', methods=['GET'])
def get_buku():
    buku = Buku("Calculus", 2024, 1000, "Kertas", 0)
    return jsonify({
        'judul': buku.get_judul(),
        'tahun': buku.get_tahun(),
        'jumlah_halaman': buku.get_jumlah_halaman(),
        'bahan_material': buku.get_bahan_material(),
        'diskon': buku.get_diskon(),
        'harga': buku.check_harga()
    })

@app.route('/komik', methods=['GET'])
def get_komik():
    komik = Komik("One Piece", 1998, 500, "Kertas", 0, True)
    return jsonify({
        'judul': komik.get_judul(),
        'tahun': komik.get_tahun(),
        'jumlah_halaman': komik.get_jumlah_halaman(),
        'bahan_material': komik.get_bahan_material(),
        'diskon': komik.get_diskon(),
        'harga': komik.check_harga(),
        'is_colorful': komik.get_is_colorful()
    })

if __name__ == '__main__':
    app.run(debug=True)
