using System;

namespace MathWindow.ViewModel.Config
{
	public class ConfigFonts
	{
		public ConfigFonts(string[] config)
		{
			Overall = config[0];
			Calculus = config[1];
			Data = config[2];
			Result = config[3];
		}

		public string Overall { get; set; }
		public string Calculus { get; set; }
		public string Data { get; set; }
		public string Result { get; set; }
	}
}
