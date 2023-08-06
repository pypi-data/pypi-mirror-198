import os
from win32com.client import constants, gencache
# import win32com.client as win32
from pathlib import Path


class MainWord():

    def docx2pdf(self, path, output_path, docxSuffix=".docx", pdfSuffix='.pdf'):
        waiting_covert_docx_files = []  # 指定路径下，待转换的docx文件。如果是目录，不递归
        abs_input_path = Path(path).absolute()
        # 如果不存在，则不做处理
        if not abs_input_path.exists():
            print("path does not exist path = " + path)
            return
        # 判断是否是文件
        elif abs_input_path.is_file():
            print("path file type is file " + path)
            waiting_covert_docx_files.append(path)
        # 如果是目录，则遍历目录下面的文件
        elif abs_input_path.is_dir():
            for file in abs_input_path.iterdir():
                if file.suffix == docxSuffix:
                    waiting_covert_docx_files.append(file)
        print(waiting_covert_docx_files)
        for docx_file in waiting_covert_docx_files:
            abs_output_path = Path(output_path).absolute()
            abs_single_docx_path = Path(docx_file).absolute()
            new_pdf_name = (str(Path(abs_single_docx_path).stem) + pdfSuffix)
            pdfPath = abs_output_path / new_pdf_name
            self.createpdf(str(abs_single_docx_path), str(pdfPath))

    def createpdf(self, wordPath, pdfPath):
        word_app = gencache.EnsureDispatch('Word.Application')
        doc = word_app.Documents.Open(wordPath, ReadOnly=1)
        # 转换方法
        doc.ExportAsFixedFormat(pdfPath, constants.wdExportFormatPDF)
        word_app.Quit()

    def merge4docx(self, input_path, output_path, new_word_name):
        abs_input_path = Path(input_path).absolute()  # 相对路径→绝对路径
        abs_output_path = Path(output_path).absolute()  # 相对路径→绝对路径
        save_path = abs_output_path / new_word_name
        print('-' * 10 + '开始合并!' + '-' * 10)
        word_app = gencache.EnsureDispatch('Word.Application')  # 打开word程序
        word_app.Visible = False  # 是否可视化
        folder = Path(abs_input_path)
        waiting_files = [path for path in folder.iterdir()]
        output_file = word_app.Documents.Add()  # 新建合并后的文档
        for single_file in waiting_files:
            output_file.Application.Selection.InsertFile(single_file)  # 拼接文档
        output_file.SaveAs(str(save_path))  # 保存
        output_file.Close()
        print('-' * 10 + '合并完成!' + '-' * 10)
