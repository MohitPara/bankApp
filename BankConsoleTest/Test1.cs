using BankConsole1.Dtos;
using System.Text.Json;

namespace BankConsoleTest
{
    [TestClass]
    public sealed class Test1
    {
        [TestMethod]
        public void TestMethod1()
        {
            string jsonData = File.ReadAllText(@"C:\Users\mohit.parab\source\repos\BankConsole1\AccDtl.json");
            List<AccInfo>? accInfo = JsonSerializer.Deserialize<List<AccInfo>>(jsonData);
        }
    }
}
