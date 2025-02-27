using System;
using System.IO;
using System.Linq;
using System.Collections.Generic;
using MathWindow.ViewModel.Config;

namespace MathWindow.ViewModel
{
	public class Defaults
	{
		private static Defaults _defaults;
		private static bool _to_be_set = true;

		public static string NoValue = "N/A";
		public static string Runtime => Path.Combine(Environment.CurrentDirectory, "Resources", "Runtime");

		public static string[] GetLines(string file) {
			return File.ReadLines(Path.Combine(Runtime, file)).ToArray();
		}

		private Defaults()
		{
			Colors = new ConfigColors(Defaults.GetLines($"colors.txt"));
			Margin = new ConfigMargin(Defaults.GetLines($"margin.txt"));
			Paths = new ConfigPaths(Defaults.GetLines($"paths.txt"));
			Fields = new Dictionary<string, string[]>
			{
				{ "table", GetLines("fields/table.txt") },
				{ "model", GetLines("fields/model.txt") }
			};
		}

		public Dictionary<string, string[]> Fields { get; set; }
		public ConfigColors Colors { get; set; }
		public ConfigMargin Margin { get; set; }
		public ConfigPaths Paths { get; set; }

		public static Defaults Config
		{
			get {
				if (_to_be_set)
				{
					_to_be_set = false;
					_defaults = new Defaults();
				}
				return _defaults;
			}
		}
	}
}
