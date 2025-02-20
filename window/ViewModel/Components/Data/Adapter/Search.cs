using System.IO;

namespace WisdomLight.ViewModel.Components.Data.Adapter
{
	public static class Search
	{
		public static int Variant()
		{
			string variantPath = Search.File("project", "variant.txt");
			Console.WriteLine("Path to variant: ", variantPath);
			return (int)File.ReadAllText(variantPath);
		}

		public static string Python(string folder)
		{
			return File(folder, Path.Combine("myenv", "Scripts", "python.exe"));
		}

		public static string File(string directory, string name)
		{
			Assembly exe = Assembly.GetExecutingAssembly();

			string current = Path.GetDirectoryName(exe.Location);
			string path = Folder(current, directory, name);

			while ((current != string.Empty) && (path == string.Empty))
			{
				current = Directory.GetParent(current)?.FullName;
				path = Folder(current, directory, name);
			}

			return path;
		}

		public static string Folder(string basis, string target, string name)
		{
			string path = Path.Combine(basis, target);
			if (!Directory.Exists(path))
				return string.Empty;

			string result = Path.Combine(path, name);
			if (File.Exists(result))
				return result;

			result = string.Empty;
			string[] folders = Directory.GetDirectories(path);
			int i = folders.Length;

			while ((--i >= 0) && (result == string.Empty))
				result = Folder(folders[i], string.Empty, name);

			return result;
		}
	}
}
