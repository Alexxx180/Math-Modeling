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
		private Dictionary<string, string> _result;

		public string Output(string kind)
		{
			string output;
			if (_result.TryGetValue(kind, out output)) return output;
			return string.Empty;
		}

		public ScriptParser() {
			_kinds = new string[] { "table", "model" };
			_result = new Dictionary<string, string>();
			_script = NoPath(Search.File(_app, _script), nameof(_script));
			_interpreter = NoPath("C:\\Python312\\python.exe", nameof(_interpreter)); // Defaults.Config.Paths.Python
		}

		private string NoPath(string path, string name)
		{
			_noScripts |= string.IsNullOrEmpty(path) || !System.IO.File.Exists(path);
			if (_noScripts) { Log($"no-{name}", $"No path found: {path}"); }
			return path;
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

		private void Log(string status, string message)
		{
			System.IO.File.WriteAllText($"{Environment.CurrentDirectory}/{status}.txt", message);
		}

		private void Log(Stopwatch time, string status, string message)
		{
			time.Stop();
			message = $"[{DateTime.Now}] {message} - Time {time.Elapsed} ms";
			Log(status, message);
		}

		public async Task Parse(string kind)
		{
			string errors = "";
			Stopwatch time = new Stopwatch();
			try
			{
				time.Start();

				ProcessStartInfo info = GetInfo(kind);
				using (Process process = Process.Start(info))
				{
					await Task.Run(() => {
						using (System.IO.StreamReader reader = process.StandardOutput)
						{
							_result[kind] = reader.ReadToEnd();
						}
					});
					await Task.Run(() => {
						using (System.IO.StreamReader errorReader = process.StandardError)
						{
							errors = errorReader.ReadToEnd();
						}
					});
					process.WaitForExit();
					Log(time, $"{kind}-ok", $"Process exit with code: {process.ExitCode}. {errors}");
				}
			}
			catch (Exception ex)
			{
				Log(time, $"{kind}-error", $"MSG: '{ex.Message}', Calls: {ex.StackTrace}, ERR: {errors}");
			}
		}

		public async Task ParseAll()
		{
			await Task.Run(async() => { await Parse("table"); });
			await Task.Run(async() => { await Parse("model"); });
		}

	}
}
