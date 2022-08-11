import pymysql
from app import app
from config import mysql
from flask import jsonify
from flask import flash, request


@app.route('/create', methods=['POST','GET'])
def create():
    try:
        _json = request.json
        _name = _json['name']
        _email = _json['email']
        _phone = _json['phone']

        
      
        if _name and _email and _phone:
            print("hellos")
            conn = mysql.connect()
            cursor = conn.cursor()
            sqlQuery = "INSERT INTO interns(name, email, phone) VALUES(%s,%s,%s)"
            data=(_name, _email, _phone)
            cursor.execute(sqlQuery,data)
            conn.commit()
            response = jsonify('Intern added successfully!!!')
            response.status_code= 200
            
            return response 
        else:
            return showMessage()

        
    except Exception as e:
        print(e)
    finally:
        cursor.close()  
        conn.close()

@app.route('/internsdata')
def internsdata():
    try:
        conn = mysql.connect()
        cursor = conn.cursor()
        cursor.execute("Select * from interns")
        internsrows = cursor.fetchall()
        response = jsonify(internsrows)
        response.status_code = 200
        return response
    except Exception as e:
        print(e)

    finally:
        cursor.close()
        conn.close()

@app.route('/internsdata/<int:i_id>')
def intern_details(i_id):
    print('salman')
    try:
        conn = mysql.connect()
        cursor = conn.cursor()
        cursor.execute("SELECT idinterns, name, email, phone FROM interns WHERE idinterns =%s", i_id)
        empRow = cursor.fetchone()
        respone = jsonify(empRow)
        respone.status_code = 200
        return respone
    except Exception as e:
        print(e)
    finally:
        cursor.close() 
        conn.close()

@app.route('/update', methods=['PUT'])
def update():
    try:
        _json = request.json
        _id = _json['idinterns']
        _name = _json['name']
        _email = _json['email']
        _phone = _json['phone']

        
      
        if _name and _email and _phone:
            
            conn = mysql.connect()
            cursor = conn.cursor()
            sqlQuery = "UPDATE interns SET name=%s, email=%s, phone=%s where idinterns=%s"
            data=(_name, _email, _phone,_id)
            cursor.execute(sqlQuery,data)
            conn.commit()
            response = jsonify('employ updated successfully!!!')
            response.status_code= 200
            return response 
        else:
            return showMessage()

        
    except Exception as e:
        print(e)
    finally:
        cursor.close()  
        conn.close()

@app.route('/delete', methods=['DELETE'])
def delete_intern(i_id):
    
    try:
        conn = mysql.connect()
        cursor = conn.cursor()
        cursor.execute("DELETE FROM interns WHERE idinterns=%s", i_id)
        conn.commit()
        response = jsonify('Employee deleted successfully!')
        response.status_code = 200
        return response
    except Exception as e:
        print(e)
    finally:
        cursor.close() 
        conn.close()






@app.errorhandler(404)
def showMessage(error=None):
    message = {
        'status': 404,
        'message': 'Record not found: ' + request.url,
    }
    respone = jsonify(message)
    respone.status_code = 404
    return respone



    





if __name__ == '__main__':
    app.run()