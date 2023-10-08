from src.utils import User
from src.work_file import Json_file


def get_user(player: User, count: int):
    """Запрос пользователя"""

    player.choice_site()  # выбор сайта
    player.get_request()  # запрос
    player.choice_city()  # выбор региона для поиска вакансий
    player.quantity_vacancies()  # количество вакансий

    print(f'\n{player}')

    player.api(count)


def get_repeat(player: User):
    """Повторяет запрос пользователя с проверкой на корректность запроса повтора"""

    while True:
        try:
            choice_user = int(input('\nХотите повторить запрос?\n1 - Да\n2 - Нет'))
            if choice_user == 1:
                get_user(player, 1)
            elif choice_user == 2:
                break
            else:
                raise ValueError
        except ValueError:
            print("Некорректный ввод")


def find_get(player: User):
    """Ищет дополнительный запрос пользователя"""

    while True:
        try:
            choice_user = int(input('\n1 - Да\n2 - Нет\nХотите найти ключевое слово в вакансиях?'))
            if choice_user == 1:
                data = input('Введите Ваш запрос: ')
                print(player.find_word(data))
            elif choice_user == 2:
                break
            else:
                raise ValueError
        except ValueError:
            print("Некорректный ввод")


def main():
    while input('Нажмите Enter, чтобы начать: ') != '':
        continue

    # Очистка файла
    f = open('vacancies.json', 'w')
    f.close()

    print('\nПриветствую Вас! Подготовим Ваш запрос по поиску вакансий.')

    player = User()

    get_user(player, 0)
    get_repeat(player)
    User.sort_all()
    find_get(player)

    if not Json_file.read_json():
        print('\nПо Вашему запросу ничего не найдено')
    else:
        print('\nСписок вакансий отсортированных по зарплате Вы можете посмотреть в файле - vacancies.json')
    print('\nХорошего дня!')


if __name__ == "__main__":
    main()
