import sys
from PyQt4 import QtGui
from PyQt4 import QtCore
from kuaidi_ui import Ui_kuaidi
import urllib2
from bs4 import BeautifulSoup

class MyForm(QtGui.QMainWindow):
	def __init__(self,parent=None):
		QtGui.QWidget.__init__(self,parent)
		self.ui=Ui_kuaidi()
		self.ui.setupUi(self)
		self.ui.pushButton.clicked.connect(self.Search)
	def Search(self):
		if(self.ui.radioButton.isChecked()):
			self.SearchHtml('shunfeng',self.ui.lineEdit.text())
		if(self.ui.radioButton_2.isChecked()):
			self.SearchHtml('yunda',self.ui.lineEdit.text())
		if(self.ui.radioButton_3.isChecked()):
			self.SearchHtml('shentong',self.ui.lineEdit.text())
		if(self.ui.radioButton_4.isChecked()):
			self.SearchHtml('zhongtong',self.ui.lineEdit.text())
		if(self.ui.radioButton_5.isChecked()):
			self.SearchHtml('tiantian',self.ui.lineEdit.text())
		if(self.ui.radioButton_6.isChecked()):
			self.SearchHtml('zhaijisong',self.ui.lineEdit.text())
		if(self.ui.radioButton_7.isChecked()):
			self.SearchHtml('ems',self.ui.lineEdit.text())
		if(self.ui.radioButton_8.isChecked()):
			self.SearchHtml('yuantong',self.ui.lineEdit.text())
	
	def SearchHtml(self,name,number):
		url = 'http://wap.kuaidi100.com/wap_result.jsp?rand=20120517&id=%s&fromWeb=null&&postid=%s'%(name,number)
		req = urllib2.Request(url, headers = {
    			'Connection': 'Keep-Alive',
    			'Accept': 'text/html, application/xhtml+xml, */*',
    			'Accept-Language': 'en-US,en;q=0.8,zh-Hans-CN;q=0.5,zh-Hans;q=0.3',
    			'User-Agent': 'Mozilla/5.0 (Windows NT 6.3; WOW64; Trident/7.0; rv:11.0) like Gecko'
			})
		oper = urllib2.urlopen(req)
		data = oper.read()
		soup=BeautifulSoup(data)
		self.ui.textBrowser.setText('')
		for item in soup.find_all('p')[3:-1]:
			self.ui.textBrowser.append(item.text)
	

if __name__ == '__main__':
	app=QtGui.QApplication(sys.argv)
	myapp=MyForm()
	myapp.show()
	sys.exit(app.exec_())