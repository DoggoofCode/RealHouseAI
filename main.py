from models import LinearRegressionModel, save_model, process_data


def remove_duplicates(data: list) -> list:
    return list(set(data))


def GetInput(depth=None, msg=None) -> list[str]:
    user_input = input(f"{f"({depth})" if depth else ""}{f"<{msg}" if msg else ">"}>")

    # find strings in the input
    start_index, end_index = getControlCharacters('"', user_input)
    max_split_range = (0, len(user_input))

    _ = []
    for value in start_index:
        _.append(value - 1)
        _.append(value)
    start_index = _

    _ = []
    for value in end_index:
        _.append(value)
        _.append(value + 1)
    end_index = _

    additional_list = [0, len(user_input) - 1]
    total_index = sorted(start_index + end_index + additional_list)

    # Bound the list to the max_split_range
    for index, value in enumerate(total_index):
        if value < max_split_range[0]:
            total_index[index] = max_split_range[0]
        elif value > max_split_range[1]:
            total_index[index] = max_split_range[1]

    final_list = remove_duplicates(total_index)
    final_list = sorted(final_list)

    # Split the string
    split_string = []
    for index in range(0, len(final_list) - 1, 2):
        split_string.append(user_input[final_list[index]:final_list[index + 1]])
    print(split_string)

    return split_string

def getControlCharacters(char: str, string: str) -> tuple[list, list]:
    start = []
    end = []
    for index, letter in enumerate(string):
        if letter == char:
            if len(start) <= len(end):
                start.append(index)
            elif len(start) > len(end):
                end.append(index)

    if len(start) != len(end):
        raise Exception(f"Unbalanced control characters, {start} and {end}")
    if len(start) == len(end):
        return start, end


def RunInfiniteConsole():
    running = True
    # while running:
    user_input = GetInput()


def main() -> None:
    RunInfiniteConsole()


if __name__ == '__main__':
    main()
