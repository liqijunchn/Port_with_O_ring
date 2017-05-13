# coding = utf-8
import sys
import os
import sqlite3
from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel, QLineEdit, QComboBox, QWidget, QVBoxLayout, QGridLayout, QHBoxLayout,QPushButton
from PyQt5.QtGui import QPixmap,QIcon


class port_with_o_ring(QMainWindow):
    def __init__(self):
        super().__init__()
        mainWidget = QWidget()
        self.setCentralWidget(mainWidget)
        mainLayout = QVBoxLayout(mainWidget)

        hbox = QHBoxLayout()
        self.info = QLabel('Use tube OD or thread_size to query dimensions of threaded port with o ring per SAE J1926-1')
        self.tube_OD_lb = QLabel("Tube OD")
        self.tube_OD_cb = QComboBox()
        self.tube_query_btn = QPushButton('Query')
        self.thread_size_lb = QLabel('thread_size')
        self.thread_size_cb = QComboBox()
        self.thread_query_btn = QPushButton("Query")
        self.pictureLabel = QLabel()
        self.pictureLabel.setPixmap(QPixmap(self.resource_path('port.png')))
        self.pictureLabel.resize(500,500)
        self.spotface_diameter_le = QLineEdit('Y')

        self.spotface_depth_le = QLineEdit('S')
        self.o_ring_seat_diameter_le= QLineEdit('U')
        self.o_ring_depth_le=QLineEdit('Y')
        self.minimum_drill_depth = QLineEdit('P')
        self.minimum_tap_depth = QLineEdit('J')
        self.pilot_hole_diameter = QLineEdit('d1')
        self.z_angle_le = QLineEdit('Z')

        self.inch_tubing_OD_lb =QLabel('Inch Tubing OD')
        self.inch_tubing_OD_le =QLineEdit()
        self.metric_tubing_OD_lb =QLabel('Metric Tubing OD')
        self.metric_tubing_OD_le =QLineEdit()
        self.as568_lb = QLabel('AS568')
        self.as568_le =QLineEdit()

        self.as568_le.setMaximumWidth(30)
        self.spotface_diameter_le.setMaximumWidth(40)
        self.o_ring_seat_diameter_le.setMaximumWidth(40)
        self.spotface_depth_le.setMaximumWidth(40)
        self.minimum_drill_depth.setMaximumWidth(40)

        self.o_ring_size = QLabel('O ring size ID X W')
        self.o_ring_size_le = QLineEdit()
        self.thread_minor_diameter =QLabel('Thread Minor Diameter')
        self.thread_minor_diameter_le =QLineEdit()

        mainLayout.addWidget(self.info)

        hbox.addWidget(self.tube_OD_lb)
        hbox.addWidget(self.tube_OD_cb)
        hbox.addWidget(self.tube_query_btn)
        hbox.addWidget(self.thread_size_lb)
        hbox.addWidget(self.thread_size_cb)
        hbox.addWidget(self.thread_query_btn)
        hbox.addStretch()

        grid = QGridLayout()
        grid.addWidget(self.pictureLabel, 0, 0, 20, 20)
        grid.addWidget(self.spotface_diameter_le, 1, 8)
        grid.addWidget(self.spotface_depth_le,3,18)
        grid.addWidget(self.o_ring_seat_diameter_le,2,8)
        grid.addWidget(self.o_ring_depth_le,4,1)
        grid.addWidget(self.minimum_tap_depth,7,0)
        grid.addWidget(self.minimum_drill_depth,7,18)
        grid.addWidget(self.pilot_hole_diameter,18,8)
        grid.addWidget(self.z_angle_le,6,3)
        grid.setHorizontalSpacing(10)


        hbox2=QHBoxLayout()
        hbox2.addWidget(self.inch_tubing_OD_lb)
        hbox2.addWidget(self.inch_tubing_OD_le)
        hbox2.addWidget(self.metric_tubing_OD_lb)
        hbox2.addWidget(self.metric_tubing_OD_le)
        hbox2.addStretch()

        hbox3=QHBoxLayout()
        hbox3.addWidget(self.as568_lb)
        hbox3.addWidget(self.as568_le)
        hbox3.addWidget(self.o_ring_size)
        hbox3.addWidget(self.o_ring_size_le)
        hbox3.addWidget(self.thread_minor_diameter)
        hbox3.addWidget(self.thread_minor_diameter_le)
        hbox3.addStretch()


        mainLayout.addLayout(hbox)
        mainLayout.addLayout(grid)
        mainLayout.addLayout(hbox2)
        mainLayout.addLayout(hbox3)

        for column in range(19):
            grid.setColumnStretch(column, 1)
        for row in range(20):
            grid.setRowStretch(row, 1)

        self.resize(self.minimumSizeHint())

        self.setWindowTitle('Query Port with O ring')
        iconpath=self.resource_path('jci.ico')
        self.setWindowIcon(QIcon(iconpath))
        self.show()

        # self.resize(600, 530)


        # 定义tube_OD 下拉列表框中数值
        self.tube_OD_cb.addItems(self.query('nominal_tube_OD'))

        # 定义 thread_size 下拉列表框中数值
        self.thread_size_cb.addItems(self.query('thread_size'))

        # 更新查询后的数据
        self.tube_OD_cb.currentIndexChanged.connect(self.update_data)
        self.tube_query_btn.clicked.connect(self.update_data)
        self.thread_size_cb.currentIndexChanged.connect(self.update_data_two)
        self.thread_query_btn.clicked.connect(self.update_data_two)


    def query(self, query_info,query_cond=None):
        '''查询数据库中query_info列的信息'''
        self.conn=sqlite3.connect(self.resource_path('threaded port with o ring.db'))
        cursor=self.conn.cursor()
        if query_cond == None:
            sql='select %s from [thread port with o ring] ' % (query_info)
        elif query_cond == 'nominal_tube_OD':
            sql= "select %s from [thread port with o ring] where nominal_tube_OD= '%s'"%(query_info, self.tube_OD_cb.currentText())
        elif query_cond == 'thread_size':
            sql= "select %s from [thread port with o ring] where thread_size= '%s'"%(query_info, self.thread_size_cb.currentText())
        cursor.execute(sql)
        rs=cursor.fetchall()
        temp=[item[0] for item in rs]
        cursor.close()
        self.conn.close()
        return temp

    def resource_path(self, relative_path):
        """ Get absolute path to resource, works for
         dev and for PyInstaller """
        try:
            # PyInstaller creates a temp folder and stores path in _MEIPASS,
            # and places our data files in a folder relative to that temp
            # folder named as specified in the datas tuple in the spec file
            base_path=sys._MEIPASS
        except Exception:
            # sys._MEIPASS is not defined, so use the original path
            base_path=os.path.abspath(".")
        return os.path.join(base_path, relative_path)

    def update_data(self):
        tmp=self.query('spotface_diameter','nominal_tube_OD')
        self.spotface_diameter_le.setText(str(tmp[0]))
        tmp=self.query('spotface_depth','nominal_tube_OD')
        self.spotface_depth_le.setText(str(tmp[0]))
        tmp=self.query('o_ring_seat_diameter','nominal_tube_OD')
        self.o_ring_seat_diameter_le.setText(str(tmp[0]))
        tmp=self.query('o_ring_seat_depth','nominal_tube_OD')
        self.o_ring_depth_le.setText(str(tmp[0]))
        tmp=self.query('minimum_thread_depth','nominal_tube_OD')
        self.minimum_tap_depth.setText(str(tmp[0]))
        tmp=self.query('minimum_drill_depth','nominal_tube_OD')
        self.minimum_drill_depth.setText(str(tmp[0]))
        tmp=self.query('Z','nominal_tube_OD')
        self.z_angle_le.setText(str(tmp[0]))
        tmp=self.query('pilot_hole_diameter','nominal_tube_OD')
        self.pilot_hole_diameter.setText(str(tmp[0]))
        tmp=self.query('AS568','nominal_tube_OD')
        self.as568_le.setText(str(tmp[0]))
        tmp=self.query('o_ring_size','nominal_tube_OD')
        self.o_ring_size_le.setText(str(tmp[0]))
        tmp=self.query('thread_minor_diameter','nominal_tube_OD')
        self.thread_minor_diameter_le.setText(str(tmp[0]))
        tmp=self.query('nominal_tube_OD','nominal_tube_OD')
        self.tube_OD_cb.setCurrentText(str(tmp[0]))
        tmp=self.query('thread_size','nominal_tube_OD')
        self.thread_size_cb.setCurrentText(str(tmp[0]))
        tmp=self.query('inch_tubing_OD','nominal_tube_OD')
        self.inch_tubing_OD_le.setText(str(tmp[0]))
        tmp=self.query('metric_tubing_OD','nominal_tube_OD')
        self.metric_tubing_OD_le.setText(str(tmp[0]))


    def update_data_two(self):
        tmp=self.query('spotface_diameter','thread_size')
        self.spotface_diameter_le.setText(str(tmp[0]))
        tmp=self.query('spotface_depth','thread_size')
        self.spotface_depth_le.setText(str(tmp[0]))
        tmp=self.query('o_ring_seat_diameter','thread_size')
        self.o_ring_seat_diameter_le.setText(str(tmp[0]))
        tmp=self.query('o_ring_seat_depth','thread_size')
        self.o_ring_depth_le.setText(str(tmp[0]))
        tmp=self.query('minimum_thread_depth','thread_size')
        self.minimum_tap_depth.setText(str(tmp[0]))
        tmp=self.query('minimum_drill_depth','thread_size')
        self.minimum_drill_depth.setText(str(tmp[0]))
        tmp=self.query('Z','thread_size')
        self.z_angle_le.setText(str(tmp[0]))
        tmp=self.query('pilot_hole_diameter','thread_size')
        self.pilot_hole_diameter.setText(str(tmp[0]))
        tmp=self.query('AS568','thread_size')
        self.as568_le.setText(str(tmp[0]))
        tmp=self.query('o_ring_size','thread_size')
        self.o_ring_size_le.setText(str(tmp[0]))
        tmp=self.query('thread_minor_diameter','thread_size')
        self.thread_minor_diameter_le.setText(str(tmp[0]))
        tmp=self.query('nominal_tube_OD','thread_size')
        self.tube_OD_cb.setCurrentText(str(tmp[0]))
        tmp=self.query('thread_size','thread_size')
        self.thread_size_cb.setCurrentText(str(tmp[0]))
        tmp=self.query('inch_tubing_OD','thread_size')
        self.inch_tubing_OD_le.setText(str(tmp[0]))
        tmp=self.query('metric_tubing_OD','thread_size')
        self.metric_tubing_OD_le.setText(str(tmp[0]))


if __name__ == '__main__':
    app=QApplication(sys.argv)
    w=port_with_o_ring()
    sys.exit(app.exec_())
