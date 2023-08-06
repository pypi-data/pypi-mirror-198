# -*- coding: utf-8 -*-
from setuptools import setup

package_dir = \
{'': 'src'}

packages = \
['coin_test',
 'coin_test.analysis',
 'coin_test.backtest',
 'coin_test.data',
 'coin_test.orchestration',
 'coin_test.util']

package_data = \
{'': ['*']}

install_requires = \
['croniter>=1.3.7,<2.0.0',
 'pandas-stubs>=1.5.3.230203,<2.0.0.0',
 'pandas>=1.5.0,<2.0.0',
 'pytest-sugar>=0.9.6,<0.10.0',
 'tqdm>=4.64.1,<5.0.0']

setup_kwargs = {
    'name': 'coin-test',
    'version': '0.1.0',
    'description': 'Robust and rigorous backtesting framework for cryptocurrencies.',
    'long_description': '# coin-test\n\n[![Tests](https://github.com/coin-test/coin-test/workflows/Tests/badge.svg)](https://github.com/coin-test/coin-test/actions?workflow=Tests)\n[![Codecov](https://codecov.io/gh/coin-test/coin-test/branch/main/graph/badge.svg)](https://codecov.io/gh/coin-test/coin-test)\n\nCoin-test is a backtesting library designed for cryptocurrency trading. It supports trading strategies across multiple currencies and advanced configurations of tests, including cron-based scheduled execution of strategies, synthetic data generation, slippage modeling, and trading fees.\n\n## Quick Start\n\nCoin-test runs on Python 3.10 or higher. Install the package via pip:\n\n```sh\npip3 install coin-test\n```\n\nTo run a backtest, import the coin-test library. Then define your data source, strategy, and test settings to run the analysis.\n\n```python\nimport datetime as dt\nimport os\nimport pandas as pd\n\nfrom coin_test.backtest import Portfolio, Strategy, MarketTradeRequest\nfrom coin_test.data import CustomDataset\nfrom coin_test.util import AssetPair, Ticker, Money, Side\n```\nThen, import data from a CSV or another source to load\ninto the backtest.\n```python\ndataset_file = "data/ETHUSDT-1h-monthly/BTCUSDT-1h-2017-08.csv"\nheader = ["Open Time", "Open", "High", "Low", "Close", "Volume", "Close Time",\n    "Quote asset volume", "Number of trades", "Taker buy base asset volume",\n    "Taker buy quote asset volume", "Ignore"\n]\ndf = pd.read_csv(dataset_file, names=header)\ndf = df.drop(columns=["Close Time", "Quote asset volume", "Number of trades",\n                      "Taker buy base asset volume",\n                      "Taker buy quote asset volume", "Ignore"])\ndf["Open Time"] //= 1000  # To seconds\ndf = df.sort_values(by=["Open Time"])\n\n# define dataset metadata\nusdt = Ticker("USDT")\nbtc = Ticker("BTC")\nasset_pair = AssetPair(btc, usdt)\nfreq = "H"\n\ndataset = CustomDataset(df, freq, asset_pair)\n```\n\nStrategies are stored in classes as shown below. Each strategy\nshould have a schedule, which is a cron string representing\nwhen this strategy is run, a lookback, which is how much\ndata is accessed in the strategy, and a `__call__` method\nwhich returns a list of TradeRequest objects, which represent\ntrades the strategy wants to make.\n\n```python\nclass MACD(Strategy):\n    def __init__(self, asset_pair) -> None:\n        """Initialize a MACD object."""\n        super().__init__(\n            name="MACD",\n            asset_pairs=[asset_pair],\n            schedule="0 9 * * *",\n            lookback=dt.timedelta(days=26),\n        )\n        self.perc = 0.2\n\n    def __call__(self, time, portfolio, lookback_data):\n        """Execute test strategy."""\n        asset_pair = self.asset_pairs[0]\n        exp1 = lookback_data[asset_pair]["Close"].ewm(span=12 * 24, adjust=False).mean()\n        exp2 = lookback_data[asset_pair]["Close"].ewm(span=26 * 24, adjust=False).mean()\n        macd = exp1 - exp2\n        exp3 = macd.ewm(span=9 * 24, adjust=False).mean()\n\n        if macd.iloc[-1] > exp3.iloc[-1]:\n            return [MarketTradeRequest(\n                asset_pair,\n                Side.BUY,\n                notional=portfolio.available_assets(usdt).qty * self.perc,\n            )]\n        elif macd.iloc[-1] < exp3.iloc[-1]:\n            return [MarketTradeRequest(\n                asset_pair,\n                Side.SELL,\n                qty=portfolio.available_assets(btc).qty * self.perc,\n            )]\n        return []\n```\n\nThis package supports multiple strategies, train-test splits\nfor historical data, synthetic data, and further customization.\nTo run the backtest, define the datasets\n\n```python\nfrom coin_test.backtest import ConstantSlippage, ConstantTransactionFeeCalculator\nsc = ConstantSlippage(50)\ntc = ConstantTransactionFeeCalculator(50)\n\ndatasets = [dataset]\nstrategies = [MACD]\n\nresults = coin_test.run(datasets, strategies, sc, tc,\n                        portfolio, pd.Timedelta(days=90),\n                        n_parallel=8)\n```\n',
    'author': 'Eamon Ito-Fisher',
    'author_email': 'eamon@itofisher.com',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'https://github.com/coin-test/coin-test',
    'package_dir': package_dir,
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.10,<3.11',
}


setup(**setup_kwargs)
