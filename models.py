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
