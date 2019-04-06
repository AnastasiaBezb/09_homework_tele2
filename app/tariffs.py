# def is_archived(tariff):
#     return tariff.archived  # Duck Typing
#
#
# def is_actual(tariff):
#     return not tariff.archived
#
#
# def my_filter(func, items):  # в качестве func можем передавать имя любой функции
#     result = []
#     for item in items:
#         if func(item):  # вызов функции и проверка результата
#             result.append(item)
#     return result


class Tariff:
    """

    """

    def __init__(
            self,
            name,
            *,  # все остальные аргументы только keyword
            price=0,  # 0 - без абонентской платы
            price_period='month',  # я сам так придумал
            gb=0,  # -1 - безлимит (мы просто сами и сели договорились)
            minutes=0,
            sms=0,
            hit=False,
            gb_unlim=None,
            minutes_unlim_tele2=True,
            archived=False
    ):
        self.name = name
        self.price = price
        self.price_period = price_period
        self.gb = gb
        self.minutes = minutes
        self.sms = sms
        self.hit = hit
        self.gb_unlim = gb_unlim
        self.minutes_unlim_tele2 = minutes_unlim_tele2
        self.archived = archived


class TariffManager:
    def __init__(self):
        self.items = []

    def add(self, item):
        self.items.append(item)

    def actual(self):
        # фактически задача поиска:
        # archived == False
        return list(filter(lambda tariff: not tariff.archived, self.items))

    def archived(self):
        # archived == True
        # int('23') -> 23
        # list(iter) -> [...]
        # return my_filter(is_archived, self.items)
        # result = []
        # for item in self.items:
        #     if item.archived:  # вызов функции и проверка результата
        #         result.append(item)
        # return result
        # return list(filter(is_archived, self.items))  # передаём имя функции! вызывать будет сам filter
        # def is_archived(tariff): -> lambda tariff:
        #    return tariff.archived      tariff.archived
        return list(filter(lambda tariff: tariff.archived, self.items))  # передаём имя функции! вызывать будет сам filter
