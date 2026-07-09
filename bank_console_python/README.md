# Bank Console Python Application

This is the Python equivalent of the C# banking console application.

## Project Structure

```
bank_console_python/
├── dtos/
│   ├── __init__.py
│   └── acc_info.py          # Data Transfer Objects (AccInfo, AddresInfo)
├── engines/
│   ├── __init__.py
│   ├── calculation.py        # Calculation engine (addition, subtraction)
│   └── options_engine.py     # Main banking operations engine
├── interfaces/
│   ├── __init__.py
│   └── operations.py         # Interface definitions (IOperations, IoP)
├── test/
│   ├── __init__.py
│   └── test_json.py          # JSON testing utilities
└── program.py                # Main entry point
```

## Features

- **Create Account** - Create new bank accounts with user details
- **Update Account** - Update account address information
- **Delete Account** - Remove existing accounts
- **Deposit Money** - Add funds to accounts (max 10,000 per transaction)
- **Withdraw Money** - Withdraw funds from accounts (max 10,000 per transaction)
- **Account Details** - View account information

## Requirements

- Python 3.7 or higher

## How to Run

1. Navigate to the project directory:
   ```bash
   cd bank_console_python
   ```

2. Run the application:
   ```bash
   python program.py
   ```

3. Follow the interactive menu prompts

## Data Storage

Account data is stored in `AccDtl.json` file in JSON format. The file is automatically loaded on startup and saved when you exit the application.

## Architecture

The Python version maintains the same architectural structure as the C# version:

- **DTOs** - Data classes for account information
- **Interfaces** - Abstract base classes defining contracts
- **Engines** - Business logic implementation
  - `Calculation` - Handles balance calculations
  - `OptionsEngine` - Implements all banking operations
- **Test** - JSON testing utilities

## Differences from C# Version

1. Uses Python dataclasses instead of C# classes with properties
2. Uses Abstract Base Classes (ABC) for interfaces
3. Uses multiple inheritance for `OptionsEngine` (inherits from both `Calculation` and `IOperations`)
4. JSON file path is relative to the project root instead of hardcoded
5. Removed profanity from error messages for better user experience
