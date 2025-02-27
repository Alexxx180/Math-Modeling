using System.IO;
using System.Collections.ObjectModel;
using System.Collections.Generic;
using MathWindow.ViewModel.Components.Data.Fields;
using MathWindow.ViewModel;

namespace MathWindow.ViewModel.Components.Data.Adapter
{
	public class ScriptViewModel
	{
		private static string _total = " - ", _lists = " + ", _list = ", ";

		private ObservableCollection<NumberExpression> _calculus;
		private ObservableCollection<ListExpression> _data;
		private ObservableCollection<GridExpression> _result;

		private List<FileViewModel> _model;

		private void AddResult(string field, string[] output)
		{
			GridExpression values = new GridExpression
			{
				Name = field,
				No = new ObservableCollection<List<string>>()
			};

			foreach(string text in output)
			{
				// /*
				string[] cells = text.Split(_list);
				List<string> result = new List<string>();
				foreach(string cell in cells) result.Add(cell);
				values.No.Add(result);
				// */
				// values.No.Add(new List<string> { text });
			}
			_result.Add(values);
		}

		private void AddData(string field, string[] output)
		{
			ListExpression listing = new ListExpression
			{
				Name = field,
				No = new ObservableCollection<string>()
			};
			foreach(string data in output) listing.No.Add(data);
			_data.Add(listing);
		}

		private void AddCalculus(string field, string output)
		{
			_calculus.Add(new NumberExpression(field, output));
		}

		public FileViewModel SetupModel()
		{
			return new FileViewModel
			{
				Data = new TemplateViewModel() {
					Calculus = _calculus,
					Data = _data,
					Result = _result
				}
			};
		}

		public FileViewModel GetModel(string output, string kind)
		{
			_calculus = new ObservableCollection<NumberExpression>();
			_data = new ObservableCollection<ListExpression>();
			_result = new ObservableCollection<GridExpression>();

			string[] fields = Defaults.GetLines($"{kind}/fields.txt");
			string[] values = output.Split(_total);

			int length = values.Length;
			while (--length >= 0) {
				string field = values[length];

				if (field.Contains(_lists))
				{
					// string f = fields[length];
					AddResult(fields[length], field.Split(_lists));
				}
				else if (field.Contains(_list))
				{
					AddData(fields[length], field.Split(_list));
				}
				else
				{
					AddCalculus(fields[length], field);
				}
			}
			// ($"{kind}/config.txt")
			return SetupModel();
		}

		public MainViewModel GetMainViewModel(ScriptParser parser)
		{
			_model = new List<FileViewModel>();

			foreach(string kind in parser.Kinds)
				_model.Add(GetModel(parser.Output(kind), kind));

			return new MainViewModel { Table = _model[0], Model = _model[1] };
		}
	}
}
