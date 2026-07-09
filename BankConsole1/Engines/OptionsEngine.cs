using BankConsole1.Dtos;
using BankConsole1.Interfaces;
using System;
using System.Collections.Generic;
using System.Text;
using System.Text.Json;
using System.Text.Json.Nodes;

namespace BankConsole1.Engines
{
    internal class OptionsEngine : Calculation, Ioperations
    {
        internal List<AccInfo>? accInfos;
        public OptionsEngine()
        {
            string jsonData = File.ReadAllText(@"C:\Users\mohit.parab\source\repos\BankConsole1\AccDtl.json");
            accInfos = JsonSerializer.Deserialize<List<AccInfo>>(jsonData);
        }

        public void AccDetail()
        {
            Console.Write("Enter Account No: ");
            int accNo = Convert.ToInt32(Console.ReadLine());
            var accInfo = accInfos?.FirstOrDefault(x => x.AccNo == accNo);
            if (accInfo != null)
            {
                Console.WriteLine("Account Detail");
                Console.WriteLine(JsonSerializer.Serialize(accInfo));
                Console.WriteLine("*****************");
                
            }
            else
            {
                Console.Write("Account not present");
            }
        }

        public void CreateAcc()
        {
            DateTime now = DateTime.Now;
            AccInfo accInfo = new AccInfo();
            AddresInfo addres = new AddresInfo();
            Console.Write("Full Name: ");
            accInfo.Name = Console.ReadLine();
            Console.Write("City: ");
            addres.City = Console.ReadLine();
            Console.Write("State: ");
            addres.State = Console.ReadLine();
            Console.Write("Pin: ");
            addres.Pin = Convert.ToInt32(Console.ReadLine());
            accInfo.Date = now.ToString("dd/MM/yyyy");
            accInfo.Balance = 0;
            accInfo.AccNo = Convert.ToInt32(now.ToString("mmHHss"));
            accInfo.Addres = addres;
            accInfos?.Add(accInfo);
        }

        public void DeleteAcc()
        {
            Console.Write("Account Number");
            int accNo = Convert.ToInt32(Console.ReadLine());
            int delInd = Convert.ToInt32(accInfos?.FindIndex(x => x.AccNo == accNo));
            if (delInd >= 0)
            {
                accInfos.RemoveAt(delInd);
            }
        }

        public void DepositMony()
        {

            Console.Write("Enter Account No: ");
            int accNo = Convert.ToInt32(Console.ReadLine());
            var accInfo = accInfos?.FirstOrDefault(x => x.AccNo == accNo);
            if (accInfo != null)
            {
                Console.Write("Enter your amount: ");
                int amount = Convert.ToInt32(Console.ReadLine());
                if (amount > 0 && amount < 10000)
                {
                    //accInfo.Balance += amount;
                    Addition(accInfo, amount);
                }
                else
                {
                    Console.Write("Enter correct amount");
                }
            }
            else
            {
                Console.Write("Account not present");
            }
        }

        public void UpdateAcc()
        {
            Console.Write("Full Name: ");
            string accNam = Console.ReadLine() ?? "";
            Console.Write("Pin: ");
            int accPin = Convert.ToInt32(Console.ReadLine());

            var accInfo = accInfos?.FirstOrDefault(x => x.Name == accNam && x.Addres?.Pin == accPin);
            if (accInfo == null)
            {
                Console.WriteLine("Account is not present");
                return;
            }
            Console.WriteLine("Update city type - 1");
            Console.WriteLine("Update state type - 2");
            string option = Console.ReadLine();
            if (option == "1")
            {
                Console.Write("City name: ");
                accInfo.Addres?.City = Console.ReadLine();
            }
            else if (option == "2")
            {
                Console.Write("State name: ");
                accInfo.Addres?.State = Console.ReadLine();
            }
            else
            {
                Console.WriteLine("Choose proper option fucker");
            }
        }

        public void WithwrewMony()
        {
            Console.Write("Enter Account No: ");
            int accNo = Convert.ToInt32(Console.ReadLine());
            var accInfo = accInfos?.FirstOrDefault(x => x.AccNo == accNo);
            if (accInfo != null)
            {
                Console.Write("Enter your amount: ");
                int amount = Convert.ToInt32(Console.ReadLine());
                if (amount > 0 && amount < 10000)
                {
                    //accInfo.Balance += amount;
                    Substraction(accInfo, amount);
                }
                else
                {
                    Console.Write("Enter correct amount");
                }
            }
            else
            {
                Console.Write("Account not present");
            }
        }
    }
}
