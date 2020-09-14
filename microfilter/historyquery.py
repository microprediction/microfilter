from microfilter.historyreader import HistoryReader
from collections import Counter
import pprint
from functools import partial


class HistoryQuery(HistoryReader):

    def __init__(self):
        super().__init__()

    # ------------------------ #
    #   A few common queries   #
    # -----------------------  #

    @staticmethod
    def _counter(df, col_name):
        return Counter(df[col_name].values)

    @staticmethod
    def _counter_updater(c1,c2):
        if c1 is None:
            return c2
        else:
            c1.update(c2)
            return c1

    def _cusip_counter(self, df):
        return self._counter(df=df,col_name='CUSIP')

    def run_cusip_count(self):
        return self.run_query(mapper=self._cusip_counter,reducer=self._counter_updater)

    @staticmethod
    def _cusip_selector(df, cusip):
        return df.loc[df['CUSIP'] == cusip]

    def run_cusip_selector(self, cusip='126650CX6'):
        return self.run_query(mapper=partial(self._cusip_selector, cusip=cusip))


if __name__=='__main__':
    hq = HistoryQuery()
    if False:
        # Example: Find the 10 most liquid bonds
        cusip_count = hq.run_cusip_count()
        print(cusip_count.most_common(10))
    if True:
        # Example: Trades for most liquid bond
        trades = hq.run_cusip_selector(cusip='126650CX6')
        pass