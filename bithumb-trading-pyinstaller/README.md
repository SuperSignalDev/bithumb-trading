# Bithumb Trading PyInstaller Project

This project is designed to convert the `bithumb-trading.py` Python script into an executable file using PyInstaller. The script interacts with the Bithumb API to fetch current prices and execute buy/sell orders.

## Project Structure

```
bithumb-trading-pyinstaller
├── src
│   └── bithumb-trading.py        # Main Python script for trading on Bithumb
├── scripts
│   └── build.sh                  # Shell script to automate the build process
├── pyinstaller
│   └── bithumb-trading.spec      # PyInstaller specification file
├── requirements.txt               # Python dependencies
├── .gitignore                     # Git ignore file
├── README.md                      # Project documentation
└── .github
    └── workflows
        └── build.yml             # GitHub Actions workflow for automation
```

## Installation

To get started, clone the repository and navigate to the project directory:

```bash
git clone <repository-url>
cd bithumb-trading-pyinstaller
```

### Requirements

Make sure you have Python 3 and pip installed. Install the required Python packages using:

```bash
pip install -r requirements.txt
```

## Building the Executable

To build the executable, run the `build.sh` script located in the `scripts` directory:

```bash
bash scripts/build.sh
```

This will create an executable file from the `bithumb-trading.py` script using PyInstaller.

## Usage

Once the build process is complete, you can run the generated executable to interact with the Bithumb API for trading.

## Contributing

Feel free to submit issues or pull requests for improvements or bug fixes.

## License

This project is licensed under the MIT License. See the LICENSE file for more details.