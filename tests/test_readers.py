from unittest.mock import Mock, patch

import pandas as pd
import pytest

from src.readers import reader_csv_file, reader_excel_file


@patch('pandas.read_csv')
def test_reader_csv_file(mock_data, csv_or_excel_file, result_reader_csv_or_excel_file):
    mock_data.return_value = pd.DataFrame(csv_or_excel_file)
    assert reader_csv_file('path') == result_reader_csv_or_excel_file


def test_reader_excel_file(csv_or_excel_file, result_reader_csv_or_excel_file):
    mock_data = Mock(return_value=pd.DataFrame(csv_or_excel_file))
    pd.read_excel = mock_data
    assert reader_excel_file('path') == result_reader_csv_or_excel_file
