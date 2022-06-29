public class Program
{
	public static string GetFilename(string path)
	{
		
	}
}

TestsConsoleusing System;

using NUnit.Framework;



[TestFixture]

public class Tests

{

    [Test]

		[TestCase("C:/Projects/pil_tests/ascii/edabit.txt", Result= "edabit.txt")]

		[TestCase("C:/Users/johnsmith/Music/Beethoven_5.mp3", Result= "Beethoven_5.mp3")]

		[TestCase("ffprobe.exe", Result= "ffprobe.exe")]

		[TestCase("Music/Drafts/unfinished2.midi", Result= "unfinished2.midi")]

		[TestCase("C:/Users/chad/OneDrive/Desktop/Atom.lnk", Result= "Atom.lnk")]

		[TestCase("senoron/OneDrive/Desktop/DDLC-1.1.1-pc/lib/windows-i686/DDLC.exe", Result= "DDLC.exe")]

    public static string FixedTest(string n)

    {

				Console.WriteLine($"Input: {n}");

        return Program.GetFilename(n);

    }

}