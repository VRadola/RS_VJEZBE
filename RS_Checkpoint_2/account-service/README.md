# Account Service

Manages account balances.

## Run
conda create -n account-service python=3.14
conda activate account-service
pip install -r requirements.txt
uvicorn server:app --port 8001

## JWT
Requires Authorization header.