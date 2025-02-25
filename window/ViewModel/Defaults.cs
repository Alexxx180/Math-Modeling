using System;
using System.IO;
using System.Linq;
using System.Collections.Generic;

namespace WisdomLight.ViewModel
{
	public static class Defaults
	{
		public static string Runtime => Path.Combine(Environment.CurrentDirectory, "Resources", "Runtime");

		public static string[] GetLines(string file) {
			return File.ReadLines(Path.Combine(Runtime, file)).ToArray();
		}
	}
}
