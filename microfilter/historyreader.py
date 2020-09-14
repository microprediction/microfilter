import pandas as pd
from datetime import datetime
from dateutil.relativedelta import relativedelta


class HistoryReader:

    def __init__(self):
        self.START_DATE = datetime(2019, 9, 1)
        self.END_DATE = datetime(2020, 8, 31)

    def monthly_ids(self, start_date=None, end_date=None)->[str]:
        """
        :return:  List of monthly ids
        """
        start_date = start_date or self.START_DATE
        end_data = end_date or self.END_DATE
        monthly_ids = list()
        iterDate = self.START_DATE
        while iterDate <= self.END_DATE:
            month_id = iterDate.strftime('%Y_%m')
            monthly_ids.append(month_id)
            iterDate += relativedelta(months=+1)
        return monthly_ids

    def get_month(self,month_id:str)->pd.DataFrame:
        """
        :param month_id: str    strftime('%Y_%m')
        :return: pd.DataFrame
        """
        return pd.read_csv('/Users/petercotton/github/microfilter/data/'+month_id+'.zip', compression='zip', header=0, sep=',', quotechar='"')

    @staticmethod
    def identity(df):
        return df

    @staticmethod
    def _append(df1, df2):
        return df1.append(df2) if df1 is not None else df2

    def run_query(self, start_date=None, end_date=None, mapper=None, reducer=None):
        """
        :param start_date:
        :param end_date:
        :param func:
        :return:
        """
        start_date= start_date or self.START_DATE
        end_date = end_date or self.END_DATE
        if mapper is None:
            mapper = self.identity
        if reducer is None:
            reducer = self._append
        results = None
        for month_id in self.monthly_ids(start_date=start_date, end_date=end_date):
            df_ = self.get_month(month_id)
            result = mapper(df_)
            results = reducer(results, result)
        return results


