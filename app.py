from flask import Flask, render_template, request
import sqlite3

app = Flask(__name__)

def get_db_connection():
    conn = sqlite3.connect('data.db')  
    conn.row_factory = sqlite3.Row
    return conn

@app.route('/', methods=['GET', 'POST'])
def index():
    tables = ['customer', 'customer_order', 'order_detail', 'product'] #choix des tables a mettre apres
    
    if request.method == 'POST': #utilisation de la methode POST et GET 
        
        selected_table = request.form['table']
        conn = get_db_connection()
        query = f'SELECT * FROM {selected_table} LIMIT 50'
        rows = conn.execute(query).fetchall()
        conn.close() 
        
        return render_template('index.html', tables=tables, rows=rows, selected_table=selected_table)
    
    return render_template('index.html', tables=tables, rows=None)

if __name__ == '__main__':
    app.run(debug=True)

