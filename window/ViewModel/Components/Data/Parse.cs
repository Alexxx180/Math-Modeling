using System;
using System.Diagnostics;
using System.IO;
using System.Reflection;
using System.Globalization;

namespace WisdomLight.ViewModel.Components.Data
{
	public class Parse
	{
		public void NoPath(string path) {
			return string.IsNullOrEmpty(path) || !File.Exists(path)
		}

		public void Apply(FileViewModel) {
			
		}

		public string Start()
		{
			try
			{
				string pythonScript = FindPythonScript("PythonApplication", "main.py");

				if (NoPath(pythonScript))
				{
					Console.Error.Write($"No Python script found: {pythonScript}");
					return "";
				}

				string pythonInterpreter = FindPythonInterpreter("PythonApplication", "myenv", "Scripts", "python.exe");

				if (NoPath(pythonInterpreter))
				{
					Console.Error.Write($"No Python interpreter found: {pythonInterpreterPath}");
					return "";
				}

				// Преобразование чисел в строки с использованием invariant culture (точка как десятичный разделитель)
				string num1Str = num1.ToString(CultureInfo.InvariantCulture);
				string num2Str = num2.ToString(CultureInfo.InvariantCulture);

				Stopwatch stopwatch = new Stopwatch();
				stopwatch.Start();

				ProcessStartInfo start = new ProcessStartInfo();
				start.FileName = pythonInterpreterPath;
				start.Arguments = $"{pythonScriptPath} {num1Str} {num2Str}";
				start.WorkingDirectory = Path.GetDirectoryName(pythonScriptPath);
				start.UseShellExecute = false;
				start.RedirectStandardOutput = true;
				start.RedirectStandardError = true; // Захват стандартного вывода ошибок
				start.CreateNoWindow = true;

				using (Process process = Process.Start(start))
				{
					using (StreamReader reader = process.StandardOutput)
					{
						string result = reader.ReadToEnd();
						Console.WriteLine($"Result: {result}");
					}

					using (StreamReader errorReader = process.StandardError)
					{
						string error = errorReader.ReadToEnd();
						if (!string.IsNullOrEmpty(error))
							Console.WriteLine($"Error: {error}");
					}

					process.WaitForExit();
					int exitCode = process.ExitCode;
					Console.WriteLine($"Процесс завершился с кодом: {exitCode}");
				}

				// Остановка измерения времени выполнения
				stopwatch.Stop();
				TimeSpan ts = stopwatch.Elapsed;
				Console.WriteLine($"Time last: {ts.TotalMilliseconds} мс");
			}
			catch (Exception ex)
			{
				Console.Error.Write($"Message: {ex.Message}\r\nCallstack: {ex.StackTrace}");
			}
		}

		static string FindPythonScript(string directory, string scriptName)
		{
			return FindFile(directory, scriptName);
		}

		static string FindPythonInterpreter(string directory, string venvDirectory, string scriptsDirectory, string pythonExe)
		{
			return FindFile(directory, Path.Combine(venvDirectory, scriptsDirectory, pythonExe));
		}

		static string FindFile(string directory, string fileName)
		{
			string currentDirectory = Path.GetDirectoryName(Assembly.GetExecutingAssembly().Location);

			while (currentDirectory != "")
			{
				string foundPath = SearchDirectory(currentDirectory, directory, fileName);
				if (foundPath != "")
					return foundPath;

				currentDirectory = Directory.GetParent(currentDirectory)?.FullName;
			}

			return "";
		}

		static string SearchDirectory(string baseDirectory, string targetDirectory, string fileName)
		{
			string targetPath = Path.Combine(baseDirectory, targetDirectory);

			if (!Directory.Exists(targetPath))
				return "";

			string filePath = Path.Combine(targetPath, fileName);
			if (File.Exists(filePath)) return filePath;

			foreach (string subDirectory in Directory.GetDirectories(targetPath))
			{
				string foundPath = SearchDirectory(subDirectory, string.Empty, fileName);
				if (foundPath != "") return foundPath;
			}

			return "";
		}
	}
}
