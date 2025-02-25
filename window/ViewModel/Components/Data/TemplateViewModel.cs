using System.IO;
using System.Collections.Generic;
using System.Collections.ObjectModel;
using MathWindow.ViewModel.Components.Data.Fields;

namespace MathWindow.ViewModel.Components.Data
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
			get => _data;
			set
			{
				_data = value;
				OnPropertyChanged();
			}
		}

		private GridExpression _result;
		public GridExpression Result
		{
			get => _result;
			set
			{
				_result = value;
				OnPropertyChanged();
			}
		}
	}
}
