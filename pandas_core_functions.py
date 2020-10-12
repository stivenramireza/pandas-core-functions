import pandas as pd
from matplotlib import pyplot as plt
from logger import logger
from typing import Tuple


def merge_data(df_1: pd.DataFrame, df_2: pd.DataFrame) -> None:
    df_outer: pd.DataFrame = pd.merge(df_1, df_2, on='Year', how='outer')
    logger.info(df_outer)
    df_inner: pd.DataFrame = pd.merge(df_1, df_2, on='Year', how='inner')
    logger.info(df_inner)


def filter_data(df_temp: pd.DataFrame, df_rain: pd.DataFrame) -> Tuple[pd.DataFrame, pd.DataFrame]:
    df_temp_f: pd.DataFrame = df_temp.query('Temperature > 0 & Temperature < 40')
    logger.info(df_temp_f)
    df_temp_f.plot.scatter(x='Year', y='Temperature', label='Temperature and Year')
    plt.show()

    df_rain_f: pd.DataFrame = df_rain.query('Rainfall > 0 & Rainfall < 6')
    logger.info(df_rain_f)
    df_rain_f.plot.scatter(x='Year', y='Rainfall', label='Rainfall and Year')
    plt.show()
    return df_temp_f, df_rain_f


def read_data(dataset_1: str, dataset_2: str) -> Tuple[pd.DataFrame, pd.DataFrame]:
    df_temp: pd.DataFrame = pd.read_csv(dataset_1)
    logger.info(df_temp)
    df_temp.plot.scatter(x='Year', y='Temperature', label='Temperature and Year')
    plt.show()

    df_rain: pd.DataFrame = pd.read_csv(dataset_2)
    logger.info(df_rain)
    df_rain.plot.scatter(x='Year', y='Rainfall', label='Rainfall and Year')
    plt.show()
    return df_temp, df_rain


def main():
    # Read data and plot
    df_temp, df_rain = read_data('temperature_yearly.csv', 'rain_yearly.csv')

    # Filter data and plot
    df_temp_f, df_rain_f = filter_data(df_temp, df_rain)

    # Merge data
    merge_data(df_temp_f, df_rain_f)


if __name__ == "__main__":
    main()
