import logging

import pandas as pd
import requests
from dotmap import DotMap
from flatten_dict import flatten

from common.environment import TRADIER_BASE_URL, TRADIER_TOKEN


def get_data(path, params):
    response = requests.get(
        url="{}/{}".format(TRADIER_BASE_URL, path),
        params=params,
        headers={
            "Authorization": f"Bearer {TRADIER_TOKEN}",
            "Accept": "application/json",
        },
    )
    return DotMap(response.json())


def option_chain(symbol, expiration):
    path = "/markets/options/chains"
    params = {"symbol": symbol, "expiration": expiration, "greeks": "true"}
    return get_data(path, params)


def option_expirations(symbol):
    path = "/markets/options/expirations"
    params = {"symbol": symbol, "includeAllRoots": "true"}
    return get_data(path, params)


def fetch_options_data(ticker, expiries=10):
    try:
        expirations_output = option_expirations(ticker)
        for exp_date in expirations_output.expirations.date[:expiries]:
            logging.info(">> {} data for {}".format(ticker, exp_date))
            options_data = option_chain(ticker, exp_date)
            yield exp_date, options_data
    except Exception:
        logging.exception(f"Error downloading options for {ticker}")


def process_options_data(options_data_single_expiry):
    file_content = DotMap(options_data_single_expiry)
    flattened_dict = [
        flatten(option_row, "underscore") for option_row in file_content.options.option
    ]
    options_df = pd.DataFrame(flattened_dict)
    options_df["bid_ask_spread"] = options_df["ask"] - options_df["bid"]
    return options_df


def combined_options_df(ticker, expiries):
    options_records = []
    for exp_date, option_data in fetch_options_data(ticker, expiries):
        options_df = process_options_data(option_data)
        options_records.append(options_df.to_dict("records"))

    return pd.DataFrame([item for each_row in options_records for item in each_row])
