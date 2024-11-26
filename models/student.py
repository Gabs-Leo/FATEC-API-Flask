from database import get_db_connection

class Student:
    @staticmethod
    def get_all():
        conn = get_db_connection()
        students = conn.execute('''
            SELECT a.*, c.name AS course_name 
            FROM student a
            LEFT JOIN course c ON a.course_id = c.id
        ''').fetchall()
        conn.close()
        return students

    @staticmethod
    def get_by_id(id):
        conn = get_db_connection()
        student = conn.execute('SELECT * FROM student WHERE id = ?', (id,)).fetchone()
        conn.close()
        return student

    @staticmethod
    def create(name, cpf, address, password, course_id):
        conn = get_db_connection()
        conn.execute(
            'INSERT INTO student (name, cpf, address, password, course_id) VALUES (?, ?, ?, ?, ?)',
            (name, cpf, address, password, course_id)
        )
        conn.commit()
        conn.close()

    @staticmethod
    def update(id, name, cpf, address, password, course_id):
        conn = get_db_connection()
        conn.execute(
            'UPDATE student SET name = ?, cpf = ?, address = ?, password = ?, course_id = ? WHERE id = ?',
            (name, cpf, address, password, course_id, id)
        )
        conn.commit()
        conn.close()

    @staticmethod
    def delete(id):
        conn = get_db_connection()
        conn.execute('DELETE FROM student WHERE id = ?', (id,))
        conn.commit()
        conn.close()
