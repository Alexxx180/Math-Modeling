using System;
using System.IO;
using System.Linq;
using System.Collections.Generic;

namespace MathWindow.ViewModel
{
	public static class Defaults
	{
		public static string NoValue = "N/A";

		public static string Runtime => Path.Combine(Environment.CurrentDirectory, "Resources", "Runtime");

		public static string[] GetLines(string file) {
			return File.ReadLines(Path.Combine(Runtime, file)).ToArray();
		}
	}
}
