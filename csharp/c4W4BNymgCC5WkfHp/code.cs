public class Program
    {
        public static string NameShuffle(string str)
        {
            return str.Split()[1] + ' ' + str.Split()[0];
        }
    }