# portoptpy
### About
A Python library for interfacing with and conducting backtests using the Portfolio Optimizer API: https://docs.portfoliooptimizer.io/. All portfolio optimization methodologies require the historical returns of the portfolio's constiutent assets. By default, the library will obtain daily returns data from Yahoo finance for performing optimizations. Users can utilize their own returns data as long as it is passed in with the proper format:

1. Must be a pandas DataFrame.
2. Column indices must be ticker symbols.
3. Row indices must be pandas Timestamps in ascending order.
4. Cell values must be the returns of each asset with the type float64.

For backtesting, the library utilizes asyncio and aiohttp to make concurrent calls to the Portfolio Optimizer API which significantly improves the speed of conducting backtests.

### Installation
```python
pip install portoptpy
```

### Authentication
An API key is not required to use the Portfolio Optimizer API, however, authenticated users get full access to all endpoints more favorable API limits. Using this library for backtesting purposes will likely require an API key which can be obtained here: https://www.buymeacoffee.com/portfolioopt

### Usage
```python
from portoptpy import PortfolioOptimizer

po = PortfolioOptimizer(api_key = 'YOUR_API_KEY')
```

Performing a single minimum variance portfolio optimization using a 63 day lookback period for calculating the covaraince matrix:
```python
portfolio = po.construct_minimum_variance_portfolio(symbols = ['SPY','TLT','GLD','BTC-USD'], lookback = 63)
```

Backtesting an equal risk contributions portfolio using an exponentially weighted covariance matrix with decay factor of 0.95:
```python
backtest = await po.backtest_equal_risk_contributions_portfolio(symbols = ['SPY','TLT','GLD','BTC-USD'],
                                                                    lookback = 63,
                                                                    covariance_type = 'exponential',
                                                                    decay_factor = 0.95)

backtest[['portfolio_equity_curve','benchmark_equity_curve']].plot()
```

### Roadmap
1. Add support for all endpoints.
2. Add support for constraints for each portfolio optimization methodology.
3. Add support for backtesting dynamic portfolios (i.e. Multi-Asset Momentum strategies).