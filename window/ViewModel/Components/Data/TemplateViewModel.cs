using System.IO;
using System.Collections.Generic;
using System.Collections.ObjectModel;
using MathWindow.ViewModel.Components.Data.Fields;

namespace MathWindow.ViewModel.Components.Data
{
	public class TemplateViewModel : NameLabel
	{
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

		private ObservableCollection<ListExpression> _data;
		public ObservableCollection<ListExpression> Data
		{
			get => _data;
			set
			{
				_data = value;
				OnPropertyChanged();
			}
		}

		private ObservableCollection<GridExpression> _result;
		public ObservableCollection<GridExpression> Result
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
