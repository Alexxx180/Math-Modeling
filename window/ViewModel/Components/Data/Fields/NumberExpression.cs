using MathWindow.ViewModel.Config;

namespace MathWindow.ViewModel.Components.Data.Fields
{
	public class NumberExpression : NameLabel
	{
		private string _no;
		public string No
		{
			get => _no;
			set
			{
				_no = value;
				OnPropertyChanged();
			}
		}

		public static NumberExpression Default = new NumberExpression
		{
			Name = Defaults.NoValue,
			No = Defaults.NoValue
		};

		public ConfigMargin Margin => Defaults.Config.Margin;
	}
}
