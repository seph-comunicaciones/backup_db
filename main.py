from datetime import datetime
import pyautogui
from time import sleep
from os import remove, mkdir
from shutil import rmtree, make_archive


# while True:
#     cord_x, cord_y = pyautogui.position()
#
#     print(f"cord_x {cord_x}")
#     print(f"cord_y {cord_y}")
#     sleep(1)

class BackUp:
    def __init__(self, sleep_time, path_file):
        self.sleep_time = sleep_time
        self.path_file = path_file
        self.name_backup = datetime.now().strftime('%d-%m-%Y-%H-%M-%S')

    @staticmethod
    def limpiar_carpeta():
        # Limpiar carpeta
        try:
            rmtree("C:/Users/PC/Downloads/sig")
            sleep(2)
        except FileNotFoundError:
            print("Carpeta no existente")

        # Crear carpeta
        mkdir("C:/Users/PC/Downloads/sig")
        sleep(2)

    def abrir_datagrip(self):
        pyautogui.press("win")
        sleep(self.sleep_time)
        pyautogui.write("DataGrip")
        sleep(self.sleep_time)
        pyautogui.press("enter")
        sleep(10)
        # Click sig
        pyautogui.click(x=60, y=147)
        sleep(2)
        # Recargar db
        pyautogui.click(x=95, y=98)
        sleep(30)

    def export_db(self):
        # Click sig
        pyautogui.rightClick(x=60, y=147)
        sleep(self.sleep_time)
        # Click import/export DB
        pyautogui.click(x=164, y=441)
        sleep(self.sleep_time)
        # Export DB
        pyautogui.click(x=320, y=474)
        sleep(self.sleep_time)
        # Run export
        pyautogui.click(x=1124, y=723)
        sleep(self.sleep_time)

    def export_data(self):
        # Click sig
        pyautogui.click(x=32, y=142)
        sleep(self.sleep_time)
        # Click db sig
        pyautogui.click(x=50, y=185)
        sleep(self.sleep_time)
        # Click public
        pyautogui.click(x=67, y=203)
        sleep(self.sleep_time)
        # Click tables
        pyautogui.rightClick(x=106, y=222)
        sleep(self.sleep_time)
        # Click import/export
        pyautogui.click(x=210, y=469)
        sleep(self.sleep_time)
        # Click export
        pyautogui.click(x=423, y=466)
        sleep(self.sleep_time)
        # Click export to files
        pyautogui.click(x=1219, y=778)
        sleep(self.sleep_time)
        # Click sig
        pyautogui.click(x=32, y=142)
        sleep(30)

    def comprimir_backup(self):
        # Comprimir backup
        make_archive(f"sig-{self.name_backup}", "zip", "C:/Users/PC/Downloads/sig")
        sleep(5)

    def subir_backup_onedrive(self):
        # Abrir one drive
        pyautogui.press("win")
        sleep(self.sleep_time)
        pyautogui.write("OneDrive")
        sleep(self.sleep_time)
        pyautogui.press("enter")
        sleep(5)

        # Buscar carpeta InSEPH
        pyautogui.click(x=822, y=60)
        sleep(self.sleep_time)
        pyautogui.write("InSEPH")
        sleep(self.sleep_time)
        pyautogui.click(x=764, y=135)
        sleep(self.sleep_time)

        # Abrir carpeta backups
        pyautogui.doubleClick(x=323, y=301)
        sleep(self.sleep_time)

        # Click limpio
        pyautogui.rightClick(x=250, y=416)
        sleep(self.sleep_time)

        # Click cargar
        pyautogui.click(x=355, y=466)
        sleep(self.sleep_time)

        # Click cargar archivo
        pyautogui.click(x=612, y=476)
        sleep(self.sleep_time)

        # Click path
        pyautogui.click(x=441, y=55)
        sleep(self.sleep_time)

        # Click escribir path
        pyautogui.write(self.path_file)
        sleep(self.sleep_time)

        # Click subir archivo
        pyautogui.doubleClick(x=233, y=249)
        sleep(5)

    def eliminar_backup(self):
        # Eliminar zip
        remove(f"sig-{self.name_backup}.zip")


if __name__ == '__main__':
    backup = BackUp(0.5, "C:/Users/PC/Documents/backup_db")
    backup.limpiar_carpeta()
    backup.abrir_datagrip()
    backup.export_db()
    backup.export_data()
    backup.comprimir_backup()
    backup.subir_backup_onedrive()
    backup.eliminar_backup()
