public class Program
{
	public static string GetFilename(string path)
	{
		int l = path.Split('/').Length - 1;
	  	return path.Split('/')[l];
	}
}