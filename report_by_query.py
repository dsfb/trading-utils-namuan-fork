import argparse
from datetime import datetime
import logging

import pandas as pd

from common.filesystem import output_dir
from common.logger import init_logging
from common.reporting import add_reporting_data, generate_report, convert_to_html


def parse_args():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("-c", "--count", type=int, default=100)
    parser.add_argument("-o", "--sort-by", type=str, default="symbol")
    parser.add_argument("-t", "--title", type=str, required=True)
    parser.add_argument("-q", "--query", type=str, required=True)
    parser.add_argument(
        "-i",
        "--input-file",
        type=str,
        default="{}/{}-data.csv".format(
            output_dir(), datetime.now().strftime("%Y-%m-%d")
        ),
    )
    parser.add_argument(
        "-v",
        "--view-in-browser",
        action="store_true",
        default=False,
        help="Generate HTML Report",
    )
    return parser.parse_args()


if __name__ == "__main__":
    args = parse_args()
    init_logging()

    select_top = args.count
    sort_by = args.sort_by.split(",")
    query = args.query
    report_title = args.title
    view_in_browser = args.view_in_browser
    input_file = args.input_file

    logging.info(f"Reading from file: {input_file}")

    enriched_stocks_df = pd.read_csv(input_file, index_col="symbol")
    logging.info(enriched_stocks_df.columns)

    selected_stocks = (
        enriched_stocks_df.query(query)
        .sort_values(by=sort_by, ascending=False)
        .head(n=select_top)
    )
    report_data = add_reporting_data(selected_stocks)
    logging.info(
        "({}) Selected Stocks: {}".format(
            len(report_data), ", ".join([f"${d.get('symbol')}" for d in report_data])
        )
    )
    template_data = {"sort_by": sort_by, "query": query, "report_data": report_data}
    logging.info("Generating report for: {}".format(report_title))
    output_file = generate_report(
        report_title, template_data, report_file_name="stocks-report.md"
    )
    if view_in_browser:
        convert_to_html(output_file, open_page=True)
    else:
        logging.info(f"Generated {output_file}")
