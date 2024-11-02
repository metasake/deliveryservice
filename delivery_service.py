"""
Модуль для определения минимального количества транспортных платформ.

Минимум определяется необходимостью перевозки всех роботов с учётом
их весов и предельной грузоподъемности платформы, а также тем, что на
платформу помещается не более двух роботов одновременно.

Функции:
    - min_platforms_required(weights: list[int], limit: int) -> int:
        Определяет мин. кол-во платформ, требуемых для перевозки всех роботов.
    - read_input() -> tuple[list[int], int]:
        Считывает входные данные.
    - print_result(result: int) -> None:
        Выводит результат на консоль.
"""


def min_platforms_required(
    weights: list[int],
    platform_limit: int
) -> int:
    """
    Определи минимальное кол-во платформ, требуемых для перевозки всех роботов.

    :param weights: Список весов роботов.
    :param platform_limit: Максимальная грузоподъемность одной платформы.
    :return: Минимальное кол-во платформ, требуемых для перевозки всех роботов.
    """
    robot_weights = sorted(weights)
    min_platforms_count: int = 0
    left_pointer: int = 0
    right_pointer: int = len(robot_weights) - 1

    while left_pointer <= right_pointer:
        if (
            robot_weights[left_pointer] + robot_weights[right_pointer]
            <= platform_limit
        ):
            left_pointer += 1
        right_pointer -= 1
        min_platforms_count += 1

    return min_platforms_count


def read_input() -> tuple[list[int], int]:
    """
    Считай входные данные.

    :return weights: Список весов отдельных роботов.
    :return platform_limit: Предельная грузоподъемность платформы.
    """
    weights: list[int] = [int(weight) for weight in input().strip().split()]
    platform_limit: int = int(input())

    return weights, platform_limit


def print_result(result: int) -> None:
    """
    Выведи результат на консоль.

    :param result: Целое число, обозначающее минимальное количество платформ.
    :return: None
    """
    print(result)


if __name__ == '__main__':
    weights, platform_limit = read_input()
    print_result(min_platforms_required(weights, platform_limit))
