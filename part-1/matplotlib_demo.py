#!/usr/bin/env python3
# Youssef Chahine
# CPSC 223p-03
# 2020-10-23
# ykchahine@csu.fullerton.edu
#
# Examples taken from various gallery items at
# https://matplotlib.org/gallery
""" A program that prints out a series of
    graphs and plots"""

import matplotlib.pyplot as plt
import numpy as np
import matplotlib.dates as mdates
from datetime import datetime
from time import sleep


def fill_between_demo():
    """Fills between subplots"""
    # https://matplotlib.org/3.1.0/
    # gallery/lines_bars_and_markers/fill_between_demo.html
    # fill_between_demo.py
    _x_ = np.arange(0.0, 2, 0.01)
    _y1_ = np.sin(2 * np.pi * _x_)
    _y2_ = 1.2 * np.sin(4 * np.pi * _x_)

    ##########################################################################

    fig, (ax1, ax2, ax3) = plt.subplots(3, 1, sharex=True)

    ax1.fill_between(_x_, 0, _y1_)
    ax1.set_ylabel('between _y1_ and 0')

    ax2.fill_between(_x_, _y1_, 1)
    ax2.set_ylabel('between _y1_ and 1')

    ax3.fill_between(_x_, _y1_, _y2_)
    ax3.set_ylabel('between _y1_ and _y2_')
    ax3.set_xlabel('x')
    fig.savefig("a.png")
    plt.close()

    #####################################################################
    # Now fill between y1 and _y2_ where a logical condition is met.  Note
    # this is different than calling
    # ``fill_between(x[where], y1[where], _y2_[where] ...)``
    # because of edge effects over multiple contiguous regions.

    fig, (_ax_, ax1) = plt.subplots(2, 1, sharex=True)
    _ax_.plot(_x_, _y1_, _x_, _y2_, color='black')
    _ax_.fill_between(_x_, _y1_, _y2_, where=_y2_ >= _y1_,
                      facecolor='green', interpolate=True)
    _ax_.fill_between(_x_, _y1_, _y2_, where=_y2_ <= _y1_,
                      facecolor='red', interpolate=True)
    _ax_.set_title('fill between where')

    # Test support for masked arrays.
    _y2_ = np.ma.masked_greater(_y2_, 1.0)
    ax1.plot(_x_, _y1_, _x_, _y2_, color='black')
    ax1.fill_between(_x_, _y1_, _y2_, where=_y2_ >= _y1_,
                     facecolor='green', interpolate=True)
    ax1.fill_between(_x_, _y1_, _y2_, where=_y2_ <= _y1_,
                     facecolor='red', interpolate=True)
    ax1.set_title('Now regions with _y2_>1 are masked')
    fig.savefig("b.png")
    plt.close()
    #####################################################
    # This example illustrates a problem; because of the data
    # gridding, there are undesired unfilled triangles at the crossover
    # points.  A brute-force solution would be to interpolate all
    # arrays to a very fine grid before plotting.
    ##############################################################
    # Use transforms to create axes
    # spans where a certain condition is satisfied:

    fig, _ax_ = plt.subplots()
    _y_ = np.sin(4 * np.pi * _x_)
    _ax_.plot(_x_, _y_, color='black')

    # use data coordinates for the x-axis and the
    # axes coordinates for the y-axis
    import matplotlib.transforms as mtransforms
    trans = mtransforms.blended_transform_factory(_ax_.transData,
                                                  _ax_.transAxes)
    theta = 0.9
    _ax_.axhline(theta, color='green', lw=2, alpha=0.5)
    _ax_.axhline(-theta, color='red', lw=2, alpha=0.5)
    _ax_.fill_between(_x_, 0, 1, where=_y_ > theta,
                      facecolor='green', alpha=0.5, transform=trans)
    _ax_.fill_between(_x_, 0, 1, where=_y_ < -theta,
                      facecolor='red', alpha=0.5, transform=trans)
    fig.savefig("c.png")
    plt.close()


def simple_plot():
    """Creates a plot graph"""
    # https://matplotlib.org/3.1.0/gallery/lines_bars_and_markers/simple_plot.
    # html#sphx-glr-gallery-lines-bars-and-markers-simple-plot-py
    # Data for plotting
    # Modified to write only to a file and close the figure.
    _t_ = np.arange(0.0, 2.0, 0.01)
    _s_ = 1 + np.sin(2 * np.pi * _t_)

    fig, _ax_ = plt.subplots()
    _ax_.plot(_t_, _s_, color='red')

    _ax_.set(xlabel='time (s)', ylabel='voltage (mV)',
             title='About as simple as it gets, folks')
    _ax_.grid()
    print('Writing out figure to simple_plot.png')
    fig.savefig("simple_plot.png")
    plt.close()


def timeline():
    """ Shows the dates contained within lists"""
    # https://matplotlib.org/gallery/lines_bars_and_markers
    # /timeline.html#sphx-glr-gallery-lines-bars-and-markers-timeline-py
    # Modified to write only to a file and close the figure.

    names = ['v2.2.4', 'v3.0.3', 'v3.0.2', 'v3.0.1', 'v3.0.0', 'v2.2.3',
             'v2.2.2', 'v2.2.1', 'v2.2.0', 'v2.1.2', 'v2.1.1', 'v2.1.0',
             'v2.0.2', 'v2.0.1', 'v2.0.0', 'v1.5.3', 'v1.5.2', 'v1.5.1',
             'v1.5.0', 'v1.4.3', 'v1.4.2', 'v1.4.1', 'v1.4.0']

    dates = ['2019-02-26', '2019-02-26', '2018-11-10', '2018-11-10',
             '2018-09-18', '2018-08-10', '2018-03-17', '2018-03-16',
             '2018-03-06', '2018-01-18', '2017-12-10', '2017-10-07',
             '2017-05-10', '2017-05-02', '2017-01-17', '2016-09-09',
             '2016-07-03', '2016-01-10', '2015-10-29', '2015-02-16',
             '2014-10-26', '2014-10-18', '2014-08-26']

    # Convert date strings (e.g. 2014-10-18) to datetime
    dates = [datetime.strptime(_d_, "%Y-%m-%d") for _d_ in dates]
    levels = np.tile([-5, 5, -3, 3, -1, 1],
                     int(np.ceil(len(dates)/6)))[:len(dates)]

    # Create figure and plot a stem plot with the date
    fig, _ax_ = plt.subplots(figsize=(8.8, 4), constrained_layout=True)
    _ax_.set(title="Matplotlib release dates")

    _ax_.vlines(dates, 0, levels, color="tab:red")  # The vertical stems.
    _ax_.plot(dates, np.zeros_like(dates), "-o",
              color="k", markerfacecolor="w")  # Baseline and markers on it.

    # annotate lines
    for _d_, _l_, _r_ in zip(dates, levels, names):
        _ax_.annotate(_r_, xy=(_d_, _l_),
                      xytext=(-3, np.sign(_l_)*3), textcoords="offset points",
                      horizontalalignment="right",
                      verticalalignment="bottom" if _l_ > 0 else "top")

    # format xaxis with 4 month intervals
    _ax_.get_xaxis().set_major_locator(mdates.MonthLocator(interval=4))
    _ax_.get_xaxis().set_major_formatter(mdates.DateFormatter("%b %Y"))
    plt.setp(_ax_.get_xticklabels(), rotation=30, ha="right")

    # remove y axis and spines
    _ax_.get_yaxis().set_visible(False)
    for spine in ["left", "top", "right"]:
        _ax_.spines[spine].set_visible(False)

    _ax_.margins(y=0.1)
    print('Writing out figure to timeline.png')
    fig.savefig("timeline.png")
    plt.close()


def line_demo_dash_control():
    # https://matplotlib.org/gallery/lines_bars_and_markers
    # /line_demo_dash_control.html#sphx-glr
    # -gallery-lines-bars-and-markers-line-demo-dash-control-py
    # Modified to write only to a file and close the figure.

    """
    ==============================
    Customizing dashed line styles
    ==============================

    The dashing of a line is controlled via a dash sequence. It can be modified
    using `.Line2D.set_dashes`.

    The dash sequence is a series of on/off lengths in points, e.g.
    ``[3, 1]`` would be 3pt long lines separated by 1pt spaces.

    Some functions like `.Axes.plot` support passing Line properties as
    keyword arguments. In such a case, you can already set the dashing when
    creating the line.

    *Note*: The dash style can also be configured via a
    :doc:`property_cycle </tutorials/intermediate/color_cycle>`
    by passing a list of dash sequences using the keyword *dashes* to the
    cycler. This is not shown within this example.
    """
    import numpy as np
    import matplotlib.pyplot as plt

    _x_ = np.linspace(0, 10, 500)
    _y_ = np.sin(_x_)

    fig, _ax_ = plt.subplots()

    # Using set_dashes() to modify dashing of an existing line
    line1, = _ax_.plot(_x_, _y_, label='Using set_dashes()')
    line1.set_dashes([2, 2, 10, 2])
    # 2pt line, 2pt break, 10pt line,
    # 2pt break

    # Using plot(..., dashes=...) to set the dashing when creating a line
    line2, = _ax_.plot(_x_, _y_ - 0.2,
                       label='Using the dashes parameter', linestyle='solid')

    _ax_.legend()
    print('Writing out figure to line_demo_dash_control.png')
    fig.savefig("line_demo_dash_control.png")
    plt.close()


def main():
    """This is the main function that will call the plot
       and helper functions"""
    simple_plot()
    line_demo_dash_control()
    timeline()
    fill_between_demo()


if __name__ == "__main__":
    main()
