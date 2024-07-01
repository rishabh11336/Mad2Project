# E-Commerce Application

## Overview

This project is a full-featured e-commerce web application with a Vue.js frontend and a Python Flask backend. The application allows users to browse products, add them to a cart, and complete purchases.

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
    python3 main.py
    ```

    The backend application will be running at `http://localhost:5000`.

## Project Features

- User authentication and authorization
- Browse products by category
- Search for products
- Add products to a shopping cart
- Checkout and process orders
- View order history
- Admin dashboard to manage products, categories, and orders

## Usage

1. Register or log in to the application.
2. Browse or search for products.
3. Add products to the shopping cart.
4. Proceed to checkout to complete the purchase.
5. View order history from your account dashboard.

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
