from database import get_db_connection

class Teacher:
    @staticmethod
    def get_all():
        conn = get_db_connection()
        professores = conn.execute('SELECT * FROM teacher').fetchall()
        conn.close()
        return professores

    @staticmethod
    def get_by_id(id):
        conn = get_db_connection()
        teacher = conn.execute('SELECT * FROM teacher WHERE id = ?', (id,)).fetchone()
        disciplines = conn.execute('''
            SELECT d.id, d.name
            FROM discipline d
            INNER JOIN teacher_discipline pd ON pd.discipline_id = d.id
            WHERE pd.teacher_id = ?
        ''', (id,)).fetchall()
        discipline_ids = [disciplina['id'] for disciplina in disciplines]
        conn.close()
        return {"teacher": teacher, "discipline_ids": discipline_ids}

    @staticmethod
    def create(name, phone, user, password):
        conn = get_db_connection()
        conn.execute(
            'INSERT INTO teacher (name, phone, user, password) VALUES (?, ?, ?, ?)',
            (name, phone, user, password)
        )
        conn.commit()
        conn.close()

    @staticmethod
    def update(id, name, phone, user, password):
        conn = get_db_connection()
        conn.execute(
            'UPDATE professores SET name = ?, phone = ?, user = ?, password = ? WHERE id = ?',
            (name, name, phone, user, password, id)
        )
        conn.commit()
        conn.close()

    @staticmethod
    def delete(id):
        conn = get_db_connection()
        conn.execute('DELETE FROM teacher_discipline WHERE teacher_id = ?', (id,))
        conn.execute('DELETE FROM teacher WHERE id = ?', (id,))
        conn.commit()
        conn.close()

    @staticmethod
    def update_discipline(teacher_id, discipline_ids):
        conn = get_db_connection()
        conn.execute('DELETE FROM teacher_discipline WHERE teacher_id = ?', (teacher_id,))
        for discipline_id in discipline_ids:
            conn.execute(
                'INSERT INTO teacher_discipline (teacher_id, discipline_id) VALUES (?, ?)',
                (teacher_id, discipline_id)
            )
        conn.commit()
        conn.close()
