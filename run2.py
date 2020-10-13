from flask import *
from functools import wraps
import sqlite3
import time
import pandas as pd



DATABASE = 'dataweb.db'

app = Flask(__name__)
app.secret_key = 'mysecretkey'
app.config.from_object(__name__)

def connect_db():
    con = sqlite3.connect('dataweb.db')
    cursor = con.cursor()
    print('La base funcionò bien')

def run_query(query='',parameters=()):
    conn = sqlite3.connect('dataweb.db')
    cursor = conn.cursor()                 # Crear un cursor
    cursor.execute(query, parameters)                  # Ejecutar una consulta
    if query.upper().startswith('SELECT'):
       data= cursor.fetchall()               # Traer los resultados de un select
       
    else:
        conn.commit()                          # Hacer efectiva la escritura de datos
        data = None
         
    #cursor.close()                         # Cerrar el cursor
    #conn.close()                           # Cerrar la conexión
    #conn.close()                           # Cerrar la conexión
    
    return data





@app.route('/')
def index():

    #query = 'SELECT * FROM datosclientes'
    #curs  = run_query(query)
    #return render_template('index_desa.html', contacts = curs)
     return render_template('layout1.html')
     

@app.route('/crear')
def crear():
    return render_template('crear.html')

@app.route('/crear_datos', methods = ['POST'])
def crear_datos():
      
    if request.method == 'POST':

        fullname = request.form['fullname']
        email = request.form['email']

        query1 = "SELECT count(*) FROM datosclientes WHERE fullname ='%s'  or email ='%s'" % (fullname,email)
        result1 = run_query(query1)
        result2 = list(result1[0])
        #print(result2[0])  
        
        if result2[0] > 0:
            flash ('Existe El Contacto y/o El E-mail')
            return redirect(url_for('index'))
        else:
            query = "INSERT INTO datosclientes (fullname,email) VALUES ('%s','%s')" % (fullname,email)
            result = run_query(query)
            flash ('Contacto agregado exitosamente')
            return redirect(url_for('index'))
        
        

@app.route('/modificar')
def modificar():
    
    query = "select fullname from datosclientes"
    result = run_query(query)
    print(result)

    return render_template('modificar.html',contacts= result,var2= '')



@app.route('/modificar_mod', methods = ['POST'])
def actualizar_mod():

    if request.method == 'POST':

        nombre = request.form['select']
        
        query1 = "SELECT * FROM datosclientes WHERE fullname ='%s'" % (nombre)
        result1 = run_query(query1)
        result2 = list(result1)
        print(result2)  
        print(result2[0])
        #print(result2[1])
        #return redirect(url_for('index'))
        return render_template('modificar.html',contacts= result2, var2=result2[0] )


@app.route('/actualizar_cont', methods = ['POST'])
def actualizar_cont():

    if request.method == 'POST':
        
        try:
            nombre = request.form['select']
            nombre1 = request.form['nombre']
            email = request.form['email']
        
            query1 = "update datosclientes set fullname='%s', email = '%s' where fullname = '%s'" % (nombre1,email,nombre)
            result1 = run_query(query1)
            #result2 = list(result1)
            #print(result2)  
            #print(result2[0])
            flash ('Contacto modificado exitosamente')
            return redirect(url_for('index'))

        except Exception as identifier:
            flash ('Existe el registro Contacto y/o email')
            return redirect(url_for('index'))
            pass
        


@app.route('/eliminar')
def eliminar():

    query = "select fullname from datosclientes"
    result = run_query(query)
    print(result)

    return render_template('eliminar.html',contacts= result)


@app.route('/eliminar_reg',methods = ['POST'])
def eliminar_reg():

    if request.method == 'POST':

            nombre = request.form['select']
        
            query1 = "delete from datosclientes where fullname ='%s'" % (nombre)
            result1 = run_query(query1)
            flash ('Contacto eliminado exitosamente')
            return redirect(url_for('index'))



@app.route('/consultar')
def consultar():

    query = 'SELECT * FROM datosclientes'
    curs  = run_query(query)
    return render_template('consultar.html', contacts = curs)
    


@app.route('/Grafico_Usuarios')
def grafico():

    query = "SELECT id,substr(date,0,8) as date,count(*) as 'cantidad' from History_user  group by id,substr(date,0,8)"
    curs  = run_query(query)

    dates = []
    prices = []

    for x in curs:
        dates.append(x[1])
        prices.append(x[2])

    #print (dates)
    #print (prices)

    return render_template('grafico_usuarios.html', title='Inicio', dates=dates, prices=prices)



@app.route('/home')
def filtro():

    user = request.args.get('user', 'all')
    #month = request.args.get('month', 'all')

    if user != 'all':

         query = "SELECT id,substr(date,0,8) as date,count(*) as 'cantidad' from History_user   where id = '%s' group by id,substr(date,0,8)" % (user)
         curs  = run_query(query)

    else:
    
         query = "SELECT id,substr(date,0,8) as date,count(*) as 'cantidad' from History_user  group by id,substr(date,0,8)"
         curs  = run_query(query)


    dates = []
    prices = []

    for x in curs:
        dates.append(x[1])
        prices.append(x[2])

    print (dates)
    print (prices)

    return render_template('grafico_usuarios.html', title='Inicio', dates=dates, prices=prices)




if __name__ == '__main__':
    app.run(port = 3000, debug=True)





#connect_db()
#index()
#run_query()