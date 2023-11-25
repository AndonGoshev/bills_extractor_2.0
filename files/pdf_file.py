from abc import ABC, abstractmethod
from files.base_file import BaseFile
import PyPDF2


class PdfFile(BaseFile):
    def extract_data(self):
        pdf_file = open(self.path, 'rb')
        pdf_reader = PyPDF2.PdfReader(pdf_file)
        pages = len(pdf_reader.pages)
        bill_info = ''
        number = ''
        sum_no_vat = 0
        sum_vat = 0
        time_period = ''

        for n in range(pages):
            page = pdf_reader.pages[n].extract_text()
            page_splitted = page.split('\n')
            if len(page_splitted) < 2:
                continue
            if "Обща сума за мобилна/фиксирана услуга без ДДС" in page_splitted[1] or "Обща сума за мобилен/фиксиран номер без ДДС" in page_splitted[1]:
                data_list = page_splitted[0:2]
                number = data_list[0][len(data_list[0]) - 11:]
                sum_no_vat = float(data_list[1][0:6].replace(',', '.'))
                sum_vat = sum_no_vat*1.2
                time_period = data_list[1][50:73]

                bill_info += f"""
Клиент : {BaseFile.NAMES_MAP[number]}
Номер: {number}
Сума без ДДС: {sum_no_vat}
Сума с ДДС: {sum_vat:.2f}
Отчетен период: {time_period}""" + '\n'

        return f"""
        {bill_info}
        
        """
