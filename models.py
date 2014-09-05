class Device:
    def __init__(self, dbconn):
        self.id = 0
        self.name = None
        self.obs = None
        self.latitude = None
        self.longitude = None

        self.dbconn = dbconn


    def load(self, id):
        db = self.dbconn.cursor()
        db.execute("SELECT * FROM device WHERE id = ? ", (id, ))
        row = db.fetchone()

        if row:
            self.id = row[0]
            self.name = row[1]
            self.obs = row[2]
            self.latitude = row[3]
            self.longitude = row[4]


    def _insert(self):
        if not self.name:
            raise Exception("Atributo nome vazio")

        db = self.dbconn.cursor()

        stmt  = "INSERT INTO device (name, obs, latitude, longitude) "
        stmt += "   VALUES (?, ?, ?, ?)"

        db.execute(stmt,
            (self.name,
            self.obs,
            self.latitude,
            self.longitude))

        self.id = db.lastrowid
        self.dbconn.commit()


    def _update(self):
        db = self.dbconn.cursor()

        stmt  = "UPDATE device set "
        stmt += "    name = ?, "
        stmt += "    obs = ?, "
        stmt += "    latitude = ?, "
        stmt += "    longitude = ? "
        stmt += "WHERE "
        stmt += "    id = ? "

        db.execute(stmt,
            (self.name,
            self.obs,
            self.latitude,
            self.longitude,
            self.id))

        self.dbconn.commit()
