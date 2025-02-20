using System.Collections.Generic;
using System.Collections.ObjectModel;

namespace WisdomLight.ViewModel.Components.Data.Fields
{
    public class GridExpression : NameLabel
    {
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
