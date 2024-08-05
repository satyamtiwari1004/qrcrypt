# QrCrypt

QrCrypt is a secure data sharing application that uses QR codes for encrypted communication. It employs AES encryption to maintain data confidentiality during transmission and allows users to securely upload encrypted data to their chosen cloud storage service for centralized storage.

![QrCrypt Screenshot](https://satyam-portfolio-24.s3.ap-south-1.amazonaws.com/img/projects/qrcrypt_snapshot.png)

## Features

- **AES Encryption**: Ensures data confidentiality during transmission.
- **QR Code Generation**: Creates QR codes for encrypted data.
- **Dropbox Integration**: Securely uploads encrypted data to Dropbox.
- **Eel Framework**: Combines Python with HTML, CSS, and JavaScript for a seamless user interface.

## Requirements

- Python 3.x
- pip (Python package installer)

## Installation

1. **Clone the repository**:
    ```bash
    git clone https://github.com/satyamtiwari1004/QrCrypt.git
    cd QrCrypt
    ```

2. **Create a virtual environment** (optional but recommended):
    ```bash
    python3 -m venv venv
    source venv/bin/activate  # On Windows use `venv\Scripts\activate`
    ```

3. **Install the dependencies**:
    ```bash
    pip install -r requirements.txt
    ```

4. **Set up the `.env` file**:
    Create a file named `.env` in the project directory and add your Dropbox API key:
    ```
    DROPBOX_SECRET_KEY=your_dropbox_api_key
    ENCRYPTION_KEY=your_encryption_key
    ```

## Usage

1. **Run the application**:
    ```bash
    python main.py
    ```

2. **Access the application**:
    Open your web browser and go to `http://localhost:8000/home.html`.

## Project Structure

- `main.py`: The main entry point of the application.
- `web/`: Contains HTML, CSS, and JavaScript files.
- `encryption.py`: Handles AES encryption and decryption.
- `dropboxapi.py`: Handles interactions with the Dropbox API.
- `eelconfig.py`: Configures and starts the Eel server.
- `.env`: Contains the Dropbox API key (not included in the repository).

## Contributing

1. Fork the repository.
2. Create a new branch (`git checkout -b feature-branch`).
3. Make your changes.
4. Commit your changes (`git commit -m 'Add new feature'`).
5. Push to the branch (`git push origin feature-branch`).
6. Create a pull request.

## License

This project is licensed under the GNU GENERAL PUBLIC LICENSE License - see the [LICENSE](LICENSE) file for details.

## Acknowledgements

- [Eel](https://github.com/ChrisKnott/Eel) - For bridging Python with front-end technologies.
- [pycrypto](https://pypi.org/project/pycrypto/) - For AES encryption.
- [dropbox](https://www.dropbox.com/developers) - For the cloud storage API.
- [pyqrcode](https://pypi.org/project/PyQRCode/) - For generating QR codes.