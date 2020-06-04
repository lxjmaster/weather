from PyQt5.QtWidgets import QApplication, QMainWindow
from WeatherWidget import Ui_Weather
from core import search, get_city_code, parse
import sys


class Main(QMainWindow, Ui_Weather):

    def __init__(self):

        super(Main, self).__init__()
        self.setupUi(self)
        self.CityEdit.setPlaceholderText("请输入需要查询的城市名称")
        self.WeatherResult.setPlaceholderText("程序名称: 城市天气查询-娱乐版\n\n"
                                              "作者: Master_lxj\n\n"
                                              "联系邮箱: 379501669@qq.com\n\n"
                                              "个人博客: http://www.dagouzi.cn")
        self.Search.clicked.connect(self.search_weather)

    def keyPressEvent(self, *args, **kwargs):
        if args[0].key() == 16777220:
            self.search_weather()

    def search_weather(self):

        city = self.CityEdit.text()
        if not city:
            self.statusBar().setStyleSheet("color: red;")
            self.statusBar().showMessage("请输入想要查询的城市名称!")
            return False

        city_code = get_city_code(city)
        if not city_code:
            self.statusBar().setStyleSheet("color: red;")
            self.statusBar().showMessage("没有找到您想要查询的城市名称,请检查名称是否错误!")
            return False

        try:
            response = search(city_code)
            data = parse(response)
            self.WeatherResult.setText("\n".join(data))
        except Exception as error:
            self.statusBar().setStyleSheet("color: red;")
            self.statusBar().showMessage(str(error))


if __name__ == '__main__':
    app = QApplication(sys.argv)
    main = Main()
    main.show()
    sys.exit(app.exec())
