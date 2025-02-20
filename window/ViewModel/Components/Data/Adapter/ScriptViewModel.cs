using System.IO;
using System.Collections.ObjectModel;
using WisdomLight.ViewModel.Components.Data.Fields;
using WisdomLight.ViewModel;

namespace WisdomLight.ViewModel.Components.Data.Adapter
{
	public class ScriptViewModel
	{
		private static string _lists = " + ", _list = ", ";

		private ObservableCollection<NumberExpression> _calculus;
		private ListExpression _data;
		private GridExpression _result;

		private ObservableCollection<FileViewModel> _model;

		private bool NoPath(string path)
		{
			return string.IsNullOrEmpty(path) || !File.Exists(path);
		}

		private void AddResult(string field, string[] output)
		{
			_result.Name = field;
			foreach(string text in output)
				List<string> result = new List<string>();
				string[] cells = text.Split(_list);
				foreach(string cell in cells)
					result.Add(cell);
				_result.No.Add(result);
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

		public FileViewModel GetModel(string output, string kind)
		{
			if (output == string.Empty)
				return FileViewModel.Default;

			string limiter = " + ", comma = ", ";
			_calculus = new ObservableCollection<NumberExpression>();
			_data = new ListExpression()
			{
				No = new ObservableCollection<string>()
			};
			_result = new GridExpression();

			string[] fields = Defaults.GetLines($"{kind}/fields.txt");
			string[] values = output.Split(" - ");

			int length = values.Length;
			while (--length >= 0) {
				string field = values[length];

				if (field.Contains(_lists))
				{
					AddResult(fields[length], field.Split(_lists));
				}
				else if (field.Contains(comma))
				{
					AddData(fields[length], field.Split(comma));
				}
				else
				{
					AddCalculus(fields[length], field);
				}
			}

			return new FileViewModel($"{kind}/config.txt")
			{
				Data = new TemplateViewModel() {
					Calculus = _calculus,
					Data = _data,
					Result = _result
				}
			};
		}

		public MainViewModel GetMainViewModel(ScriptParser parser, string[] kinds)
		{
			_model = new ObservableCollection<FileViewModel>();

			foreach(string kind in kinds)
				if (parser.HasError(kind))
					_model.Add(FileViewModel.Default);
				else
					_model.Add(GetModel(parser.Output(kind), kind));

			return new MainViewModel { Model = model };
		}
	}
}
