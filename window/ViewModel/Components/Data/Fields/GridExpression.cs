using System.Collections.Generic;
using System.Collections.ObjectModel;

namespace MathWindow.ViewModel.Components.Data.Fields
{
	public class GridExpression : NameLabel
	{
		public readonly string Orientation = "Vertical";

		public GridExpression() {}

		private ObservableCollection<List<string>> _no;
		public ObservableCollection<List<string>> No
		{
			get => _no;
			set
			{
				_no = value;
				OnPropertyChanged();
			}
		}

		public static GridExpression Default = new GridExpression
		{
			Name = "N/A", No = new ObservableCollection<List<string>>()
		};
	}
}
