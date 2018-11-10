from pdfminer.converter import PDFPageAggregator
from pdfminer.layout import LTTextBoxHorizontal, LAParams
from pdfminer.pdfparser import PDFParser
from pdfminer.pdfdocument import PDFDocument
from pdfminer.pdfpage import PDFPage
from pdfminer.pdfpage import PDFTextExtractionNotAllowed
from pdfminer.pdfinterp import PDFResourceManager
from pdfminer.pdfinterp import PDFPageInterpreter
from pdfminer.pdfdevice import PDFDevice

fp = open('input.pdf', 'rb')
parser = PDFParser(fp)
document = PDFDocument(parser)

# 创建一个PDF资源管理器对象来存储共享资源
rsrcmgr = PDFResourceManager()
# 创建一个pdf设备对象
laparams = LAParams()
device = PDFPageAggregator(rsrcmgr, laparams=laparams)
# 创建一个PDF解析器对象
interpreter = PDFPageInterpreter(rsrcmgr, device)
# 处理文档当中的每个页面
for page in PDFPage.create_pages(document):
    interpreter.process_page(page)
    layout = device.get_result()
    for x in layout:
        if isinstance(x, LTTextBoxHorizontal):
            with open('a.txt', 'a') as f:
                f.write(str(x.get_text().encode('utf-8')))
