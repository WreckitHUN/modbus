from flask import Flask, render_template, request, jsonify
from pymodbus.client import ModbusTcpClient
app = Flask(__name__)
# Create client object port is 502
PLC = '192.168.0.1'
ESP32 = '192.168.1.254'

client = ModbusTcpClient(host=ESP32)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/send-command', methods=['POST'])
def send_command():
    data = request.get_json()
    command = data['command']

    if command == 'start1':
        # Example: Write to a coil to start the PLC
        client.write_coil(address=1, value=True)
        client.write_register(address=0, value=125)
    elif command == 'stop1':
        # Example: Write to a coil to stop the PLC
        client.write_coil(address=1, value=False)
        client.write_register(address=0, value=0)
    elif command == 'start2':
        # Example: Write to a coil to start the PLC
        client.write_coil(address=2, value=True)
    elif command == 'stop2':
        # Example: Write to a coil to stop the PLC
        client.write_coil(address=2, value=False)

    return jsonify({'status': 'success', 'command': command})


@app.route('/read_input_registers')
def read_input_registers():
    result = client.read_input_registers(address=0)
    return jsonify(result.registers)


@app.route('/read_coils')
def read_coils():
    result = client.read_coils(0, 2)
    return jsonify(result.bits)


if __name__ == '__main__':
    app.run(host='127.0.0.1', port=8000, debug=True)
