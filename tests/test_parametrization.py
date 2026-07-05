import pytest
from _pytest.fixtures import SubRequest

# тест test_numbers запустится 4 раза и проверит что число больше нуля
# 1, 2, 3, -1

@pytest.mark.parametrize('number', [1, 2, 3, -1])
def test_numbers(number: int) -> None:
    assert number > 0

@pytest.mark.parametrize('number, expected', [(1, 1), (2, 4), (3, 9)])
def test_several_numbers(number: int, expected: int) -> None:
    assert number ** 2 == expected

@pytest.mark.parametrize('os', ['macos', 'windows', 'linux', 'debian'])
@pytest.mark.parametrize('browser', ['chromium', 'webkt', 'firefox'])
def test_multiplication_of_numbers(os: str, browser: str) -> None:
    assert len(os + browser) > 0


@pytest.fixture(params=['chromium', 'webkt', 'firefox'])
def browser(request: SubRequest):
    return request.param

def test_open_browser(browser: str) -> None:
    print(f'Running on browser: {browser}')


@pytest.mark.parametrize("user", ["Alice", "Zara"])
class TestOperations:
    @pytest.mark.parametrize("account", ["Credit card", "Debit card"])
    def test_user_with_operations(self, user: str, account: str):
        print(f"User with operations: {user}")

    def test_user_without_operations(self, user: str):
        print(f"User without operations: {user}")

users = {
    "+70000000011": "User with money on bank account",
    "+70000000022": "User without money on bank account",
    "+70000000033": "User with operations on bank account"
}

@pytest.mark.parametrize(
    'phone_number',
    users.keys(),
    ids=lambda phone_number: f'{phone_number}: {users[phone_number]}'
)

def test_identifiers(phone_number: str):
    pass