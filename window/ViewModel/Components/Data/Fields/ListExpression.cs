using System.Collections.Generic;

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
			Name = "N/A", No = new List<string>()
		};
	}
}
