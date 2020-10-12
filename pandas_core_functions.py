import pandas as pd
from matplotlib import pyplot as plt


def main():
    df_temp = pd.read_csv('temperature_yearly.csv')
    df_rain = pd.read_csv('rain_yearly.csv')

    print(df_temp)
    print(df_rain)

    df_temp.plot.scatter(x='Year', y='Temperature', label='Temperature and Year')
    plt.show()

    df_rain.plot.scatter(x='Year', y='Rainfall', label='Rainfall and Year')
    plt.show()


if __name__ == "__main__":
    main()
