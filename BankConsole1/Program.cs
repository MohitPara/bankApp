// See https://aka.ms/new-console-template for more information

using BankConsole1.Engines;
using System.Text.Json;

Console.WriteLine("Creating Account - 1");
Console.WriteLine("Updating Account Detail - 2");
Console.WriteLine("Delete Account - 3");
Console.WriteLine("Depositting mony - 4");
Console.WriteLine("Withdrawing mony - 5");
Console.WriteLine("Account Detail - 6");
Console.WriteLine("");

OptionsEngine optionsEngine = new OptionsEngine();
while (true)
{
    Console.Write("Choose your option: ");
    string? option = Console.ReadLine();

    //Dev01
    string? optiontest = Console.ReadLine();

    if (!string.IsNullOrEmpty(option))
    {
        if (option == "1")
        {
            optionsEngine.CreateAcc();
            optionsEngine.CreateAcc();//Dev02
        }
        else if (option == "2")
        {
            optionsEngine.UpdateAcc();
        }
        else if (option == "3")
        {
            optionsEngine.DeleteAcc();
        }
        else if (option == "4")
        {
            optionsEngine.DepositMony();
        }
        else if (option == "5")
        {
            optionsEngine.WithwrewMony();
        }
        else if (option == "6")
        {
            optionsEngine.AccDetail();
        }
        else
        {
            Console.WriteLine("option not present fucker");
        }
        Console.WriteLine("Do you want to continue yes/no");
        Console.WriteLine("");
        string? option1 = Console.ReadLine();
        if (string.IsNullOrEmpty(option1) || option1.Trim().ToLower() != "yes")
        {
            string jData = JsonSerializer.Serialize(optionsEngine.accInfos);
            File.WriteAllText(@"C:\Users\mohit.parab\source\repos\BankConsole1\AccDtl.json", jData);
            break;
        }
    }
    else { Console.WriteLine("Choose your option correctly"); }
}
