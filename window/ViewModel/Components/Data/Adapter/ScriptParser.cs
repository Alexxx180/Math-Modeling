using System;
using System.Diagnostics;
using System.IO;
using System.Reflection;
using System.Globalization;
using System.Threading.Tasks;
using System.Collections.Generic;
using static System.Console;

namespace WisdomLight.ViewModel.Components.Data.Adapter
{
	public class ScriptParser
	{
		private bool _noScripts = false;
		public bool NoScripts => _noScripts;

		private string _script = "main.py", _app = "project", _interpreter;
		private Dictionary<string, string> _result, _error, _exit;

		public bool HasError(string kind) => _error.ContainsKey(kind);

		public string Output(string kind) => _result[kind];

		public ScriptParser() {
			_result = new Dictionary<string, string>();
			_error = new Dictionary<string, string>();

			_script = NoPath(Search.File(_app, _script), nameof(script));
			_interpreter = NoPath(Search.Python(_app), nameof(interpreter));
		}

		private bool NoPath(string path, string name)
		{
			_noScripts |= string.IsNullOrEmpty(path) || !File.Exists(path);
			if (_noScripts) Error.WriteLine($"No Python {name} found: {path}");
			return result;
		}

		private void Results(TimeSpan elapsed, string kind)
		{
			WriteLine($"Time last: {elapsed.TotalMilliseconds} ms");
			WriteLine(_exit[kind]);

			string output = HasError(kind) ?
				$"Error: {_error[kind]}" : $"Result: {_result[kind]}";
			WriteLine(output);
		}

		private ProcessStartInfo GetInfo(int variant, string kind)
		{
			return new ProcessStartInfo()
			{
				FileName = _interpreter,
				Arguments = " ".Join(_script, kind, variant),
				WorkingDirectory = Path.GetDirectoryName(_script),
				UseShellExecute = false,
				RedirectStandardOutput = true,
				RedirectStandardError = true,
				CreateNoWindow = true
			};
		}

		public async Task Parse(int variant, string kind)
		{
			try
			{
				Stopwatch time = new Stopwatch();
				time.Start();

				ProcessStartInfo info = GetInfo(variant, kind);
				using (Process process = Process.Start(info))
				{
					using (StreamReader reader = process.StandardOutput)
					{
						_result[kind] = reader.ReadToEnd();
					}
					using (StreamReader errorReader = process.StandardError)
					{
						_error[kind] = errorReader.ReadToEnd();
					}
					process.WaitForExit();
					_exit[kind] = $"Process exit with code: {process.ExitCode}";
				}
				time.Stop();
			}
			catch (Exception ex)
			{
				Error.Write($"Message: '{ex.Message}', Callstack: {ex.StackTrace}");
			}
			Results(time.Elapsed, kind);
		}
	}
}
