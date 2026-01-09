# Payment Service

The Payment Service is responsible for processing bill payments.
It simulates integration with an external payment provider and delegates
money transfer execution to the Transaction Service.

This service does NOT directly manipulate account balances.

## Run
conda create -n transaction-service python=3.14
conda activate transaction-service
pip install -r requirements.txt
uvicorn server:app --port 8003