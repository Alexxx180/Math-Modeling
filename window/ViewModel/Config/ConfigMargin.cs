using System;

namespace MathWindow.ViewModel.Config
{
	public class ConfigMargin
	{
		public ConfigMargin(string[] config)
		{
			Overall = Convert.ToInt32(config[0]);
		}

		public int Overall { get; set; }
	}
}
