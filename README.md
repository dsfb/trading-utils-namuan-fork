# Market Trading Analysis Utilities/Scripts

Collection of scripts and utilities for stock market analysis, strategies etc

## Setup virtual environment

```shell
$ make setup
```

## Update dependencies

```shell
$ make deps
```

## Running scripts

All available scripts should provide a basic description and options to run appropriately

For eg.

```shell
$ ./venv/bin/python3 download_stocklist.py --help
```

I suggest setting up a quick alias to run the python version in the virtual environment. This will save you remembering
to activate the virtual environment. There are other options where you can override the `cd` command, but I find this
simple and transparent.

```
alias py=./venv/bin/python3
```

Now you can run the same script as

```shell
$ py download_stocklist.py --help
```

## Running your own scanner

As I usually run it over weekend, I've added a make command `weekend` to download the latest stocks and data and run
analysis on it. You can run it as

```shell
$ make weekend
```

Once the analysis is complete, it'll open up [DTale](https://pypi.org/project/dtale/) in your default browser.

![DTale](docs/images/dtale.gif)

## Reporting

Although it is possible to run queries in DTale, there is a way to generate report for a selected query. The generated
report contains the chart along with useful links to third party websites for more information.

You do need to setup [Pandoc](https://pandoc.org/installing.html) to generate HTML reports. If you are unable to install
Pandoc, then run `report_by_query.py` without `-v` argument to generate report in `Markdown` format.

Sample report for finding mean-reversion setups

```shell
$ py report_by_query.py -o monthly_gains_3 -c 20 -t "Short Term Mean Reversion" -q "(last_close < 100) and (last_close > ma_50) and (monthly_gains_3 > 0) and (rsi_2 < 10)"
```

![Scanner Reporting](docs/images/stocks-scanner-reporting.gif)

## Sectors Analysis

Make sure you run `make weekend` to download all pre-requisite data.

### Sector Trends

Generate Multiple Moving Average charts for different sectors

```shell
$ py report_sectors_mma.py
```

![Sectors MMA](docs/images/sectors-mma.gif)

### Relative Strength (not RSI) using Price Momentum Oscillator

```shell
# Find Leaders/Laggards in the whole market against SPY
$ py report_relative_strength.py -b SPY

# Find Leaders/Laggards in the whole market against QQQ
$ py report_relative_strength.py -b QQQ

# Find Leaders/Laggards but only in large-cap (S&P 500)
# Requires downloading the list from BarChart https://www.barchart.com/stocks/indices/sp/sp500
# Save the csv file as 'large-cap.csv' in 'data' folder
$ py report_relative_strength.py -m large-cap -b SPY
```

## Telegram assistants

Make sure you have the following variables set in environment.

```shell
export CHAT_ID = "<telegram-chat-where-the-messages-will-be-pushed>"
export BOT_TOKEN = "<telegram-bot-token>"
```

Read links from `webpages.txt` and send over Telegram on a defined schedule.

```shell
py tele_links
```

Send quick analysis on SPY during market hours.

![SPY Bot](docs/images/telegram-spy-bot.png)

```shell
py tele_spy_trade_bot.py
```

## Crypto Bots

Make sure you define a few variables before starting up these bots

```shell
export EXCHANGE_API_KEY = 
export EXCHANGE_API_SECRET = 
export EXCHANGE = ""
```


