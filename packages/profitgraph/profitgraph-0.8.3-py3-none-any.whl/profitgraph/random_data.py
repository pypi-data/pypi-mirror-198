from random import randint
from tqdm import tqdm
import datetime

from . import db
from . import language as lg


class RandomData(db.DataBase):
    
    def __init__(self, LANGUAGE: str) -> None:
        self.LANGUAGE = LANGUAGE
        super().__init__(LANGUAGE)

    def randomize(self) -> None:
        """Used to create and save random data in data.json"""
        print(lg.randomize_msg_lang[self.LANGUAGE])
        year_step = int(input(lg.random_year_lang[self.LANGUAGE]))

        self.connect()
        self.create()

        for intyear in tqdm(range(2020, 2020 + year_step + 1)):
            for intmonth in range(1, 13):
                for intday in range(1, 32):
                    day = intday
                    cash = randint(0, 5000)
                    cashless = randint(0, 5000)
                    purchases = randint(0, 500)
                    self.insert_year(intyear)
                    self.insert_month(intmonth)
                    try:
                        datetime.date(intyear, intmonth, intday)
                    except ValueError:
                        continue
                    self.insert_day(day, intmonth, cash, cashless, purchases)
            self.commit()
        self.close()
        print(lg.success_random_data_lang[self.LANGUAGE])
