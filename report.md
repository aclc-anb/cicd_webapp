# Flask Webapp CI/CD Setup Report

## Project Overview
This project implements a simple Flask web application with CI/CD pipeline integration using GitHub Actions. The application provides a basic interface where users can submit their name and receive a personalized greeting.

## Technology Stack
- **Backend**: Flask (Python)
- **Testing**: pytest
- **CI/CD**: GitHub Actions
- **Containerization**: Docker

## Implementation Steps

### 1. Flask Application Setup
A simple Flask application was created with the following routes:
- `/` - Home route that renders the main page
- `/submit` - API endpoint that processes name submissions
- Custom 404 error handler

### 2. Unit Testing
I implemented four test cases using pytest:
- Test for the home page loading correctly
- Test for the submit endpoint with a name parameter
- Test for the submit endpoint without a name parameter (using default value)
- Test for the 404 error handler

To run tests locally:
```bash
pytest
```

### 3. CI/CD Pipeline Configuration
I created a GitHub Actions workflow file (`.github/workflows/ci.yml`) that:
- Runs on push to main/master branches and on pull requests
- Sets up Python environment
- Installs dependencies
- Runs tests
- Builds a Docker image (commented out in actual workflow)
- Has placeholder for deployment steps

### 4. Docker Configuration
Created a Dockerfile to containerize the application for consistent deployment.

### 5. Pipeline Execution
After pushing the changes to the repository, the GitHub Actions pipeline executed successfully as shown in the screenshots below.

## Screenshots

![alt text](<Screenshot 2025-03-07 225250.png>)
![alt text](<Screenshot 2025-03-07 225310.png>) ![alt text](<Screenshot 2025-03-07 225324.png>) ![alt text](<Screenshot 2025-03-07 225337.png>)
## Challenges and Solutions

### Challenge 1: Test Environment Setup
Initial tests were failing because the Flask application was in production mode. Solution: Added configuration to set the application to testing mode in the test fixture.

### Challenge 2: CI Pipeline Configuration
Initially, the workflow was failing because some dependencies were missing. Solution: Ensured all required packages were listed in requirements.txt.

## Conclusion
The implementation successfully demonstrates continuous integration practices for a Flask web application. The test suite provides coverage for the core functionality, and the CI pipeline ensures that code changes are tested before they are merged.