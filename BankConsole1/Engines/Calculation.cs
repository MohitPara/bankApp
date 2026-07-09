using BankConsole1.Dtos;
using System;
using System.Collections.Generic;
using System.Text;

namespace BankConsole1.Engines
{
    internal class Calculation
    {
        internal void Addition(AccInfo _accInfo, int amount2)
        {
            _accInfo.Balance += amount2;
        }

        internal void Substraction(AccInfo _accInfo, int amount) 
        {
            if (0 < _accInfo.Balance - amount)
            {
                _accInfo.Balance -= amount;
            }
            else { Console.WriteLine("Insuffient Balance"); }
        }
    }
}
