from mealy_main import main, MealyError


def raises(method, error):
    output = None
    try:
        output = method()
    except Exception as e:
        assert type(e) == error
    assert output is None


def test():
    o = main()
    assert o.init() == 0
    assert o.type() == 2
    assert o.type() == 3
    assert o.init() == 4
    assert o.init() == 7
    assert o.type() == 2
    assert o.type() == 3
    assert o.init() == 4
    assert o.type() == 6
    assert o.init() == 8
    assert o.init() == 9
    o = main()
    assert o.type() == 1
    raises(lambda: o.init(), MealyError)
    assert o.type() == 3
    assert o.type() == 5
    raises(lambda: o.type(), MealyError)
