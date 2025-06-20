using System.Collections.Generic;
using MathWindow.ViewModel.Config;

namespace MathWindow.ViewModel.Components.Data.Fields
{
	public class ListExpression : NameLabel
	{
		private List<string> _no;
		public List<string> No
		{
			get => _no;
			set
			{
				_no = value;
				OnPropertyChanged();
			}
		}

		public static ListExpression Default = new ListExpression
		{
			Name = Defaults.NoValue, No = new List<string>()
		};

		public ConfigMargin Margin => Defaults.Config.Margin;
	}
}
