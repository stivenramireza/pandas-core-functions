import pandas as pd
from matplotlib import pyplot as plt
from logger import logger


def main():
    df_temp: pd.DataFrame = pd.read_csv('temperature_yearly.csv')
    df_rain: pd.DataFrame = pd.read_csv('rain_yearly.csv')

    logger.info(df_temp)
    logger.info(df_rain)

    df_temp_f: pd.DataFrame = df_temp.query('Temperature > 0 & Temperature < 40')
    logger.info(df_temp_f)

    df_temp_f.plot.scatter(x='Year', y='Temperature', label='Temperature and Year')
    plt.show()

    df_rain_f: pd.DataFrame = df_rain.query('Rainfall > 0 & Rainfall < 6')
    logger.info(df_rain_f)

    df_rain_f.plot.scatter(x='Year', y='Rainfall', label='Rainfall and Year')
    plt.show()


if __name__ == "__main__":
    main()
