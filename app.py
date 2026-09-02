import os
import sqlite3
from flask import Flask, render_template, request, redirect, url_for, flash
from forms.productos_form import ProductoForm
from forms.clientes_form import ClienteForm
from forms.proveedores_form import ProveedorForm
from forms.facturacion_form import FacturaForm

app = Flask(__name__)
app.config['SECRET_KEY'] = 'clave_secreta_dermopiel_2026'

# Función para conectar a la base de datos SQLite
def get_db_connection():
    conn = sqlite3.connect('dermopiel.db')
    conn.row_factory = sqlite3.Row
    return conn

# Función para crear la tabla automáticamente si no existe
def init_db():
    conn = get_db_connection()
    conn.execute('''
        CREATE TABLE IF NOT EXISTS productos (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nombre TEXT NOT NULL,
            precio REAL NOT NULL,
            stock INTEGER NOT NULL
        )
    ''')
    conn.commit()
    conn.close()

# Ejecutamos la función para crear la tabla al arrancar
init_db()

@app.route('/')
def index():
    usuario = "Carlos"
    return render_template('index.html', usuario=usuario)

# 1. Ruta única para ver los productos desde la base de datos
@app.route('/productos')
def ver_productos():
    conn = get_db_connection()
    cursor = conn.execute('SELECT * FROM productos')
    lista_productos = cursor.fetchall()
    conn.close()
    return render_template('productos.html', productos=lista_productos)

## 2. Ruta única para registrar un nuevo producto
@app.route('/productos/nuevo', methods=['GET', 'POST'])
def crear_producto():
    form = ProductoForm()
    if form.validate_on_submit():
        nombre = form.nombre.data
        precio = form.precio.data
        stock = form.stock.data
        
        conn = get_db_connection()
        conn.execute(
            'INSERT INTO productos (nombre, precio, stock) VALUES (?, ?, ?)',
            (nombre, float(precio), stock)  # 👈 AQUÍ CONVERTIMOS EL PRECIO A FLOAT
        )
        conn.commit()
        conn.close()
        
        flash('Producto guardado correctamente en la base de datos', 'success')
        return redirect(url_for('ver_productos'))
        
    return render_template('productos_form.html', form=form, titulo="Registrar Producto")
if __name__ == '__main__':
    app.run(debug=True)