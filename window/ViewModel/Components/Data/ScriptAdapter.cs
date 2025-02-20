using System;
using System.Diagnostics;
using System.IO;
using System.Reflection;
using System.Globalization;
using static System.Console;

namespace WisdomLight.ViewModel.Components.Data
{
	public class ScriptAdapter
	{
		private ObservableCollection<NumberExpression> _calculus;
		private ListExpression data;
		private GridExpression result;

		private void NoPath(string path)
		{
			return string.IsNullOrEmpty(path) || !File.Exists(path)
		}

		private void AddResult(string[] output)
		{

		}

		private void AddResult(string[] output)
		{

		}

		private void AddCalculus(string output)
		{
			_data
		}

		public FileViewModel GetModel(string output)
		{
			string limiter = " + ", comma = ", ";
			_calculus = new ObservableCollection<NumberExpression>();
			_data = new ListExpression();
			_result = new GridExpression();

			string[] fields = GetLines($"{kind}/fields.txt");
			string[] values = output.Split(" - ");

			int length = values.Length
			while (--length >= 0) {
				string field = values[length];
				if (field.Contains(limiter))
				{
					AddResult(fields[length], field.Split(limiter));
				}
				else if (field.Contains(comma))
				{
					AddData(fields[length], field.Split(comma));
				}
				else
				{
					AddCalculus(fields[length], field);
				}
			}

			return new FileViewModel($"{kind}/config.txt")
			{
				Data = new TemplateViewModel() {
					Calculus = calculus,
					Data = data,
					Result = result
				}
			};
		}

		public MainViewModel ParsePython(string[] kinds)
		{
			MainViewModel main = new MainViewModel();
			string table = ParsePython(main.Model[0].Data.Kind);
			string model = ParsePython(main.Model[1].Data.Kind);

			string[] lines = File.ReadAllLines($"{Runtime}/{kind}/fields.txt");
			string[] 

			foreach(string field in lines) {
				calculus.Add(new NumberExpression(field, ));
			}

			Calculus = calculus;
			RandomValues = RandomValues;
		}

		private void Results(TimeSpan elapsed, string result, string error)
		{
			WriteLine($"Time last: {elapsed.TotalMilliseconds} ms");
			WriteLine($"Process exit with code: {exitCode}");

			string output = string.IsNullOrEmpty(error) ?
				$"Result: {result}" : $"Error: {error}";

			WriteLine(output);
		}

		public string Apply(string kind)
		{
			string error, app = "PythonApplication", result = "";
			int variant, exitCode;
			try
			{
				string variantPath = FindFile(app, "variant.txt")
				WriteLine("Path to variant: ", variantPath);

				variant = (int)File.ReadAllText(variantPath);

				string pythonScript = FindScript(app, "main.py");

				if (NoPath(pythonScript))
				{
					Error.WriteLine($"No Python script found: {pythonScript}");
					return "";
				}

				string interpreter = GetPython(app, "myenv", "Scripts", "python.exe");

				if (NoPath(interpreter))
				{
					Error.WriteLine($"No Python interpreter found: {interpreter}");
					return "";
				}

				Stopwatch stopwatch = new Stopwatch();
				stopwatch.Start();

				ProcessStartInfo start = new ProcessStartInfo()
				{
					FileName = interpreter,
					Arguments = $"{script} {kind} {variant}",
					WorkingDirectory = Path.GetDirectoryName(pythonScript),
					UseShellExecute = false,
					RedirectStandardOutput = true,
					RedirectStandardError = true,
					CreateNoWindow = true
				};

				using (Process process = Process.Start(start))
				{
					using (StreamReader reader = process.StandardOutput)
					{
						result = reader.ReadToEnd();
					}
					using (StreamReader errorReader = process.StandardError)
					{
						error = errorReader.ReadToEnd();
					}
					process.WaitForExit();
					exitCode = process.ExitCode;
				}

				stopwatch.Stop();
			}
			catch (Exception ex)
			{
				Error.Write($"Message: {ex.Message}\r\nCallstack: {ex.StackTrace}");
			}


			return result;
		}

		private string FindScript(string directory, string scriptName)
		{
			return FindFile(directory, scriptName);
		}

		private string GetPython(string directory, string venv, string scripts, string exe)
		{
			return FindFile(directory, Path.Combine(venv, scripts, exe));
		}

		private string FindFile(string directory, string fileName)
		{
			string path, current = Path.GetDirectoryName(Assembly.GetExecutingAssembly().Location);

			while (current != "")
			{
				path = SearchDirectory(current, directory, fileName);
				if (path != "") return path;
				current = Directory.GetParent(current)?.FullName;
			}

			return "";
		}

		private string SearchDirectory(string baseDirectory, string targetDirectory, string fileName)
		{
			string targetPath = Path.Combine(baseDirectory, targetDirectory);

			if (!Directory.Exists(targetPath))
				return "";

			string filePath = Path.Combine(targetPath, fileName);
			if (File.Exists(filePath)) return filePath;

			foreach (string subDirectory in Directory.GetDirectories(targetPath))
			{
				string path = SearchDirectory(subDirectory, string.Empty, fileName);
				if (path != "") return path;
			}

			return "";
		}
	}
}
