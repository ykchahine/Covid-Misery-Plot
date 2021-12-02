#!/usr/bin/env python3
# Youssef Chahine
# CPSC 223p-03
# 2020-10-25
# ykchahine@csu.fullerton.edu
#
"""A program that takes in a JSON file plots three lines
   from unemployment rate, inflation rate, and misery from 1948 to 2020"""
import sys
import json
from datetime import datetime
import matplotlib.pyplot as plt
import matplotlib.lines as mlines


def simple_plot():
    """A function that takes in the JSON file
      and plots the lines using the datetime and matplotlib module"""
    if len(sys.argv) < 2:
        print("Not enough arguments provided. Exiting...")
        sys.exit()
    _f_ = sys.argv[1]
    with open(_f_, 'r') as _fp_:
        _d_ = json.load(_fp_)
    dates_list = []
    unemp_list = []
    inf_list = []
    misery_list = []

    for i in _d_['dataset_data']['data']:
        date = i[0]
        dates_list.append(date)
        unemp_rate = i[1]
        unemp_list.append(unemp_rate)
        inf_rate = i[2]
        inf_list.append(inf_rate)
        misery_rate = i[3]
        misery_list.append(misery_rate)
    dates_list = [datetime.strptime(_d_, "%Y-%m-%d") for _d_ in dates_list]
    fig, _ax_ = plt.subplots(figsize=(10, 10), constrained_layout=True)
    fig.suptitle('U.S Misery Index', fontsize=25)
    _ax_.set_xlim([datetime.strptime(str(1948), "%Y"),
                  datetime.strptime(str(2020), "%Y")])
    _ax_.plot(dates_list, unemp_list)
    line_2 = _ax_.plot(dates_list, inf_list)
    plt.setp(line_2, color='r', linestyle='--')
    line_3 = _ax_.plot(dates_list, misery_list)
    plt.setp(line_3, color='g', linestyle='dotted')
    label_1 = mlines.Line2D([], [], color='blue', markersize=15,
                            label='Unemployment rate')
    label_2 = mlines.Line2D([], [], color='red', markersize=15,
                            label='Inflation rate', linestyle='--')
    label_3 = mlines.Line2D([], [], color='green', markersize=15,
                            label='Misery rate', linestyle='dotted')
    _ax_.set(xlabel = "Dates", ylabel="Floating Point Values")
    _ax_.legend(title="Legend", handles=[label_1, label_2, label_3])
    fig.savefig("us_misery_plot.png")
    print("Writing plot to us_misery_plot.png")
    plt.close()


def main():
    """Calls simple_plot()"""
    simple_plot()


if __name__ == "__main__":
    main()
