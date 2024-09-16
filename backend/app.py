from flask import Flask, request, jsonify
import psycopg2

app = Flask(__name__)

# Connect to PostgreSQL database
def get_db_connection():
    conn = psycopg2.connect(
        host="db-service",
        database="mydb",
        user="postgres",
        password="password"
    )
    return conn

@app.route('/api/data', methods=['POST'])
def add_data():
    data = request.json
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute('INSERT INTO users (name, email) VALUES (%s, %s)', 
                   (data['name'], data['email']))
    conn.commit()
    cursor.close()
    conn.close()
    return jsonify({'message': 'Data inserted successfully'}), 201

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5001)

