using System;
using System.Diagnostics;
using System.Reflection;
using System.Globalization;
using System.Threading.Tasks;
using System.Collections.Generic;
using static System.Console;

namespace MathWindow.ViewModel.Components.Data.Adapter
{
	public class ScriptParser
	{
		private bool _noScripts = false;
		public bool NoScripts => _noScripts;

		private string[] _kinds;
		public string[] Kinds => _kinds;

		private string _script = "main.py", _app = "project", _interpreter;
		private Dictionary<string, string> _result, _error, _exit;

		public bool HasError(string kind) => _error.ContainsKey(kind);

		public string Output(string kind) => _result[kind];

		public ScriptParser() {
			_kinds = new string[] { "table", "model" };
			_result = new Dictionary<string, string>();
			_error = new Dictionary<string, string>();
			_exit = new Dictionary<string, string>();
			/*
			_script = Search.File(_app, _script);
			_interpreter = Search.Python(_app);
			*/
			_script = NoPath(Search.File(_app, _script), nameof(_script));
			_interpreter = NoPath(Search.Python(_app), nameof(_interpreter));
		}

		private string NoPath(string path, string name)
		{
			_noScripts |= string.IsNullOrEmpty(path) || !System.IO.File.Exists(path);
			if (_noScripts)
			{
				// Error.WriteLine($"No Python {name} found: {path}");
			}
			return path;
		}

		private void Results(TimeSpan elapsed, string kind)
		{
			// string output = HasError(kind) ?
				// $"Error: {_error[kind]}" : $"Result: {_result[kind]}";
			/*
			WriteLine($"Time last: {elapsed.TotalMilliseconds} ms");
			WriteLine(_exit[kind]);
			WriteLine(output);
			// */
		}

		internal ProcessStartInfo GetInfo(string kind)
		{
			string limiter = " ";
			return new ProcessStartInfo()
			{
				FileName = _interpreter,
				Arguments = string.Join(limiter, _script, kind),
				WorkingDirectory = System.IO.Path.GetDirectoryName(_script),
				UseShellExecute = false,
				RedirectStandardOutput = true,
				RedirectStandardError = true,
				CreateNoWindow = true
			};
		}

		public void Parse(string kind)
		{
			Stopwatch time = new Stopwatch();
			try
			{
				time.Start();

				ProcessStartInfo info = GetInfo(kind);
				using (Process process = Process.Start(info))
				{
					using (System.IO.StreamReader reader = process.StandardOutput)
					{
						_result[kind] = reader.ReadToEnd();
					}
					using (System.IO.StreamReader errorReader = process.StandardError)
					{
						_error[kind] = errorReader.ReadToEnd();
					}
					process.WaitForExit();
					_exit[kind] = $"Process exit with code: {process.ExitCode}";
					System.IO.File.WriteAllText($"C:/{kind}-ok.txt", _exit[kind]);
				}
			}
			catch (Exception ex)
			{
				System.IO.File.WriteAllText($"C:/{kind}-error.txt", $"Message: '{ex.Message}', Callstack: {ex.StackTrace}");
				// Error.Write($"Message: '{ex.Message}', Callstack: {ex.StackTrace}");
			}
			finally
			{
				time.Stop();
			}
			Results(time.Elapsed, kind);
		}

		public async Task ParseAll()
		{
			// List<Task> tasks = new List<Task>();
			/* for (byte i = 0; i < 2; i++)
			{
				var LastTask = new Task(SomeFunction);
				LastTask.Start();
				TaskList.Add(LastTask);
			}
			var task1 = Parse();*/

			// /*
			await Task.Run(() => { Parse("table"); });
			await Task.Run(() => { Parse("model"); });
			/*	// Task.Factory.StartNew(Parse),
				//Task.Factory.StartNew(Parse)
			}; */
			// await Task.WaitAll(tasks); // */
		}

	}
}
