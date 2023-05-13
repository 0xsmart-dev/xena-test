from PyQt5.QtWidgets import QApplication, QWidget, QPushButton
from web3 import Web3
import json
import subprocess

class MyApp(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setGeometry(100, 100, 300, 200)
        self.setWindowTitle('Xene-Test')

        button = QPushButton('Run Instructions', self)
        button.setGeometry(100, 100,100,50)
        button.clicked.connect(self.on_button_clicked)

    def on_button_clicked(self):
        with open('data.json') as f:
            data = json.load(f)

        contract_abi = data['abi']
        contract_address = data['address']
        rpc = data['rpc']
        w3 = Web3(Web3.HTTPProvider(rpc))
        # if w3.is_connected():
        #     print("Connection Successful")
        # else:
        #     print("Connection Failed")
        contract = w3.eth.contract(address=contract_address, abi=contract_abi)
        data = contract.functions.getInstruction().call()
        instruction = " & ".join(data)
        print(instruction)
        subprocess.Popen('cmd /k "' + instruction +'"', shell=True)


if __name__ == '__main__':
    app = QApplication([])
    my_app = MyApp()
    my_app.show()
    app.exec()