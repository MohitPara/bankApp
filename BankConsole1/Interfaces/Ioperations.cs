using System;
using System.Collections.Generic;
using System.Text;

namespace BankConsole1.Interfaces
{
    internal interface Ioperations
    {
        public void CreateAcc();
        public void UpdateAcc();
        public void DeleteAcc();
        public void DepositMony();
        public void WithwrewMony();
        public void AccDetail();
    }
}
