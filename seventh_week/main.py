import json
import typing
from keyword import iskeyword


class JsonHandler:
    def __init__(self, data) -> None:
        self.data = dict(data)

        for key, attr in self.data.items():
            if iskeyword(key):
                key = f'{key}_'
            setattr(self, key, self.attr_handler(attr))

    def attr_handler(self, attr):
        if isinstance(attr, list):
            return [self.attr_handler(x) for x in attr]
        elif isinstance(attr, dict):
            return JsonHandler(attr)
        return attr


class ColorizeMixin():
    default = f'\033[1;{{}};40m'

    def __str__(self) -> str:
        super().__init_subclass__
        self.output = f'{self.default.format(self.repr_color_code)}{self.output}'


class Advert(ColorizeMixin, JsonHandler):
    repr_color_code = 36

    def __init__(self, data) -> None:
        super().__init__(data)
        if hasattr(self, 'price'):
            if int(self.price) < 0:
                raise ValueError('must be >= 0')
        else:
            self.price = 0
        if not hasattr(self, 'title'):
            raise ValueError('must be title')

    def __str__(self) -> str:
        self.output = ''
        for attr in self.__dict__['data'].values():
            if isinstance(attr, list) or isinstance(attr, dict):
                self.output += '| '
                self.output += f'{str(attr)} '
            elif isinstance(attr, JsonHandler):
                self.output += '| '
                self.output += f'{attr.__str__} '
            else:
                self.output += f'| {attr} '
        self.output += '|'
        super().__str__()
        return self.output


if __name__ == '__main__':
    lesson_str = """{
        "title": "python",
        "price": "1",
        "location": {
        "address": "город Москва, Лесная, 7",
        "class": ["Белорусская"]
        }
    }"""
    lesson = json.loads(lesson_str)
    lesson_ad = Advert(lesson)
    print(lesson_ad.location.class_)

    dog_str = """{
    "title": "Вельш-корги",
    "price": 1000,
    "class": "dogs"
    }"""
    dog = json.loads(dog_str)
    dog_ad = Advert(dog)
    # обращаемся к атрибуту `dog_ad.class_` вместо `dog_ad.class`
    print(dog_ad.class_)
