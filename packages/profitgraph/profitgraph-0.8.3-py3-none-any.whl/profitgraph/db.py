import sqlite3
import calendar
import os

from . import language as lg


class DataBase:

    def __init__(self, LANGUAGE: str) -> None:
        self.LANGUAGE = LANGUAGE

    def connect(self) -> None:
        """Connects to the database file"""

        os.makedirs(os.path.dirname(__file__) + "\\Database", exist_ok=True)
        self.conn = sqlite3.connect(os.path.dirname(__file__) + "\\Database\\entries.sqlite")
        self.cur = self.conn.cursor()

    def create(self) -> None:
        """Create tables in database if they not exists"""

        self.cur.executescript("""
            CREATE TABLE IF NOT EXISTS years (
            id INTEGER NOT NULL PRIMARY KEY UNIQUE,
            year INTEGER NOT NULL UNIQUE
            );
            
            CREATE TABLE IF NOT EXISTS months (
            id INTEGER NOT NULL PRIMARY KEY UNIQUE,
            month TEXT UNIQUE
            );
            
            CREATE TABLE IF NOT EXISTS days (
            id INTEGER NOT NULL PRIMARY KEY UNIQUE,
            day INTEGER,
            cash REAL,
            cashless REAL,
            purchases INTEGER,
            month_id INTEGER,
            year_id INTEGER
            );
        """)

    def insert_day(self, day: str, month: str, cash: float, cashless: float, purchases: int) -> None:
        """Inserts day, month, year_id, cash, cashless and purchases to "days" table"""

        self.cur.execute("""INSERT INTO days (day, cash, cashless, purchases, month_id, year_id) 
                            VALUES (?, ?, ?, ?, ?, ?)""", (day, cash, cashless, purchases, month, self.year_id))

    def insert_month(self, month: str) -> None:
        """Inserts month id and month name in "months" table"""

        month_name = calendar.month_name[int(month)]
        self.cur.execute('INSERT OR IGNORE INTO months (id, month) VALUES (?, ?)', (month, month_name))

    def insert_year(self, year: str) -> None:
        """Inserts year in "years" table"""

        self.cur.execute('INSERT OR IGNORE INTO years (year) VALUES (?)', (year, ))
        self._take_year_id(year)

    def _take_year_id(self, year: str) -> None:
        year_data = self.cur.execute("SELECT years.id, years.year FROM years WHERE years.year = ?", (year, ))
        for year in year_data:
            self.year_id = year[0]

    def duplicate_check(self, period: str) -> bool:
        """Check if current period is not in Database"""

        duplicate = self.cur.execute("""SELECT days.day, days.month_id, days.year_id 
                                        FROM days 
                                        JOIN years 
                                        WHERE days.day = ? AND days.month_id = ?""", (period[8:], period[5:7]))
        for date in duplicate:
            if date[0] == int(period[8:]) and date[1] == int(period[5:7]) and date[2] == self.year_id:
                print(lg.date_already_in_DB[self.LANGUAGE])
                return True
        else:
            return False

    def take_last_period(self) -> str:
        """Takes last period from DB to show it while add data"""

        id = self.cur.execute("SELECT id FROM days ORDER BY id DESC LIMIT 1").fetchone()
        period = self.cur.execute("""SELECT days.day, days.month_id, years.year 
                                     FROM days 
                                     JOIN years 
                                     WHERE days.id = (?) 
                                     ORDER BY years.year DESC LIMIT 1""", id).fetchone()
        period = '-'.join([str(i) for i in period])
        return period

    def commit(self) -> None:
        """Commits changes to Database"""
        self.conn.commit()

    def close(self) -> None:
        """Close connection with Database"""
        self.cur.close()
        