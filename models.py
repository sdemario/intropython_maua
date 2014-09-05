class Device:
    def __init__(self, dbconn):
        self.id = 0
        self.name = None
        self.obs = None
        self.latitude = None
        self.longitude = None

        self.dbconn = dbconn
