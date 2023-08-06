from datetime import datetime, timedelta
from backStrategy.engine.backEngine import BacktestingEngine


class RunBackTest:
    def __init__(self):
        self.engine = BacktestingEngine()

    def set_parameters(self, start_time: str, end_time: str):
        start_time = start_time.split("-")
        end_time = end_time.split("-")
        self.engine.set_parameters(
            start=datetime(int(start_time[0]), int(start_time[1]), int(start_time[2]), 0, 0, 0),
            end=datetime(int(end_time[0]), int(end_time[1]), int(end_time[2]), 23, 59, 0),
        )

    def init_strategy(self, strategy_class, param: dict):
        self.engine.add_strategy(strategy_class, param)

    def start_strategy(self, strategy_class, start_time: str, end_time: str, file_name: list, html_name: str, is_show_symbol: bool):
        self.set_parameters(start_time, end_time)
        self.init_strategy(strategy_class, {})
        self.engine.load_data(file_name)
        self.engine.run_backtesting(html_name, is_show_symbol)


back_tester = RunBackTest()
