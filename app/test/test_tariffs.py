from app.tariffs import Tariff, TariffManager


def test_actual():
    test_manager = TariffManager()
    my_online = Tariff('Мой Онлайн', price=290, hit=True, gb=15,
                       gb_unlim=['vk', 'facebook', 'whatsapp', 'viber', 'instagram'], minutes=400)
    unlimited = Tariff('Безлимит', price=350, gb=-1, minutes=500, sms=50)
    classic = Tariff('Классический', minutes_unlim_tele2=False)
    infinitely_black = Tariff('Беспредельно черный', price=310, gb=30,
                              minutes=200, sms=200, minutes_unlim_tele2=False, archived=True)
    city = Tariff('сити', minutes_unlim_tele2=False, archived=True)

    test_manager.add(my_online)
    test_manager.add(unlimited)
    test_manager.add(classic)
    test_manager.add(infinitely_black)
    test_manager.add(city)

    expected = [my_online, unlimited, classic]
    actual = test_manager.actual()
    assert expected == actual


def test_archived():
    test_manager = TariffManager()
    my_online = Tariff('Мой Онлайн', price=290, hit=True, gb=15,
                       gb_unlim=['vk', 'facebook', 'whatsapp', 'viber', 'instagram'], minutes=400)
    unlimited = Tariff('Безлимит', price=350, gb=-1, minutes=500, sms=50)
    classic = Tariff('Классический', minutes_unlim_tele2=False)
    infinitely_black = Tariff('Беспредельно черный', price=310, gb=30,
                              minutes=200, sms=200, minutes_unlim_tele2=False, archived=True)
    city = Tariff('сити', minutes_unlim_tele2=False, archived=True)

    test_manager.add(my_online)
    test_manager.add(unlimited)
    test_manager.add(classic)
    test_manager.add(infinitely_black)
    test_manager.add(city)

    expected = [infinitely_black, city]
    actual = test_manager.archived()
    assert expected == actual
