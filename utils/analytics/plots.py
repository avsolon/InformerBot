import matplotlib.pyplot as plt
from io import BytesIO

def plot_to_buffer(plot_func):
    buf = BytesIO()
    plt.figure(figsize=(8, 5))
    plot_func()
    plt.tight_layout()
    plt.savefig(buf, format='png')
    buf.seek(0)
    plt.close()
    return buf


def plot_top_cities(top_cities):
    return plot_to_buffer(lambda: top_cities.plot(kind='bar', title="Топ городов"))


def plot_daily(daily):
    return plot_to_buffer(lambda: daily.plot(kind='line', marker='o', title="Активность"))


def plot_top_users(users):
    return plot_to_buffer(lambda: users.plot(kind='bar', title="Топ пользователей"))