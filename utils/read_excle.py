import os
import openpyxl
from config import datas_path


class ReadExcel:
    @staticmethod
    def read_excle(file_path,sheet_name):
        datas = []
        try:
            wb = openpyxl.load_workbook(file_path)
            sheet = wb[sheet_name]
            for row in sheet.iter_rows(min_row=2):
                data=tuple([i.value for i in row])
                datas.append(data)
        except Exception as e:
            print(e)
        print(datas)
        return datas

if __name__ == '__main__':
    data=ReadExcel.read_excle(os.path.join(datas_path,'autointerface.xlsx'),'logindata')