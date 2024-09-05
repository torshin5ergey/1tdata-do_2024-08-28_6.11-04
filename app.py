"""
app.py - Load CSV data, calculates avg salary, filter employees older than 30.
"""

import logging

import pandas as pd

log = logging.getLogger(__name__)


def load_dataframe_from_csv(filename):
    """"""
    try:
        dataframe = pd.read_csv(filename)
        return dataframe
    except FileNotFoundError:
        log.error("Error. File '%s' not found", filename)
    except Exception as e:
        log.error("Error. %s", e)
        return None

def calculate_avg(dataframe, column):
    """"""
    try:
        average = dataframe[column].mean()
        return average
    except KeyError:
        log.error("Error. Column '%s' doesn't exist", column)
    except Exception as e:
        log.error("Error. %s", e)
        return None

def get_employees_older_than(dataframe, age):
    """"""
    try:
        filtered_dataframe = dataframe[dataframe['age'] > age]
        return filtered_dataframe
    except Exception as e:
        log.error("Error. %s", e)
        return None


def main():
    logging.basicConfig(
        level=logging.INFO,
        format='%(message)s'
    )
    df = load_dataframe_from_csv('data.csv')
    if df is not None:
        avg_salary = calculate_avg(df, 'salary')
        log.info("Средняя зарплата сотрудников: %s\n", avg_salary)
        older_than_30 = get_employees_older_than(df, 30)
        log.info("Сотрудники старше 30 лет:\n %s", older_than_30)
    else:
        log.error("Canceled")

if __name__ == "__main__":
    main()
