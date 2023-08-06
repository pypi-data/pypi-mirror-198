from market_financialexpress.FinancialExpress_Stock import FinancialExpress_Stock


def getTopGainersData():
    """
    Getting all top gainers data from financial express
    :return:
    """
    feStock = FinancialExpress_Stock()
    feStockData=feStock.getTopGainsersStocksList("nse")
    print(feStockData)

def getTopLosersData():
    """
    Get all top losers data from financial express
    :return:
    """
    feStock = FinancialExpress_Stock()
    feStockData=feStock.getTopLosersStocksList("bse")
    print(feStockData)


if __name__ == '__main__':
    getTopLosersData()