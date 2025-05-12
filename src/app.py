from flask import Flask
import sqlite3

app = Flask(__name__)

@app.route('/')
def home():
    conn = sqlite3.connect('veri.db')
    c = conn.cursor()
    c.execute("CREATE TABLE IF NOT EXISTS notlar (id INTEGER PRIMARY KEY, icerik TEXT)")
    c.execute("INSERT INTO notlar (icerik) VALUES ('Merhaba Docker Mini Proje')")
    conn.commit()
    c.execute("SELECT * FROM notlar")
    sonuc = c.fetchall()
    conn.close()
    return f"Veritabanı içerikleri: {sonuc}"

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
