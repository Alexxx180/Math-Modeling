using System;

namespace MathWindow.ViewModel.Config
{
	public class ConfigPaths
	{
		public ConfigPaths(string[] config)
		{
			Python = config[0];
		}

		public string Python { get; set; }
	}
}
