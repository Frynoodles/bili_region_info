import time
import requests
import json
from datetime import datetime, timedelta
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


def get_region_data():
    day_to = datetime.today().strftime("%Y%m%d")
    day_from = (datetime.today() - timedelta(days=7)).strftime("%Y%m%d")
    f = open("./resources/region_data.json", "r", encoding="utf-8")
    regions = json.load(f)
    for main_region in regions:
        print(main_region["tid"], main_region["名称"])
        resp = requests.get(
            f'https://api.bilibili.com/x/web-interface/ranking/region?day=7&rid={main_region["tid"]}'
        )
        d = resp.json()
        if d["code"] == 0:
            main_region["hot_data"] = d["data"]
            main_region["hot_video_total_play"] = sum(
                [j["play"] for j in d["data"] if "play" in j]
            )  # 播放量
            main_region["hot_video_total_coins"] = sum(
                [j["coins"] for j in d["data"] if "coins" in j]
            )  # 硬币数
            main_region["hot_video_total_favorites"] = sum(
                [j["favorites"] for j in d["data"] if "favorites" in j]
            )  # 收藏数

        else:
            main_region["hot_data"] = {}
            main_region["hot_video_total_play"] = 0
            main_region["hot_video_total_coins"] = 0
            main_region["hot_video_total_favorites"] = 0
        resp.close()
        time.sleep(0.5)
        resp = requests.get(
            f'https://s.search.bilibili.com/cate/search?main_ver=v3&search_type=video&view_type=hot_rank&copy_right=-1&new_web_tag=1&order=click&cate_id={main_region["tid"]}&page=1&pagesize=30&time_from={day_from}&time_to={day_to}'
        )
        d2 = resp.json()
        if d2["code"] == 0:
            main_region["hot_video_nums_7"] = d2["numResults"]  # 7天内视频总数
        time.sleep(0.5)
    with open(f"./output/data_{day_to}.json", "w") as f:
        json.dump(regions, f)
    # 转换为Excel
    json_data = pd.read_json(f"./output/data_{day_to}.json")
    writer = pd.ExcelWriter(f"./output/data_{day_to}.xlsx")
    json_data.to_excel(writer, "Sheet1", index=False)
    writer.close()


def plot_data():
    # 读取Excel数据
    df = pd.read_excel(f'./output/data_{datetime.today().strftime("%Y%m%d")}.xlsx')
    # 设置字体
    plt.rcParams['font.family'] = ['SimHei']
    # 获取数据列
    x = df.iloc[:, 7]  # 横坐标（分区热门总播放数）
    y = df.iloc[:, 8]  # 纵坐标（分区热门总硬币数）
    names = df.iloc[:, 1]  # 分区

    # 绘制散点图
    plt.scatter(x, y, label="Data Points")

    # 添加数据点名称
    for i, txt in enumerate(names):
        plt.annotate(txt, (x[i], y[i]))

    # 拟合一条直线
    p_fit = np.polyfit(x, y, 1)
    f_line = np.poly1d(p_fit)

    # 绘制拟合线
    x_fit = np.linspace(x.min(), x.max(), 100)
    plt.plot(x_fit, f_line(x_fit), label="Fitted Line")

    # 设置图形标题和标签
    plt.title("2D Scatter Plot with Fitted Line")
    plt.xlabel("热门总播放数")
    plt.ylabel("热门总硬币数")
    plt.legend()

    # 显示图形
    plt.show()


if __name__ == "__main__":
    get_region_data()
    plot_data()
