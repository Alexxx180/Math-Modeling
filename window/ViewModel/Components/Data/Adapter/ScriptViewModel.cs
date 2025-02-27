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
		private ListExpression _data;
		private GridExpression _result;

		private List<FileViewModel> _model;

		private void AddResult(string field, string[] output)
		{
			_result.Name = field;
			foreach(string text in output)
			{
				List<string> result = new List<string>();
				string[] cells = text.Split(_list);
				foreach(string cell in cells) result.Add(cell);
				_result.No.Add(result);
			}
		}

		private void AddData(string field, string[] output)
		{
			_data.Name = field;
			foreach(string data in output)
				_data.No.Add(data);
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
			_data = new ListExpression()
			{
				No = new ObservableCollection<string>()
			};
			_result = new GridExpression();

			string[] fields = Defaults.GetLines($"{kind}/fields.txt");
			string[] values = output.Split(_total);

			int length = values.Length;
			while (--length >= 0) {
				string field = values[length];

				if (field.Contains(_lists))
				{
					// AddResult(fields[length], field.Split(_lists));
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
				/*if (parser.HasError(kind))
					_model.Add(FileViewModel.Default);
				else
					_model.Add(GetModel(parser.Output(kind), kind));*/

			return new MainViewModel { Table = _model[0], Model = _model[1] };
		}
	}
}
