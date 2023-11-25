from constraints.constraints import company_name_constraint
from constraints.constraints import total_attempts_reached
from constraints.constraints import extensions
from constraints.constraints import extension_error


class BaseFile:
    NAMES_MAP = {
            "087 6939779": "Дамян",
            "088 6811365": "Миленка",
            "088 8411150": "Меги",
            "089 2907007": "Пиле",
            "089 3047676": "Кака",
            "089 3461275": "Ива",
            "089 3461484": "Мими Бъни",
            "089 4466550": "Марти",
            "089 5564173": "Златка",
            "089 7005887": "Аз",
            "089 8559068": "Мими Бъни",
            "089 8559163": "Мими Бъни",
            "089 8559215": "Йонка",
            "089 8559241": "Мама",
            "089 8559326": "Зорница",
            "089 8559374": "леля Ани"
    }


    def __init__(self, username, company, path):
        self.username = username
        self.company = company
        self.path = path
        self.extension = path.split('.')[-1]

    @property
    def company(self):
        return self.__company

    @company.setter
    def company(self, value):
        if value not in company_name_constraint():
            print("Bills extractor 2.0 does not work this company! Please contact customer service")
        else:
            self.__company = value
            value_not_correct = False

    @property
    def extension(self):
        return self.__extension

    @extension.setter
    def extension(self, value):
        self.__extension = value