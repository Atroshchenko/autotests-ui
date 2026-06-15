# распознаётся pytest-ом как тест потому что название начинается с test
# это правило определено в файле pytest.ini
# функция no_test не распознаётся как тест потому что название не соответсвует паттерну

def test_user_login():
    print('Hello!')

class TestUserLogin:
    def test_1(self):
        ...
    def test_2(self):
        ...

    def no_test3(self):
        ...
# в тестах не должно быть __init__ конструкторов
#    def __init__(self):
#        ...

def test_assert_positive_case():
    assert (2 + 2) == 4

def test_assert_negative_case():
    assert (2 + 2) == 5, "2 + 2 != 5"