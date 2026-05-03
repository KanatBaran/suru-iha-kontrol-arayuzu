@echo off
echo [1/2] arayuz.ui -> arayuz.py dönüştürülüyor...
pyside6-uic arayuz.ui -o arayuz.py

echo [2/2] resource.qrc -> resource_rc.py dönüştürülüyor...
pyside6-rcc .\resource.qrc -o .\resource_rc.py

echo islem tamamlandi.
pause
