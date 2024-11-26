from database import get_db_connection

class Course:
    @staticmethod
    def get_all():
        conn = get_db_connection()
        cursos = conn.execute('SELECT * FROM course').fetchall()
        conn.close()
        return cursos

    @staticmethod
    def get_by_id(id):
        conn = get_db_connection()
        course = conn.execute('SELECT * FROM course WHERE id = ?', (id,)).fetchone()
        disciplines = conn.execute('''
            SELECT d.id, d.name 
            FROM discipline d
            INNER JOIN course_discipline cd ON cd.discipline_id = d.id
            WHERE cd.course_id = ?
        ''', (id,)).fetchall()
        conn.close()
        return {"course": course, "disciplines": disciplines}

    @staticmethod
    def create(name):
        conn = get_db_connection()
        conn.execute('INSERT INTO course (name) VALUES (?)', (name,))
        conn.commit()
        conn.close()

    @staticmethod
    def update(id, name):
        conn = get_db_connection()
        conn.execute('UPDATE course SET name = ? WHERE id = ?', (name, id))
        conn.commit()
        conn.close()

    @staticmethod
    def delete(id):
        conn = get_db_connection()
        conn.execute('DELETE FROM course_discipline WHERE course_id = ?', (id,))
        conn.execute('DELETE FROM course WHERE id = ?', (id,))
        conn.commit()
        conn.close()

    @staticmethod
    def update_disciplines(course_id, discipline_ids):
        conn = get_db_connection()
        conn.execute('DELETE FROM course_discipline WHERE course_id = ?', (course_id,))
        for discipline_id in discipline_ids:
            conn.execute(
                'INSERT INTO course_discipline (course_id, discipline_id) VALUES (?, ?)',
                (course_id, discipline_id)
            )
        conn.commit()
        conn.close()
