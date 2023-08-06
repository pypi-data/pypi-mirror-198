'''
Author: hexu
Date: 2021-10-14 14:54:05
LastEditTime: 2023-03-17 17:24:52
LastEditors: Hexu
Description: 从数据工场获取模型数据集
FilePath: /iw-algo-fx/intelliw/datasets/datasource_semantic.py
'''
from intelliw.datasets.datasource_base import AbstractDataSource, DataSourceReaderException
from intelliw.utils import iuap_request
from intelliw.utils.logger import _get_framework_logger
from intelliw.config import config

logger = _get_framework_logger()


def err_handler(request, exception):
    print("请求出错,{}".format(exception))


class DataSourceSemanticData(AbstractDataSource):
    """
    数据工场数据源
    """

    def __init__(self, data_address, table_id, fields):
        """
        智能分析数据源
        :param data_address:   获取数据 url
        :param fields: 获取数据表字段 
        :param table_id:   表Id
        """
        self.data_address = data_address
        self.table_id = table_id
        self.fields = fields
        self.__total = None

    def total(self):
        """获取数据总行数"""
        if self.__total is not None:
            return self.__total

        data = {
            'entity': self.table_id,
            'pager': {
                "pageIndex": 1,
                "pageSize": 1
            }
        }
        response = iuap_request.post_json(
            self.data_address, json=data)
        if response.status != 200:
            msg = f"获取行数失败，url: {self.get_row_address}, response: {response}"
            raise DataSourceReaderException(msg)
        row_data = response.json

        self.__total = 0
        try:
            count = row_data["data"]["pager"]['recordCount']
            if isinstance(count, int):
                self.__total = count
        except Exception as e:
            msg = f"获取行数返回结果错误, response: {row_data}, request_url: {self.get_row_address}"
            raise DataSourceReaderException(msg)
        return self.__total

    def reader(self, pagesize=10000, offset=0, limit=0, transform_function=None, dataset_type='train_set'):
        return self.__Reader(self.data_address, self.table_id, self.fields, self.total(), pagesize, transform_function)

    class __Reader:
        def __init__(self, data_address, table_id, fields, total, pagesize=5000, transform_function=None):
            """
            eg. 91 elements, page_size = 20, 5 pages as below:
            [0,19][20,39][40,59][60,79][80,90]
            offset 15, limit 30:
            [15,19][20,39][40,44]
            offset 10 limit 5:
            [10,14]
            """
            self.logger = _get_framework_logger()
            self.data_address = data_address
            self.table_id = table_id
            self.fields = fields
            self.page_size = max(100, pagesize)
            self.page_num = 1
            self.total_read = 0
            self.total_rows = total

        def get_data_bar(self):
            """数据拉取进度条"""
            if self.page_num % 5 == 1:
                try:
                    proportion = round(
                        (self.total_read/self.total_rows)*100, 2)
                    logger.info(
                        f"数据获取中: {self.total_read}/{self.total_rows}, 进度{proportion}%")
                except:
                    pass

        @property
        def iterable(self):
            return True

        def __iter__(self):
            return self

        def __next__(self):
            if self.total_read == self.total_rows:
                logger.info('数据下载完成，共读取原始数据 {} 条'.format(self.total_read))
                raise StopIteration

            self.get_data_bar()

            page = None
            try:
                page = self._read_page(self.page_num, self.page_size)
                assert page is not None, "获取的数据为空"
            except Exception as e:
                logger.exception(
                    f"智能工场数据源读取失败, input_address: [{self.table_id}]")
                raise DataSourceReaderException('智能工场数据源读取失败') from e

            page_count = len(page['result'])
            if page_count == 0:
                raise StopIteration
            self.total_read += page_count
            self.page_num += 1
            return page

        def _get_meta(self, data):
            if self.meta == []:
                self.meta = [{"code": k} for k in data.keys()]
            return self.meta

        def _data_process(self, data):
            result = []
            if len(data) > 0:
                self._get_meta(data[0])
            for d in data:
                val = []
                [val.append(d.get(k["code"])) for k in self.meta]
                result.append(val)
            return {"result": result, "meta": self.meta}

        def _read_page(self, page_index, page_size):
            """
            数据工场获取数据接口，分页读取数据
            :param page_index: 页码，从 0 开始
            :param page_size:  每页大小

            此接口：pageIndex 代表起始下标（不是页）， pagesize代表每页数据的数量， pagecount代表获取几页
                   但是返回的数据类型是[{},{}] 而不是 [[{},{}],[]], 所以保证pageSize和pageCount中某一个数为1的时候， 另一个参数就可以当size使用（很迷惑）
            例如： {'id': self.table_id, 'pageIndex': 1,'pageSize': 10, 'pageCount': 1} 和 {'id': self.table_id, 'pageIndex': 1,'pageSize': 1, 'pageCount': 10} 的结果完全一致
            :return:
            """
            request_data = {
                'entity': self.table_id,
                'pager': {
                    "pageIndex": page_index,
                    "pageSize": page_size
                }
            }
            response = iuap_request.post_json(
                url=self.input_address, json=request_data, timeout=30)
            response.raise_for_status()
            result = response.json
            return self._data_process(result["data"])
