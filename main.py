import sys
import cv2
import math
from PySide6.QtCore   import QTimer, Qt, QElapsedTimer
from PySide6.QtGui    import QImage, QPixmap
from PySide6.QtWidgets import (
    QMainWindow, QApplication, QLabel,
    QVBoxLayout, QSizePolicy
)
from arayuz import Ui_MainWindow

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        # --- Başlangıç ayarları ---
        self.ui.widgetIcons.hide()
        self.ui.stackedWidget.setCurrentIndex(0)
        self.ui.pButtoniconBaglanti.setChecked(True)
        self.menuBar().hide()
        self.statusBar().hide()

        # --- Menü butonları ile sayfa geçişi ---
        mapping = {
            self.ui.pButtoniconBaglanti:    0,
            self.ui.pButtonMenuBaglanti:    0,
            self.ui.pButtoniconFormasyon:   1,
            self.ui.pButtonMenuFormasyon:   1,
            self.ui.pButtoniconNavigasyon:  2,
            self.ui.pButtonMenuNavigasyon:  2,
            self.ui.pButtoniconBirey:       3,
            self.ui.pButtonMenuBirey:       3,
            self.ui.pButtoniconKesif:       4,
            self.ui.pButtonMenuKesif:       4,
        }
        for btn, idx in mapping.items():
            btn.toggled.connect(lambda checked, i=idx: self._switch_page(i) if checked else None)

        # --- KAMERA BAŞLATMA BUTONU BAĞLAMASI ---
        self.ui.G4Baslat.clicked.connect(self._start_camera)
        print(">> Init complete, waiting for G4Baslat click")

    def _switch_page(self, index: int):
        self.ui.stackedWidget.setCurrentIndex(index)

    # ----------------------------------------------------------------
    # ——— Kamera Bölümü —————————————————————————————————————
    #   _start_camera(): Kamerayı başlatma tetikleyicisi
    #   _init_camera(): Kamera akışını açıp QLabel üzerine bind eder
    #   _update_frame(): Her 30ms’de bir kareyi QLabel’a çeker
    # ----------------------------------------------------------------
    def _start_camera(self):
        print(">> G4Baslat clicked")
        if hasattr(self, 'cap') and self.cap.isOpened():
            print(">> Kamera zaten açık")
            return

        # Tarama ilerleyişini de aynı anda başlat
        self._start_scan()

        # Kamerayı başlat
        self._init_camera()

    def _init_camera(self):
        print(">> Kamera init ediliyor…")
        # Tek kez aç: ikinci görüntü de aynı cap'i kullanacak
        if not (hasattr(self, 'cap') and self.cap.isOpened()):
            self.cap = cv2.VideoCapture(0)
            if not self.cap.isOpened():
                print("!! Kamera açılamadı")
                return

        # --- 1. hedef: pageKamera ---
        # Var olan layout'u kullan, yoksa oluştur
        lay1 = self.ui.pageKamera.layout()
        if lay1 is None:
            lay1 = QVBoxLayout(self.ui.pageKamera)
            lay1.setContentsMargins(0, 0, 0, 0)
            lay1.setSpacing(0)

        if not hasattr(self, 'video_label') or self.video_label is None:
            self.video_label = QLabel()
            self.video_label.setAlignment(Qt.AlignCenter)
            self.video_label.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
            self.video_label.setScaledContents(True)
            lay1.addWidget(self.video_label)

        # --- 2. hedef: pageKamera2 ---
        lay2 = self.ui.pageKamera2.layout()
        if lay2 is None:
            lay2 = QVBoxLayout(self.ui.pageKamera2)
            lay2.setContentsMargins(0, 0, 0, 0)
            lay2.setSpacing(0)

        if not hasattr(self, 'video_label2') or self.video_label2 is None:
            self.video_label2 = QLabel()
            self.video_label2.setAlignment(Qt.AlignCenter)
            self.video_label2.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
            self.video_label2.setScaledContents(True)
            lay2.addWidget(self.video_label2)

        # Tek timer, iki hedefe birden basacak
        if not hasattr(self, 'timer'):
            self.timer = QTimer(self)
            self.timer.timeout.connect(self._update_frame)  # aynısını kullanacağız
            self.timer.start(30)

        # Eğer ikinci stackedWidget farklı sayfadaysa onu da hedef sayfaya geçir
        if hasattr(self.ui, 'stackedWidgetKamera2'):
            self.ui.stackedWidgetKamera2.setCurrentWidget(self.ui.pageKamera2)


    def _update_frame(self):
        if not (hasattr(self, 'cap') and self.cap.isOpened()):
            return
        ret, frame = self.cap.read()
        if not ret:
            return

        # --- Orijinal kareyi RGB'ye çeviriyoruz ---
        frame_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

        # --- Drone1 etiketi için kopya ---
        frame1 = frame_rgb.copy()
        cv2.putText(frame1, "Drone1", (30, 50), cv2.FONT_HERSHEY_SIMPLEX,
                    1.2, (255, 0, 0), 2, cv2.LINE_AA)

        # --- Drone2 etiketi için kopya ---
        frame2 = frame_rgb.copy()
        cv2.putText(frame2, "Drone2", (30, 50), cv2.FONT_HERSHEY_SIMPLEX,
                    1.2, (0, 255, 0), 2, cv2.LINE_AA)

        # --- QImage/Pixmap'e çevir ve label'lara bas ---
        h, w, ch = frame1.shape
        bytes_per_line = ch * w

        qimg1 = QImage(frame1.data, w, h, bytes_per_line, QImage.Format_RGB888)
        pix1 = QPixmap.fromImage(qimg1)
        if hasattr(self, 'video_label') and self.video_label is not None:
            self.video_label.setPixmap(pix1)

        qimg2 = QImage(frame2.data, w, h, bytes_per_line, QImage.Format_RGB888)
        pix2 = QPixmap.fromImage(qimg2)
        if hasattr(self, 'video_label2') and self.video_label2 is not None:
            self.video_label2.setPixmap(pix2)



    # ----------------------------------------------------------------
    # ——— Tarama (Scan) Bölümü —————————————————————————————————
    #   _start_scan(): Süreyi hesaplayıp QElapsedTimer ve progress-timer başlatır
    #   _update_scan_progress(): Geçen süreye göre % hesaplayıp progressBar’ı günceller
    # ----------------------------------------------------------------
    def _start_scan(self):
        # 1) Alan ve drone sayısını al
        alan = float(self.ui.G3_alandegeri.text())
        drone_count = self.ui.droneCount_SpinBox.value()
        kenar = math.sqrt(alan)
        toplam_saniye = (kenar / drone_count) * kenar + 2

        # 2) ProgressBar’ı sıfırla
        self.ui.progressBarTarama.setValue(0)

        # 3) Geçen süreyi ölçmek için timer başlat
        self._elapsed_timer = QElapsedTimer()
        self._elapsed_timer.start()

        # 4) Toplam sürenin milisaniye cinsini kaydet
        self._scan_duration_ms = toplam_saniye * 1000

        # 5) Progress güncelleme timer’ı (her 100ms)
        self._scan_timer = QTimer(self)
        self._scan_timer.timeout.connect(self._update_scan_progress)
        self._scan_timer.start(100)

    def _update_scan_progress(self):
        elapsed = self._elapsed_timer.elapsed()  # geçen ms
        pct = int((elapsed / self._scan_duration_ms) * 100)
        if pct >= 100:
            pct = 100
            self._scan_timer.stop()
            print(">> Tarama tamamlandı")
        self.ui.progressBarTarama.setValue(pct)

    # ----------------------------------------------------------------

    def closeEvent(self, event):
        if hasattr(self, 'cap') and self.cap.isOpened():
            self.cap.release()
        super().closeEvent(event)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())
