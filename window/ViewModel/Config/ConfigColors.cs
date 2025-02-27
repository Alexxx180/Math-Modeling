using System;

namespace MathWindow.ViewModel.Config
{
	public class ConfigColors
	{
		public ConfigColors(string[] config)
		{
			Overall = config[0];
		}

		public string Overall { get; set; }
	}
}
