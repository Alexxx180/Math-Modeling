using System.IO;
using System.Collections.ObjectModel;
using System.Collections.Generic;
using MathWindow.ViewModel.Components.Data.Fields;
using MathWindow.ViewModel;

namespace MathWindow.ViewModel.Components.Data.Adapter
{
	public class ScriptViewModel
	{
		private static string _total = " - ", _lists = " + ", _list = ", ", _no = "";

		private ObservableCollection<NumberExpression> _calculus;
		private ObservableCollection<ListExpression> _data;
		private ObservableCollection<GridExpression> _result;
		private List<FileViewModel> _model;

		public delegate void Add(string field, string[] output);

		private Dictionary<string, Add> _func;

		public ScriptViewModel()
		{
			_func = new Dictionary<string, Add>
			{
				{ _lists, AddResult }, { _list, AddData }, { _no, AddCalculus }
			};
		}

		private string CheckEmptyString(string cell)
		{
			return cell.Contains("''") ? cell.Replace("'", "") : cell;
		}

		private List<string> GetRow(string[] cells)
		{
			List<string> result = new List<string>();
			foreach(string cell in cells) result.Add(CheckEmptyString(cell));
			return result;
		}

		private void AddResult(string field, string[] output)
		{
			GridExpression values = new GridExpression
			{
				Name = field,
				No = new ObservableCollection<List<string>>()
			};
			foreach(string text in output) values.No.Add(GetRow(text.Split(_list)));
			_result.Add(values);
		}

		private void AddData(string field, string[] output)
		{
			_data.Add(new ListExpression
			{
				Name = field,
				No = GetRow(output)
			});
		}

		private void AddCalculus(string field, string[] output)
		{
			_calculus.Add(new NumberExpression { Name = field, No = output[0] });
		}

		private FileViewModel SetupModel()
		{
			return new FileViewModel
			{
				Data = new TemplateViewModel()
				{
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
			// 
			// return SetupModel();

			//string[] fields = new string[] { "1", "2", "3", "4", "5", "6", "7", "8", "9" };
			//string[] fields = Defaults.GetLines($"fields/{kind}.txt");
			string[] fields = Defaults.Config.Fields[kind];
			string[] values = output.Split(_total);

			int length = values.Length;
			while (--length >= 0) {
				string sequence = values[length];
				bool search = true;

				foreach (KeyValuePair<string, Add> entry in _func)
					if (search && sequence.Contains(entry.Key))
					{
						entry.Value(fields[length], sequence.Split(entry.Key));
						search = false;
					}
			}
			return SetupModel();
		}

		public MainViewModel GetMainViewModel(ScriptParser parser)
		{
			// return new MainViewModel { Table = FileViewModel.Default, Model = FileViewModel.Default };
			_model = new List<FileViewModel>();

			foreach(string kind in parser.Kinds)
				_model.Add(GetModel(parser.Output(kind), kind));

			return new MainViewModel { Table = _model[0], Model = _model[1], Evenly = _model[2] };
		}
	}
}
