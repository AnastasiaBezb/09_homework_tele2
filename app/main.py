# from flask import Flask, render_template, request, url_for, redirect
#
# from app.tariffs import Tariff, TariffManager
#
#
# def start():
#     app = Flask(__name__)
#
#     manager = TariffManager()
#
#     my_online = Tariff('Мой Онлайн', price=290, hit=True, gb=15,
#                        gb_unlim=['vk', 'facebook', 'whatsapp', 'viber', 'instagram'], minutes=400)
#     unlimited = Tariff('Безлимит', price=350, gb=-1, minutes=500, sms=50)
#     classic = Tariff('Классический', minutes_unlim_tele2=False)
#     infinitely_black = Tariff('Беспредельно черный', price=310, gb=30,
#                               minutes=200, sms=200, minutes_unlim_tele2=False, archived=True)
#     city = Tariff('сити', minutes_unlim_tele2=False, archived=True)
#
#     manager.add(my_online)
#     manager.add(unlimited)
#     manager.add(classic)
#     manager.add(infinitely_black)
#     manager.add(city)
#
#     @app.route('/tariffs')
#     def actual_tariffs():
#         actual = manager.actual()
#         for item in actual:
#             if item.price == 0:
#                 item.price = 'Без абонентской платы'
#                 item.price_period = ' '
#             else:
#                 item.price = item.price
#
#         for item in actual:
#             if item.gb == -1:
#                 item.gb = 'Безлимитный интернет'
#             if item.gb == 0:
#                 item.gb = ' '
#             else:
#                 item.gb = item.gb
#
#         for item in actual:
#             if item.minutes == 0:
#                 item.minutes = ' '
#             else:
#                 item.minutes = item.minutes
#         for item in actual:
#             if item.sms == 0:
#                 item.sms = ' '
#             else:
#                 item.sms = item.sms
#
#         for item in actual:
#             if item.hit == True:
#                 item.hit = 'Хит продаж'
#             else:
#                 item.hit = ' '
#
#         for item in actual:
#             if item.gb_unlim == None:
#                 item.gb_unlim = ' '
#             else:
#                 item.gb_unlim = item.gb_unlim
#
#         for item in actual:
#             if item.minutes_unlim_tele2 == True:
#                 item.minutes_unlim_tele2 = 'безлимит на Tele2 России'
#             else:
#                 item.minutes_unlim_tele2 = ' '
#
#         return render_template('actual_tariffs.html', actual=actual)
#
#     @app.route('/tariffs/archive')
#     def archived_tariffs():
#         archived = manager.archived()
#         for item in archived:
#             if item.price == 0:
#                 item.price = 'Без абонентской платы'
#                 item.price_period = ' '
#             else:
#                 item.price = item.price
#
#         for item in archived:
#             if item.gb == -1:
#                 item.gb = 'Безлимитный интернет'
#             if item.gb == 0:
#                 item.gb = ' '
#             else:
#                 item.gb = item.gb
#
#         for item in archived:
#             if item.minutes == 0:
#                 item.minutes = ' '
#             else:
#                 item.minutes = item.minutes
#         for item in archived:
#             if item.sms == 0:
#                 item.sms = ' '
#             else:
#                 item.sms = item.sms
#
#         for item in archived:
#             if item.hit == True:
#                 item.hit = 'Хит продаж'
#             else:
#                 item.hit = ' '
#
#         for item in archived:
#             if item.gb_unlim == None:
#                 item.gb_unlim = ' '
#             else:
#                 item.gb_unlim = item.gb_unlim
#
#         for item in archived:
#             if item.minutes_unlim_tele2 == True:
#                 item.minutes_unlim_tele2 = 'безлимит на Tele2 России'
#             else:
#                 item.minutes_unlim_tele2 = ' '
#
#         return render_template('archived_tariffs.html', archived=archived)
#
#     app.run(port=9872, debug=True)
#
#
# if __name__ == '__main__':
#     start()

from flask import Flask, render_template, request, url_for, redirect

from app.tariffs import Tariff, TariffManager


def start():
    app = Flask(__name__)

    manager = TariffManager()

    my_online = Tariff('Мой Онлайн', price=290, hit=True, gb=15,
                       gb_unlim=['vk', 'facebook', 'whatsapp', 'viber', 'instagram'], minutes=400)
    unlimited = Tariff('Безлимит', price=350, gb=-1, minutes=500, sms=50)
    classic = Tariff('Классический', minutes_unlim_tele2=False)
    infinitely_black = Tariff('Беспредельно черный', price=310, gb=30,
                              minutes=200, sms=200, minutes_unlim_tele2=False, archived=True)
    city = Tariff('сити', minutes_unlim_tele2=False, archived=True)

    manager.add(my_online)
    manager.add(unlimited)
    manager.add(classic)
    manager.add(infinitely_black)
    manager.add(city)

    @app.route('/tariffs')
    def index():
        actual = manager.actual()
        for item in actual:
            if item.price == 0:
                item.price = 'Без абонентской платы'
                item.price_period = ' '
            else:
                item.price = item.price
        return render_template('actual_tariffs.html', actual=actual)

    app.run(port=9876, debug=True)


if __name__ == '__main__':
    start()
