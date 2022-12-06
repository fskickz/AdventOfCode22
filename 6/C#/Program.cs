string line = File.ReadAllText("/Users/semreiestad/Documents/AdventOfCode22/6/input.txt").Trim();


int Uniqueness(string s, int length)
{
    for (int i = length; i < line.Length; i++)
    {
        var unique = line.Substring((i - length), length).ToHashSet();
        if (unique.Count() == length)
        {
            return i;
        }
    }
    return 0;
}

Console.WriteLine(Uniqueness(line, 4));
Console.WriteLine(Uniqueness(line, 14));