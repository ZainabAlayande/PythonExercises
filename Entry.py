from datetime import date


class Entry_App:

    def __init__(self, title: str, body: str, id_number: int):
        self.title = title
        self.body = body
        self.id_number = id_number
        self.date = date.today()

    def set_title(self, title):
        self.title = title

    def get_title(self):
        return self.title

    def set_body(self, body):
        self.body = body

    def get_body(self):
        return self.body

    def get_date(self):
        return self.date

    def set_id_number(self, id_number):
        self.id_number = id_number

    def get_id_number(self):
        return self.id_number

    def __str__(self) -> str:
        return """
        =========================
        Id: {}
        Date/Time: {}
        
        Title: {}
        Body: {}
        =========================
        """.format(self.id_number, self.date, self.get_title(), self.get_body())


