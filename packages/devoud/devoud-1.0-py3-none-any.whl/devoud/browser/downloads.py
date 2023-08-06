# TODO: Исправить статусы и переделать под БД

import json
from datetime import datetime
from pathlib import Path

from PySide6.QtCore import QObject, Signal, Slot
from PySide6.QtWebEngineCore import QWebEngineDownloadRequest
from PySide6.QtWidgets import QMessageBox, QFileDialog
from plyer import notification


class DownloadItem(QObject):
    def __init__(self, download_manager, **kwargs):
        super().__init__(download_manager)
        self.download_manager = download_manager
        self.request: QWebEngineDownloadRequest = kwargs.get('request', None)
        self.status = 'Неизвестно'
        self.percent = 0
        if self.request:
            self.url = self.request.url().toString()
            self.name = self.request.downloadFileName()
            self.path = self.request.downloadDirectory()
            self.total_bytes = self.request.totalBytes()
            self.received_bytes = self.request.receivedBytes()
        else:
            self.url = kwargs.get('url', None)
            self.name = kwargs.get('name', None)
            self.path = kwargs.get('path', '')
            self.total_bytes = kwargs.get('total_bytes', -1)
            self.received_bytes = kwargs.get('received_bytes', -1)

        self.date = kwargs.get('date', datetime.now().strftime("%d-%m-%Y %H:%M"))

    @Slot()
    def start(self):
        if self.request:
            self.request.accept()
            self.download_manager.download_queue().append(self)
            self.download_manager.download_add.emit(self)
            self.request.receivedBytesChanged.connect(self.received_bytes_changed)
            self.request.totalBytesChanged.connect(self.total_bytes_changed)
            self.request.isFinishedChanged.connect(self.finished)
            print(f'[Загрузки]: Началась загрузка файла ({self.name})')

    @Slot()
    def remove(self):
        if self.request:
            self.request.cancel()
            self.request = None
            print('[Загрузки]: Загрузка файла отменена')
        self.download_manager.remove_from_history(self)

    @Slot()
    def finished(self):
        """Удаляет запрос и выводит уведомление"""
        state = self.request.state()
        if state == QWebEngineDownloadRequest.DownloadState.DownloadCompleted:
            self.status = 'Завершен'
            notification.notify(
                title='Файл загружен',
                message=self.path,
                app_name='Devoud',
            )
            self.download_manager.add_to_history(self)
        elif state == QWebEngineDownloadRequest.DownloadState.DownloadInterrupted:
            self.status = 'Ошибка'
            notification.notify(
                title='Ошибка загрузки файла',
                message=self.path,
                app_name='Devoud',
            )
            self.download_manager.remove_from_history(self)
        elif state == QWebEngineDownloadRequest.DownloadState.DownloadCancelled:
            self.status = 'Отменен'
            notification.notify(
                title='Загрузка файла отменена',
                message=self.path,
                app_name='Devoud',
            )
            self.download_manager.remove_from_history(self)
        else:
            self.status = 'Ошибка'
            notification.notify(
                title='Файл не был загружен',
                message=self.path,
                app_name='Devoud',
            )
            self.download_manager.remove_from_history(self)
        self.request.deleteLater()
        self.request = None

    @Slot()
    def received_bytes_changed(self):
        """Обновляет данные о текущем размере файла"""
        self.received_bytes = self.request.receivedBytes()
        self.percent = int(self.received_bytes * 100 / self.total_bytes)

    @Slot()
    def total_bytes_changed(self):
        """Обновляет данные о размере файла"""
        self.total_bytes = self.request.totalBytes()


class DownloadManager(QObject):
    filename = 'downloads.json'
    download_add = Signal(DownloadItem)
    download_remove = Signal(DownloadItem)

    def __init__(self, window):
        super().__init__(parent=window)
        self.window = window
        self.__download_queue = []
        self.__history = {}
        self.load_history_from_file()

    @Slot(QWebEngineDownloadRequest)
    def download_request(self, request: QWebEngineDownloadRequest):
        item: DownloadItem = DownloadMethod.Method(self, request)
        if item:
            item.start()
        else:
            request.cancel()
        DownloadMethod.Method = DownloadMethod.MessageBox

    def download_queue(self) -> list:
        return self.__download_queue

    def history(self) -> dict:
        return self.__history

    def load_history_from_file(self):
        if not self.window.private:
            with Path(self.window.FS.user_dir(), self.filename).open(encoding="utf-8") as history_file:
                try:
                    history_data = json.load(history_file)
                    for item in history_data.items():
                        download_item = DownloadItem(self, name=item[0],
                                                     url=item[1].get('url', None),
                                                     total_bytes=item[1].get('total_bytes', -1),
                                                     path=item[1].get('path', None),
                                                     date=item[1].get('date', None))
                        self.__history[item[0]] = download_item
                except json.decoder.JSONDecodeError:
                    self._restore_history_file()

    def add_to_history(self, item: DownloadItem):
        self.__history[item.name] = item
        if not self.window.private:
            with Path(self.window.FS.user_dir(), self.filename).open(encoding="utf-8") as history_file:
                history_data = json.load(history_file)
                history_data[item.name] = {
                    'total_bytes': int(item.total_bytes),
                    'date': item.date,
                    'url': item.url,
                    'path': item.path
                }
            with Path(self.window.FS.user_dir(), self.filename).open('w', encoding="utf-8") as history_file:
                json.dump(history_data, history_file, indent=4, ensure_ascii=True)

    def remove_from_history(self, item: DownloadItem):
        try:
            del self.__history[item.name]
        except KeyError:
            return False
        if not self.window.private:
            with Path(self.window.FS.user_dir(), self.filename).open(encoding="utf-8") as history_file:
                history_data = json.load(history_file)
                del history_data[item.name]
            with Path(self.window.FS.user_dir(), self.filename).open('w', encoding="utf-8") as history_file:
                json.dump(history_data, history_file, indent=4, ensure_ascii=True)
        self.download_remove.emit(item)

    def remove_all(self):
        items = self.__download_queue + list(self.__history.values())
        for i in items:
            i.remove()

    def _restore_history_file(self):
        if not self.window.private:
            self.__history = {}
            with Path(self.window.FS.user_dir(), self.filename).open('w') as downloads_history_file:
                json.dump(self.__history, downloads_history_file)
            print('[Загрузки]: Идет восстановление файла загрузок')


class DownloadMethod(QObject):
    @classmethod
    def MessageBox(cls, parent, request: QWebEngineDownloadRequest):
        message_box = QMessageBox(parent.window)
        message_box.setWindowTitle('Подтверждение операции')
        message_box.setIcon(QMessageBox.Question)
        message_box.setText('Сохранить в загрузках?')
        message_box.setInformativeText(request.downloadFileName())
        message_box.setStandardButtons(QMessageBox.Yes | QMessageBox.No | QMessageBox.StandardButton.Reset)
        message_box.button(QMessageBox.Yes).setText('Сохранить')
        message_box.button(QMessageBox.No).setText('Отменить')
        message_box.button(QMessageBox.Reset).setText('Выбрать место')
        btn = message_box.exec()

        if btn == QMessageBox.Yes:
            return DownloadItem(parent, request=request)
        elif btn == QMessageBox.Reset:
            path = Path(QFileDialog.getSaveFileName(parent.window, 'Сохранить файл как', request.downloadFileName())[0])
            if str(path) != '.':
                request.setDownloadFileName(path.name)
                request.setDownloadDirectory(str(path.parent))
            return DownloadItem(parent, request=request)
        else:
            return False

    @classmethod
    def SaveAs(cls, parent, request: QWebEngineDownloadRequest):
        path = Path(QFileDialog.getSaveFileName(parent.window, 'Сохранить файл как', request.downloadFileName())[0])

        if str(path) != '.':
            request.setDownloadFileName(path.name)
            request.setDownloadDirectory(str(path.parent))
            return DownloadItem(parent, request=request)
        else:
            return False

    Method = MessageBox
