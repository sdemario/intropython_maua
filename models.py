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


    def save(self):
        if self.id:
            self._update()
        else:
            self._insert()


    def delete(self):
        if not self.id:
            return

        db = self.dbconn.cursor()

        stmt  = "DELETE FROM device WHERE id = ?"
        db.execute(stmt, (self.id,))

        self.dbconn.commit()


    def measures(self):
        db = self.dbconn.cursor()

        db.execute("SELECT * from MEASURE WHERE id_device = ? ", (self.id, ))

        res = []
        for row in db:
            mea = Measure(self.dbconn, self)

            mea.temperature = row[2]
            mea.device = self
            mea.humidity = row[3]
            mea.date = row[4]
            mea.latitude = row[5]
            mea.longitude = row[6]

            res.append(mea)

        return res



class Measure:
    def __init__(self, dbconn, device = None):
        self.id = 0
        self.device = device
        self.temperature = None
        self.humidity = None
        self.date = None
        self.latitude = None
        self.longitude = None

        self.dbconn = dbconn

    def load(self, id):
        db = self.dbconn.cursor()
        db.execute("SELECT * FROM measure WHERE id = ? ", (id, ))
        row = db.fetchone()

        if row:
            self.id = row[0]
            if not self.device:
                self.device = Device(self.dbconn)
                self.device.load(row[1])
            elif self.device.id != row[1]:
                self.device = Device(self.dbconn)
                self.device.load(row[1])
            self.temperature = row[2]
            self.humidity = row[3]
            self.date = row[4]
            self.latitude = row[5]
            self.longitude = row[6]


    def _insert(self):
        if not self.device:
            raise Exception("Atributo device vazio")

        db = self.dbconn.cursor()

        stmt  = "INSERT INTO measure (id_device, temperature, humidity, date, "
        stmt += "  latitude, longitude) "
        stmt += "   VALUES (?, ?, ?, ?, ?, ?)"

        db.execute(stmt,
            (self.device.id,
            self.temperature,
            self.humidity,
            self.date,
            self.latitude,
            self.longitude))

        self.id = db.lastrowid
        self.dbconn.commit()


    def save(self):
        if not self.id:
            self._insert()
