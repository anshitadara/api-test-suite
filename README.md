# API Test Suite

## Overview
This project is an **API Test Suite** designed to automate the testing of API endpoints. It ensures that the API behaves as expected by validating responses, status codes, and data integrity.

## Features
- **Automated API Testing** using `pytest` and `requests`.
- **Continuous Integration (CI)** using **GitHub Actions**.
- **Supports GET and POST requests** for API validation.
- **Modular Test Structure** for scalability and maintainability.

## Prerequisites
- **Python 3.x** installed
- `pip` package manager

## Setup Instructions
1. **Clone the repository:**
   ```bash
   git clone https://github.com/anshitadara/api-test-suite.git
   cd api-test-suite
   ```

2. **Create a virtual environment (optional but recommended):**
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

## Running the Tests
Run all test cases:
```bash
pytest
```

Run a specific test:
```bash
pytest test_api.py::test_get_valid_response
```

## CI/CD Integration
This project uses **GitHub Actions** to automate API testing. Tests are triggered automatically on **push** and **pull requests**.

- CI Workflow file: `.github/workflows/api-tests.yml`
- View results under the **Actions** tab in the repository.

## Folder Structure
```
api-test-suite/
│── tests/
│   ├── test_api.py          # Main API test cases
│   ├── test_auth.py         # Authentication tests
│── .github/workflows/
│   ├── api-tests.yml        # GitHub Actions workflow for CI
│── requirements.txt         # Dependencies
│── README.md                # Project Documentation
```

## Contributing
1. **Fork the repository**
2. **Create a feature branch** (`git checkout -b feature-branch`)
3. **Commit changes** (`git commit -m "Your message"`)
4. **Push to the branch** (`git push origin feature-branch`)
5. **Create a Pull Request**

## Contact
For any queries, reach out to **anshitadara10@gmail.com**
