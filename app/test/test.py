from app.tariffs import Tariff, TariffManager


def test_actual():
    test_manager = TariffManager()
    test_1_tariff = Tariff('Мой тариф 1', price=0, gb=0, hit=False, minutes=0, sms=0,
                           gb_unlim=None, minutes_unlim_tele2=False, archived=False)
    test_2_tariff = Tariff('Мой тариф 2', price=0, gb=0, hit=False, minutes=0, sms=0,
                           gb_unlim=None, minutes_unlim_tele2=False, archived=False)
    test_3_tariff = Tariff('Мой тариф 3', price=0, gb=0, hit=False, minutes=0, sms=0,
                           gb_unlim=None, minutes_unlim_tele2=False, archived=True)

    test_manager.add(test_1_tariff)
    test_manager.add(test_2_tariff)
    test_manager.add(test_3_tariff)

    expected = [test_1_tariff, test_1_tariff]
    actual = test_manager.actual()
    assert expected == actual


def test_archived():
    test_manager = TariffManager()
    test_1_tariff = Tariff('Мой тариф 1', price=0, gb=0, hit=False, minutes=0, sms=0,
                           gb_unlim=None, minutes_unlim_tele2=False, archived=False)
    test_2_tariff = Tariff('Мой тариф 2', price=0, gb=0, hit=False, minutes=0, sms=0,
                           gb_unlim=None, minutes_unlim_tele2=False, archived=False)
    test_3_tariff = Tariff('Мой тариф 3', price=0, gb=0, hit=False, minutes=0, sms=0,
                           gb_unlim=None, minutes_unlim_tele2=False, archived=True)

    test_manager.add(test_1_tariff)
    test_manager.add(test_2_tariff)
    test_manager.add(test_3_tariff)

    expected = [test_3_tariff]
    actual = test_manager.archived()
    assert expected == actual
