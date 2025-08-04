# vul_tracking

Vulnerability tracking for Python projects.

## Setup

### 1. Create and Activate Virtual Environment

python -m venv myenv

#### 1.1. Powershell

.\myenv\Scripts\Activate.ps1

#### 1.2. Windows CMD

myenv\Scripts\activate

### 2. Install Depedencies

pip install -r requirements.txt

## 3. Start the app

### 3.1. Start the server

uvicorn main:app --reload

### 3.2. Open in Browser

http://127.0.0.1:8000/

http://127.0.0.1:8000/docs#/

## 4. Code Formatting

black . --exclude myenv/

isort . --skip myenv

## 5. Testing

### 5.1. Unit Tests

set PYTHONPATH=.

pytest

### 5.1. Behave Tests

behave
