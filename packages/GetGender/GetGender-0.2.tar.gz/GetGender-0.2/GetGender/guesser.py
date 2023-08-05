from data import DATA


def get_gender(name: str) -> str:
    return DATA[name]


if __name__ == '__main__':
    print('Import this module in your script')