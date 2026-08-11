# Mahanaim cafe Customer Support AI Assistant

## Project Description

This project is an AI-powered customer support chatbot designed
for a specific business.

The chatbot uses the OpenAI API to answer customer questions
about the café.

The chatbot is restricted to business-related questions and
does not answer unrelated questions.

## Features

- Answers customer questions
- Provides business information
- Uses the OpenAI API
- Uses prompt engineering
- Restricts answers to the selected business
- Handles unknown information
- Saves conversations to output.txt

## Technologies Used

- Python
- OpenAI API
- OpenAI Python SDK
- python-dotenv
- Git and GitHub

## Project Structure

business-customer-chatbot/

├── main.py
├── openai_api.py
├── prompts.py
├── business_info.py
├── utils.py
├── output.txt
├── requirements.txt
├── README.md
├── .gitignore
└── .env

## Installation

Create a virtual environment:

python -m venv venv

Activate it:

Windows:
.\venv\Scripts\Activate.ps1

Install dependencies:

pip install -r requirements.txt

## Environment Variables

Create a .env file and add:

OPENAI_API_KEY=your_api_key_here

Do not upload the .env file to GitHub.

## Running the Application

Run:

python main.py

## Example

Customer:
What time do you close on Sunday?

Assistant:
Mahanaim Café closes at 8:00 PM on Sunday.

## Out-of-Scope Questions

If a customer asks an unrelated question, the chatbot
responds that it can only answer questions about Mahanaim Café.

## Team

Member 1 - Letema
Member 2 - Mell
Member 3 - Angeline
Member 4 - Sean