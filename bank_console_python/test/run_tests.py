import sys
import os
import json

# Add the project root to the path
project_root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, project_root)

from dtos.acc_info import AccInfo, AddresInfo
from engines.calculation import Calculation
from engines.options_engine import OptionsEngine
from test.test_json import TestJson


def test_dtos():
    print("Testing DTOs...")
    addres = AddresInfo(pin=123456, city="Mumbai", state="Maharashtra")
    acc = AccInfo(name="Test User", date="01/01/2026", balance=1000, acc_no=123456, addres=addres)
    print(f"✓ Created account: {acc.name}, Balance: {acc.balance}")
    print()


def test_calculation():
    print("Testing Calculation Engine...")
    calc = Calculation()
    addres = AddresInfo(pin=123456, city="Mumbai", state="Maharashtra")
    acc = AccInfo(name="Test User", balance=1000, acc_no=123456, addres=addres)
    
    # Test addition
    calc.addition(acc, 500)
    print(f"✓ After deposit: Balance = {acc.balance}")
    assert acc.balance == 1500, "Addition failed"
    
    # Test subtraction
    calc.substraction(acc, 300)
    print(f"✓ After withdrawal: Balance = {acc.balance}")
    assert acc.balance == 1200, "Subtraction failed"
    
    # Test insufficient balance
    print("Testing insufficient balance...")
    calc.substraction(acc, 5000)  # Should print "Insuffient Balance"
    print(f"✓ Balance remains: {acc.balance}")
    assert acc.balance == 1200, "Should not allow withdrawal with insufficient balance"
    print()


def test_json_serialization():
    print("Testing JSON serialization...")
    addres = AddresInfo(pin=123456, city="Mumbai", state="Maharashtra")
    acc = AccInfo(name="Test User", date="01/01/2026", balance=1000, acc_no=123456, addres=addres)
    
    # Serialize to dict
    acc_dict = {
        'Name': acc.name,
        'Date': acc.date,
        'Balance': acc.balance,
        'AccNo': acc.acc_no,
        'Addres': {
            'Pin': acc.addres.pin,
            'City': acc.addres.city,
            'State': acc.addres.state
        }
    }
    
    json_str = json.dumps(acc_dict, indent=2)
    print(f"✓ Serialized to JSON:")
    print(json_str)
    
    # Deserialize back
    data = json.loads(json_str)
    assert data['Name'] == 'Test User', "Deserialization failed"
    print(f"✓ Deserialized successfully")
    print()


def test_json_file_operations():
    print("Testing JSON file operations...")
    test_file = "test_acc.json"
    
    # Create test data
    test_data = [
        {
            "Name": "Test User 1",
            "Date": "01/01/2026",
            "Balance": 1000,
            "AccNo": 123456,
            "Addres": {"Pin": 123456, "City": "Mumbai", "State": "Maharashtra"}
        }
    ]
    
    with open(test_file, 'w') as f:
        json.dump(test_data, f)
    
    # Test loading
    options_engine = OptionsEngine(test_file)
    assert options_engine.acc_infos is not None, "Failed to load data"
    assert len(options_engine.acc_infos) == 1, "Should have 1 account"
    print(f"✓ Loaded {len(options_engine.acc_infos)} account(s) from JSON file")
    
    # Clean up
    if os.path.exists(test_file):
        os.remove(test_file)
    print()


def test_interface_compliance():
    print("Testing interface compliance...")
    from interfaces.operations import IOperations
    
    # Check if OptionsEngine implements IOperations
    test_file = "test_interface.json"
    with open(test_file, 'w') as f:
        json.dump([], f)
    
    engine = OptionsEngine(test_file)
    assert isinstance(engine, IOperations), "OptionsEngine should implement IOperations"
    print("✓ OptionsEngine implements IOperations interface")
    
    # Clean up
    if os.path.exists(test_file):
        os.remove(test_file)
    print()


def run_all_tests():
    print("=" * 50)
    print("Running Bank Console Python Tests")
    print("=" * 50)
    print()
    
    try:
        test_dtos()
        test_calculation()
        test_json_serialization()
        test_json_file_operations()
        test_interface_compliance()
        
        print("=" * 50)
        print("✓ All tests passed!")
        print("=" * 50)
    except Exception as e:
        print(f"✗ Test failed: {e}")
        import traceback
        traceback.print_exc()


if __name__ == "__main__":
    run_all_tests()
