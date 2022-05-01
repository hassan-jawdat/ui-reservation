import sqlite3
class DBConnect:
    def __init__(self):
        self._db=sqlite3.connect("Reservation.db")
        self._db.row_factory=sqlite3.Row
        self._db.execute("create table if not exists Ticket(ID integer primary key autoincrement, Name text, Email Text, telefon text, Gender text, Comment text)")
        self._db.execute("create table if not exists Room(ID integer primary key autoincrement, IsAvailable bit, IsSingleRoom bit, StartDate date, EndDdate date)")
        self._db.commit()

    def Add(self,Name,Email,telefon,Gender,Comment):
        self._db.execute("insert into Ticket(Name,Email,telefon,Gender,Comment) values(?,?,?,?,?)",(Name,Email,telefon,Gender,Comment))
        self._db.commit()
        return "request is submitted"

    def ListRequest(self):
        cursor=self._db.execute("Select * from Ticket") 
        return cursor;
