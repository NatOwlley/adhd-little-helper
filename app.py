from flask import Flask, render_template, request, redirect, url_for
import mysql.connector

app = Flask(__name__)

# Настройки подключения к базе данных
db_config = {
    'user': 'root',
    'password': 'password',
    'host': 'localhost',
    'database': 'test'
}

@app.route('/')
def index():
    conn = mysql.connector.connect(**db_config)
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM entries")
    entries = cursor.fetchall()
    cursor.close()
    conn.close()
    return render_template('index.html', entries=entries)

@app.route('/add', methods=['POST'])
def add_entry():
    hours = request.form['hours']  # Часы
    minutes = request.form['minutes']  # Минуты
    text = request.form['text']  # Текст
    
    # Форматируем время в HH:MM
    time = f"{int(hours):02}:{int(minutes):02}"
    
    conn = mysql.connector.connect(**db_config)
    cursor = conn.cursor()
    cursor.execute("INSERT INTO entries (time, text) VALUES (%s, %s)", (time, text))
    conn.commit()
    cursor.close()
    conn.close()
    return redirect(url_for('index'))

@app.route('/delete/<int:id>')
def delete_entry(id):
    conn = mysql.connector.connect(**db_config)
    cursor = conn.cursor()
    cursor.execute("DELETE FROM entries WHERE id = %s", (id,))
    conn.commit()
    cursor.close()
    conn.close()
    return redirect(url_for('index'))

@app.route('/edit/<int:id>', methods=['POST'])
def edit_entry(id):
    hours = request.form['hours']  # Часы
    minutes = request.form['minutes']  # Минуты
    text = request.form['text']  # Текст
    
    # Форматируем время в HH:MM
    time = f"{int(hours):02}:{int(minutes):02}"
    
    conn = mysql.connector.connect(**db_config)
    cursor = conn.cursor()
    cursor.execute("UPDATE entries SET time = %s, text = %s WHERE id = %s", (time, text, id))
    conn.commit()
    cursor.close()
    conn.close()
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)