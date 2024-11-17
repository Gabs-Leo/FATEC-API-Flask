from database import get_db_connection

class Discipline:
    @staticmethod
    def get_all():
        conn = get_db_connection()
        disciplinas = conn.execute('SELECT * FROM discipline').fetchall()
        conn.close()
        return disciplinas

    @staticmethod
    def get_by_id(id):
        conn = get_db_connection()
        disciplina = conn.execute('SELECT * FROM discipline WHERE id = ?', (id,)).fetchone()
        conn.close()
        return disciplina

    @staticmethod
    def create(name, hours):
        conn = get_db_connection()
        conn.execute('INSERT INTO discipline (name, hours) VALUES (?, ?)', (name, hours))
        conn.commit()
        conn.close()

    @staticmethod
    def update(id, name, hours):
        conn = get_db_connection()
        conn.execute('UPDATE discipline SET name = ?, hours = ? WHERE id = ?', (name, hours, id))
        conn.commit()
        conn.close()

    @staticmethod
    def delete(id):
        conn = get_db_connection()
        conn.execute('DELETE FROM discipline WHERE id = ?', (id,))
        conn.commit()
        conn.close()