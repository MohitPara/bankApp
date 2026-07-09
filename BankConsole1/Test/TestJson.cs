using BankConsole1.Dtos;
using System;
using System.Collections.Generic;
using System.Text;
using System.Text.Json;

namespace BankConsole1.Test
{
    public class TestJson
    {
        public void TestJson1() 
        {
            string jsonData = File.ReadAllText(@"C:\Users\mohit.parab\source\repos\BankConsole1\AccDtl.json");
            AccInfo? accInfo = JsonSerializer.Deserialize<AccInfo>(jsonData);
        }
    }
}
