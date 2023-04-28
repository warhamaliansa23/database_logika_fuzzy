import mysql.connector

def mysql_connect():
    db = mysql.connector.connect(
        host="localhost",
        user="root",
        password="",
        database="fuzzy_db"
    )
    return db

def cek_selected(cek, value):
    if cek == value:
        return "selected=\"selected\""

def format_desimal(nn, des):
    return format(nn, f',.{des}f').replace(',', '.')

def get_namakelompok(id_kelompok):
    db = mysql_connect()
    cursor = db.cursor(dictionary=True)
    sql = f"SELECT * FROM tb_kelompok WHERE id='{id_kelompok}'"
    cursor.execute(sql)
    row = cursor.fetchone()
    cursor.close()
    db.close()
    return row['nama_kelompok']

def derajat_keanggotaan(nilai, bawah, tengah, atas):
    selisih = atas - bawah
    if nilai < bawah:
        DA = 0
    elif (nilai >= bawah) and (nilai <= tengah):
        if bawah <= 0:
            DA = 1
        else:
            DA = (nilai - bawah) / (tengah - bawah)
    elif (nilai > tengah) and (nilai <= atas):
        DA = (atas - nilai) / (atas - tengah)
    elif nilai > atas:
        DA = 0
    return DA

db = mysql_connect()
cursor_kriteria = db.cursor(dictionary=True)
kelompok = 1
sql_kelompok = f"SELECT * FROM tb_kriteria WHERE kelompok='{kelompok}'"
cursor_kriteria.execute(sql_kelompok)

print("""
    <table border='1' cellpadding='5' cellspacing='3'>
        <tr>
            <th><strong>NIK</strong></th>
            <th><strong>Nama Karyawan</strong></th>
""")

for row in cursor_kriteria.fetchall():
    print(f"<th><strong>{row['nama_kriteria']}</strong></th>")

kelompok = 2
sql_kelompok = f"SELECT * FROM tb_kriteria WHERE kelompok='{kelompok}'"
cursor_kriteria.execute(sql_kelompok)
for row in cursor_kriteria.fetchall():
    print(f"<th><strong>{row['nama_kriteria']}</strong></th>")

(sql_kelompok)
for row in cursor_kriteria.fetchall():
    print(f"<th><strong>{row['nama_kriteria']}</strong></th>")

kelompok = 3
sql_kelompok = f"SELECT * FROM tb_kriteria WHERE kelompok='{kelompok}'"
cursor_kriteria.execute(sql_kelompok)
for row in cursor_kriteria.fetchall():
    print(f"<th><strong>{row['nama_kriteria']}</strong></th>")
print("""
</tr>
""")

cursor_emp = db.cursor(dictionary=True)
sql = "SELECT * FROM tb_emp"
cursor_emp.execute(sql)

ux = {}

for row in cursor_emp:
    ux[row['id']] = {}
    for skor in row['skor'].split(","):
        temp = skor.split(":")
        ux[row['id']][int(temp[0])] = float(temp[1])

for key in ux:
    print(f"<tr><td>{key}</td><td>{ux[key][1]}</td>")
    sql_kelompok = "SELECT * FROM tb_kriteria WHERE kelompok='1'"
    cursor_kriteria.execute(sql_kelompok)
    y = 2
    for row in cursor_kriteria.fetchall():
        namakrit = row['nama_kriteria']
        skor = ux[key][y]
        m = int(row['poin1'])
        n = int(row['poin2'])
        o = int(row['poin3'])
        derajatm = derajat_keanggotaan(skor, m, n, o)

        print(f"<td>({format_desimal(skor,1)}|{m}, {n}, {o})")
        print(f"</td><td>{format_desimal(derajatm,2)}</td>")
        y += 1

    sql_kelompok = "SELECT * FROM tb_kriteria WHERE kelompok='2'"
    cursor_kriteria.execute(sql_kelompok)
    for row in cursor_kriteria.fetchall():
        namakrit = row['nama_kriteria']
        skor = ux[key][y]
        m = int(row['poin1'])
        n = int(row['poin2'])
        o = int(row['poin3'])
        derajatm = derajat_keanggotaan(skor, m, n, o)

        print(f"<td>({format_desimal(skor,1)}|{m}, {n}, {o})")
        print(f"</td><td>{format_desimal(derajatm,2)}</td>")
        y += 1

    sql_kelompok = "SELECT * FROM tb_kriteria WHERE kelompok='3'"
    cursor_kriteria.execute(sql_kelompok)
    for row in cursor_kriteria.fetchall():
        namakrit = row['nama_kriteria']
        skor = ux[key][y]
        m = int(row['poin1'])
        n = int(row['poin2'])
        o = int(row['poin3'])
        derajatm = derajat_keanggotaan(skor, m, n, o)

        print(f"<td>({format_desimal(skor,1)}|{m}, {n}, {o})")
        print(f"</td><td>{format_desimal(derajatm,2)}</td>")
        y += 1
    print("</tr>")

db.close()
