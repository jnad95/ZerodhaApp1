from flask import Flask

from KiteClient import KiteClient

app = Flask(__name__)


@app.route('/')
def hello_world():  # put application's code here
    kite_client = KiteClient()
    instruments = kite_client.get_instruments()
    for instrument in instruments:
        print(instrument)
    return 'Hello World!'


if __name__ == '__main__':
    kite = KiteClient()
    instruments = kite.get_instruments()
    for instrument in instruments:
        print(instruments)
    app.run()
