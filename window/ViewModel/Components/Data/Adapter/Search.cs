using System.Linq;
using System.Reflection;

namespace MathWindow.ViewModel.Components.Data.Adapter
{
	public static class Search
	{
		public static int Variant()
		{
			string variantPath = File("project", "variant.txt");
			System.Console.WriteLine("Path to variant: ", variantPath);
			return System.Convert.ToInt32(System.IO.File.ReadAllText(variantPath));
		}

		public static string Python(string folder)
		{
			string path = System.IO.Path.Combine("myenv", "Scripts", "python.exe");
			return File(folder, path);
		}

		public static string File(string directory, string name)
		{
			Assembly exe = Assembly.GetExecutingAssembly();

			string current = System.IO.Path.GetDirectoryName(exe.Location);
			string path = Folder(current, directory, name);

			while ((current != string.Empty) && (path == string.Empty))
			{
				current = System.IO.Directory.GetParent(current)?.FullName;
				path = Folder(current, directory, name);
			}

			return path;
		}

		public static string Folder(string basis, string target, string name)
		{
			string path = System.IO.Path.Combine(basis, target);
			if (!System.IO.Directory.Exists(path))
				return string.Empty;

			string result = System.IO.Path.Combine(path, name);
			if (System.IO.File.Exists(result))
				return result;

			result = string.Empty;
			string[] folders = System.IO.Directory.GetDirectories(path).ToArray();
			int i = folders.Length;

			while ((--i >= 0) && (result == string.Empty))
				result = Folder(folders[i], string.Empty, name);

			return result;
		}
	}
}
