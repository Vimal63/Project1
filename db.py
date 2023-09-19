import sqlite3

class database:
    def __init__(self, db):
        self.con = sqlite3.connect(db)
        self.cur = self.con.cursor()
        sql = """create table if not exists employees(
            id integer primary key,
            name text,
            age text,
            doj text,
            email text,
            gender text,
            contact text,
            address text
        ) """
        self.cur.execute(sql)
        self.con.commit()

    def insert(self, name, age, doj, email, gender, contact, address):
        self.cur.execute("insert into employees values(null,?,?,?,?,?,?,?)",
                         (name, age, doj, email, gender, contact, address))
        self.con.commit()

    def fetch(self):
        self.cur.execute("select * from employees")
        rows = self.cur.fetchall()
        return rows

    def remove(self, id):
        self.cur.execute("delete from employees where id=?", (id,))
        self.con.commit()

    def update(self, id, name, age, doj, email, gender, contact, address):
        self.cur.execute("update employees set name=?, age=?, doj=?, email=?, gender=?, contact=?, address=? where id=?",
                         (name, age, doj, email, gender, contact, address, id))
        self.con.commit()

#
# o = database("employees.db")
# o.insert("ram", "25", "12-12-2020", "balaji@123", "male", "9677675839", "35 main road")
# o.fetch()

