using System.Collections.ObjectModel;

namespace MathWindow.ViewModel.Components.Data.Fields
{
	public class ListExpression : NameLabel
	{
		public readonly string Orientation = "Horizontal";

		private ObservableCollection<string> _no;
		public ObservableCollection<string> No
		{
			get => _no;
			set
			{
				_no = value;
				OnPropertyChanged();
			}
		}

		public static ListExpression Default = new ListExpression()
		{
			Name = "N/A",
			No = new ObservableCollection<string>()
		};
	}
}
