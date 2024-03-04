# Arduino Serial Spoofing Tool

## Introduction
This tool is designed to facilitate serial communication with an Arduino device connected to your computer via USB. It allows you to spoof the serial number of your Arduino by changing the Product ID (PID) and Hardware ID (HID) associated with its COM port.

## Requirements
- Python 3.x
- pyserial library (`pip install pyserial`)
- colorama library (`pip install colorama`)

## Installation
1. Clone or download this repository to your local machine.
2. Ensure you have Python 3.x installed on your system.
3. Install the required libraries by running:
    ```
    pip install pyserial colorama
    ```

## Usage
1. Connect your Arduino device to your computer via USB.
2. Run the `serial_spoofing_tool.py` script.
3. Follow the on-screen prompts:
    - Select the COM port corresponding to your Arduino device.
    - Enter the desired PID and HID to spoof your Arduino.
4. The tool will attempt to communicate with your Arduino and spoof the serial numbers. If successful, it will print "Done" in green.

## Notes
- Ensure that your Arduino device is connected and powered on before running the tool.
- Make sure to select the correct COM port corresponding to your Arduino device.
- The tool assumes that your Arduino device is compatible with serial communication and responds to the AT command (Adjust as necessary for your specific Arduino application).

## Contributing
Contributions are welcome! If you encounter any issues or have suggestions for improvements, feel free to open an issue or submit a pull request.

## License
This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.
