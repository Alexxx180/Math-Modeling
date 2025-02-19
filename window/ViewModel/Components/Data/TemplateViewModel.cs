using System.IO;
using System.Collections.Generic;
using WisdomLight.ViewModel.Components.Data.Units;

namespace WisdomLight.ViewModel.Components.Data
{
	public class TemplateViewModel : NameLabel
	{
		private string Kind { get; }

		public TemplateViewModel(string kind) {
			Kind = kind;
			// var parser 

			ObservableCollection<NumberExpression> calculus = new ObservableCollection<NumberExpression>();
			ObservableCollection<NumberExpression> randomValues = new ObservableCollection<NumberExpression>();

			string[] lines = File.ReadAllLines($"{Runtime}/{kind}.txt");
			string[] 

			foreach(string field in lines) {
				calculus.Add(new NumberExpression(field, ));
			}

			Calculus = calculus;
			RandomValues = RandomValues;
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

		private ListExpression _values;
		public ListExpression Values
		{
			get => _mathVariables;
			set
			{
				_mathVariables = value;
				OnPropertyChanged();
			}
		}

		private GridExpression _grid;
		public GridExpression Grid
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
