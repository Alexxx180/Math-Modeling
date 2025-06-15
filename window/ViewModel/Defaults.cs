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

		public static string GetLine(string file) {
			return File.ReadAllText(Path.Combine(Runtime, file));
		}

		private Defaults()
		{
			Fonts = new ConfigFonts(GetLines($"custom/fonts.txt"));
			Colors = new ConfigColors(GetLines($"custom/colors.txt"));
			Margin = new ConfigMargin(GetLines($"custom/margin.txt"));
			Paths = new ConfigPaths(GetLines($"paths.txt"));
			Fields = new Dictionary<string, string[]>
			{
				{ "table", GetLines("fields/table.txt") },
				{ "model", GetLines("fields/model.txt") },
                { "evenly", GetLines("fields/evenly.txt") }
            };
		}

		public Dictionary<string, string[]> Fields { get; set; }
		public ConfigColors Colors { get; set; }
		public ConfigMargin Margin { get; set; }
		public ConfigPaths Paths { get; set; }
		public ConfigFonts Fonts { get; set; }

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
