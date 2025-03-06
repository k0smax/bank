import pandas as pd


def reader_csv_file(file_path: str) -> list:
    """
    Считывание данных из csv-файла
    :param file_path: путь до файла
    :return: список словарей
    """
    data_file = pd.read_csv(file_path, delimiter=";")
    # Изменяем тип данных в столбце 'id' на int
    data_file["id"] = data_file["id"].fillna(0).astype(int)
    data_file_to_dict = data_file.to_dict(orient="records")

    return data_file_to_dict


def reader_excel_file(file_path: str) -> list:
    """
    Считывание данных из excel-файла
    :param file_path: путь до файла
    :return: список словарей
    """
    data_file = pd.read_excel(file_path)
    # Изменяем тип данных в столбце 'id' на int
    data_file["id"] = data_file["id"].fillna(0).astype(int)
    data_file_to_dict = data_file.to_dict(orient="records")

    return data_file_to_dict


# if __name__ == '__main__':
# print(reader_csv_file('../data/transactions.csv'))
# print(reader_excel_file('../data/transactions_excel.xlsx'))
