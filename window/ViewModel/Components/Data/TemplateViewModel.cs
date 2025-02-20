using System.IO;
using System.Collections.Generic;
using System.Collections.ObjectModel;
using WisdomLight.ViewModel.Components.Data.Fields;

namespace WisdomLight.ViewModel.Components.Data
{
	public class TemplateViewModel : NameLabel
	{
		public TemplateViewModel() {}
		public TemplateViewModel(string name) {
			Name = name;
		}

		private ObservableCollection<NumberExpression> _calculus;
		public ObservableCollection<NumberExpression> Calculus
		{
			get => _calculus;
			set
			{
				_calculus = value;
				OnPropertyChanged();
			}
		}

		private ListExpression _data;
		public ListExpression Data
		{
			get => _mathVariables;
			set
			{
				_mathVariables = value;
				OnPropertyChanged();
			}
		}

		private GridExpression _result;
		public GridExpression Result
		{
			get => _grid;
			set
			{
				_grid = value;
				OnPropertyChanged();
			}
		}
	}
}
