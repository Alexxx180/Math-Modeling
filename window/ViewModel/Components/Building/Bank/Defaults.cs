using System;
using System.IO;

namespace WisdomLight.ViewModel.Components.Building.Bank
{
    public static class Defaults
    {
        public static string Runtime => Path.Combine(Environment.CurrentDirectory, "Resources", "Runtime");

		public static IEnumerable<string> GetLines(string file) {
			return File.ReadLines(Path.Combine(Runtime, file));
		}
    }
}
