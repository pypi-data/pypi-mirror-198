from typing import List
import requests, bs4

class FinancialExpress_Stock:
    """
    handles financial express market stocks
    """
    def __init__(self):
        self._topGainerUrl = "https://www.financialexpress.com/market/stock-market/{stockExchange}-top-gainers/"
        self._topLoserUrl = "https://www.financialexpress.com/market/stock-market/{stockExchange}-top-losers/"

    def tableToList(self, table)->List[List]:
        """
        It converts html --> table object to --> List[List]
        :param table: html table object
        :return: List[List]
        """
        resultList = []
        for tr in table.find_all('tr'):
            rowList = []
            tDatas = tr.find_all('td')
            if not tDatas:
                tDatas = tr.find_all('th')
            for td in tDatas:
                cellValue = td.text
                rowList.append(cellValue.strip())
            resultList.append(rowList)
        return resultList

    def getTopGainerUrl(self, stockExchange: str = "nse") -> str:
        """
        returns top gainers url
        :param stockExchange(str): stock exchanges --> "nse" or "bse"
        :return (str): return top gainer url
        """
        url = self._topGainerUrl.format(stockExchange=stockExchange)
        return url

    def getTopLoserUrl(self, stockExchange: str = "nse") -> str:
        """
        returns top losers url
        :param stockExchange (str): stock exchanges --> "nse" or "bse"
        :return (str): top losers url
        """
        url = self._topLoserUrl.format(stockExchange=stockExchange)
        return url

    def getTopGainsersStocksList(self, stockExchange: str = "nse") -> List[List]:
        """
        returns top gainers stocks list
        :param stockExchange(str ): stock exchanges --> "nse" or "bse"
        :return: return table of top gainsers as List[List]
        """

        hdr = {
            "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.93 Safari/537.36 Edg/90.0.818.56"}
        gainerUrl = self.getTopGainerUrl(stockExchange)
        resp = requests.get(gainerUrl, headers=hdr)
        soup = bs4.BeautifulSoup(resp.text, 'html.parser')
        dataTable = soup.find(id='modality')
        dataList = self.tableToList(dataTable)
        return dataList

    def getTopLosersStocksList(self, stockExchange: str = "nse") -> List[List]:
        """
        returns top losers stocks list
        :param stockExchange(str ): stock exchanges --> "nse" or "bse"
        :return: return table of top gainsers as List[List]
        """
        hdr = {
            "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.93 Safari/537.36 Edg/90.0.818.56"}
        url = self.getTopLoserUrl(stockExchange)
        resp = requests.get(url, headers=hdr)
        soup = bs4.BeautifulSoup(resp.text, 'html.parser')
        dataTable = soup.find(id='modality')
        dataList = self.tableToList(dataTable)
        return dataList