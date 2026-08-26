from flask import Flask, render_template, request, redirect, url_for, flash
# Importar los formularios creados en la carpeta forms
from forms.productos_form import ProductoForm
from forms.clientes_form import ClienteForm
from forms.proveedores_form import ProveedorForm
from forms.facturacion_form import FacturaForm

app = Flask(__name__)
app.config['SECRET_KEY'] = 'clave_secreta_dermopiel_2026'

# ==========================================
# RUTAS PRINCIPALES
# ==========================================

@app.route('/')
def index():
    usuario = "Carlos"
    return render_template('index.html', usuario=usuario)

@app.route('/productos')
def productos():
    servicios = [
        {"id": 1, "nombre": "limpieza facial profunda", "precio": 35.00, "disponible": True, "categoria": "Faciales"},
        {"id": 2, "nombre": "peeling quimico", "precio": 60.00, "disponible": False, "categoria": "Tratamientos Avanzados"},
        {"id": 3, "nombre": "masaje descontracturante", "precio": 45.00, "disponible": True, "categoria": "Corporales"},
        {"id": 4, "nombre": "podologia clinica", "precio": 25.00, "disponible": True, "categoria": "Cuidado Especial"}
    ]
    return render_template('productos.html', servicios=servicios)

@app.route('/clientes')
def clientes():
    return render_template('clientes.html')

@app.route('/proveedores')
def proveedores():
    return render_template('proveedores.html')

@app.route('/facturacion')
def facturacion():
    return render_template('facturacion.html')

# ==========================================
# RUTAS DE FORMULARIOS
# ==========================================

@app.route('/productos/nuevo', methods=['GET', 'POST'])
def crear_producto():
    form = ProductoForm()
    if form.validate_on_submit():
        flash('Producto guardado correctamente', 'success')
        return redirect(url_for('productos'))
    return render_template('productos_form.html', form=form, titulo="Registrar Producto")

@app.route('/clientes/nuevo', methods=['GET', 'POST'])
def crear_cliente():
    form = ClienteForm()
    if form.validate_on_submit():
        flash('Cliente guardado correctamente', 'success')
        return redirect(url_for('index'))
    return render_template('clientes_form.html', form=form, titulo="Registrar Cliente")

@app.route('/proveedores/nuevo', methods=['GET', 'POST'])
def crear_proveedor():
    form = ProveedorForm()
    if form.validate_on_submit():
        flash('Proveedor guardado correctamente', 'success')
        return redirect(url_for('index'))
    return render_template('proveedores_form.html', form=form, titulo="Registrar Proveedor")

@app.route('/facturacion/nueva', methods=['GET', 'POST'])
def crear_factura():
    form = FacturaForm()
    if form.validate_on_submit():
        flash('Factura generada correctamente', 'success')
        return redirect(url_for('index'))
    return render_template('facturacion_form.html', form=form, titulo="Nueva Factura")

# ==========================================
# INICIO DE LA APLICACIÓN (SIEMPRE AL FINAL)
# ==========================================
if __name__ == '__main__':
    app.run(debug=True)