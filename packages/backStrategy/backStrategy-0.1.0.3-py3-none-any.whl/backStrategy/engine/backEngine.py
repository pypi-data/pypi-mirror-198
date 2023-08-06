from datetime import datetime
from typing import Callable
from typing import Type, List
from backStrategy.engine.template import CtaTemplate
import pandas as pd
import numpy as np
import pyecharts.options as opts
from pyecharts.charts import Line, Page
from pyecharts.components import Table


class BacktestingEngine:
    """"""

    def __init__(self) -> None:
        """"""
        self.symbol: str = ""
        self.start: datetime = None
        self.end: datetime = None
        self.strategy_class: Type[CtaTemplate] = None
        self.strategy: CtaTemplate = None
        self.bar: dict

        self.callback: Callable = None
        self.history_data: List[dict] = []

    def set_parameters(
            self,
            start: datetime,  # 开始时间
            end: datetime = None,  # 结束时间
    ):
        self.start = start
        self.end = end

    def add_strategy(self, strategy_class: Type[CtaTemplate], setting: dict) -> None:
        """"""
        self.strategy_class = strategy_class
        self.strategy = strategy_class(
            self, strategy_class.__name__, setting
        )

    def remove_data(self, new_dict: dict):
        if "时间" in new_dict.keys() and self.start <= new_dict['时间'] <= self.end:
            return True
        else:
            return False

    def load_data(self, file_name: list) -> None:
        """"""
        print("开始加载历史数据")
        if self.start >= self.end:
            return

        self.history_data.clear()  # 清除之前加载的历史数据

        self.load_bar_data(
            file_name
        )
        print("加载历史数据完成")

    def run_backtesting(self, html_name: str, is_show_symbol: bool) -> None:
        """"""
        self.strategy.on_start()

        # Use the rest of history data for running backtesting
        for data in self.history_data:
            try:
                self.new_bar(data)
            except Exception:
                return

        self.strategy.on_stop()

        self.front_web(self.strategy.line_chart,
                       self.strategy.line_table,
                       self.strategy.detail_dict,
                       html_name,
                       is_show_symbol
                       )

    def line_markpoint(self, chart, is_show_symbol: bool) -> Line:
        try:
            x = [x for x, _ in chart.items()]
            y = [x for _, x in chart.items()]
            line = (
                Line(init_opts=opts.InitOpts(width="100%", ))
                    .add_xaxis(xaxis_data=x)
                    .add_yaxis(
                    series_name='',
                    y_axis=y,
                    is_symbol_show= is_show_symbol
                )
            )
            return line
        except Exception as e:
            print(f"折线图生产异常: {repr(e)}, chart: {chart}")
            return None

    def table_point(self, table_data: list, info: dict) -> Table:
        try:
            table = (
                Table().add(
                    table_data[0],
                    table_data[1:],
                    {"class": "fl-table", "style": "width: 100%"}
                ).set_global_opts({"title": str(info),
                                   "title_style": "style='color:red', align='center'",
                                   })
            )
            return table
        except Exception as e:
            print(f"表格生成异常: {repr(e)}, table_data: {table_data}, info: {info}")
            return None

    def front_web(self, chart: dict, table: List[list], info: dict, html_name, is_show_symbol):
        """生成前端页面"""
        page = Page()
        html_chart = self.line_markpoint(chart, is_show_symbol)
        html_table = self.table_point(table, info)
        if html_table and html_chart:
            page.add(
                html_chart,
                html_table,
            )
        elif html_chart:
            page.add(
                html_chart,
            )
        elif html_table:
            page.add(
                html_table,
            )
        else:
            return
        if ".html" in html_name:
            page.render(html_name)
        else:
            page.render(html_name + ".html")

    def new_bar(self, bar: dict):
        """"""
        self.bar = bar
        self.strategy.on_bar(bar)

    def read_file(self, path):
        data = pd.read_excel(path)  # reading file
        train_data = np.array(data)
        train_data_list: list = train_data.tolist()
        train_data_list.reverse()
        keys = list(data.columns)
        for data in train_data_list:
            new_dict = dict()
            for ind in range(1, len(keys)):
                new_dict[keys[ind]] = data[ind]
            if self.remove_data(new_dict):
                self.history_data.append(new_dict)
        return train_data_list

    def load_bar_data(
            self,
            file_list: List[str],
    ):
        for path in file_list:
            self.read_file(path)
