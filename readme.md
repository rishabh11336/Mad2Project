# Project Name

## Overview

This project is a web application that downloads audio from YouTube videos, transcribes the audio using Whisper AI, and provides options to view and download the transcription files. The frontend is built with Vue.js and the backend is powered by Python Flask.

## Folder Structure

- `Frontend`: Contains the Vue.js application code.
- `Backend`: Contains the Flask application code.

## Prerequisites

- Node.js and npm (for the frontend)
- Python 3.x (for the backend)
- pip (Python package installer)

## Getting Started

### Frontend Setup

1. Navigate to the `Frontend` directory:

    ```bash
    cd Frontend
    ```

2. Install the dependencies:

    ```bash
    npm install
    ```

3. Start the development server:

    ```bash
    npm run serve
    ```

    The frontend application will be running at `http://localhost:8080`.

### Backend Setup

1. Navigate to the `Backend` directory:

    ```bash
    cd Backend
    ```

2. Create and activate a virtual environment:

    ```bash
    python -m venv venv
    source venv/bin/activate   # On Windows, use `venv\Scripts\activate`
    ```

3. Install the dependencies:

    ```bash
    pip install -r requirements.txt
    ```

4. Start the Flask server:

    ```bash
    flask run
    ```

    The backend application will be running at `http://localhost:5000`.

## Project Features

- Download audio from YouTube videos.
- Transcribe audio using Whisper AI.
- View transcriptions in the web application.
- Download transcription files.

## Usage

1. Enter the YouTube video URL in the input field on the frontend.
2. Click the "Download and Transcribe" button.
3. View the transcription in the application.
4. Download the transcription file if needed.

## Contributing

1. Fork the repository.
2. Create a new branch (`git checkout -b feature/your-feature-name`).
3. Make your changes and commit them (`git commit -m 'Add some feature'`).
4. Push to the branch (`git push origin feature/your-feature-name`).
5. Open a pull request.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

## Contact

For any questions or suggestions, please open an issue or contact [Your Name] at [your-email@example.com].

---

Feel free to customize this README file according to your project's specific details and requirements.
