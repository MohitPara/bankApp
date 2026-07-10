using System;
using System.Collections.Generic;
using System.Text;

namespace BankConsole1.Dtos
{
    public class AccInfo
    {
        public string? Name { get; set; }
        public string? Date { get; set; }
        public int Balance { get; set; }
        public int AccNo { get; set; }
        public AddresInfo? Addres { get; set; }
    }

    public class AddresInfo
    {
        public int? Pin { get; set; }
        public string? City { get; set; }
        public string? State { get; set; }
    }

    public class AddresInfotest
    {
        public int? Pin { get; set; }
        public string? City { get; set; }
        public string? State { get; set; }
    }
}
