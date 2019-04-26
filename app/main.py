import os

import waitress
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

    @app.route('/')
    def index():
        actual = manager.actual()
        for item in actual:
            if item.price_period == 'month':
                item.price_period = 'месяц'
        archived = manager.archived()
        for item in archived:
            if item.price_period == 'month':
                item.price_period = 'месяц'

        return render_template('tariffs.html', actual=actual, archived=archived)

    @app.route('/tariffs')
    def actual_tariffs():
        actual = manager.actual()

        for item in actual:
            if item.price_period == 'month':
                item.price_period = 'месяц'
        return render_template('actual_tariffs.html', actual=actual)

    @app.route('/tariffs/archive')
    def archived_tariffs():
        archived = manager.archived()

        for item in archived:
            if item.price_period == 'month':
                item.price_period = 'месяц'
        return render_template('archived_tariffs.html', archived=archived)

    print(os.getenv('APP_ENV'))
    print(os.getenv('PORT'))
    if os.getenv('APP_ENV') == 'PROD' and os.getenv('PORT'):
        waitress.serve(app, port=os.getenv('PORT'))
    else:
        app.run(port=9876, debug=True)


if __name__ == '__main__':
    start()
