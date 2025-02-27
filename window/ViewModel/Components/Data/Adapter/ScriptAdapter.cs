using System.Linq;
using System.Threading.Tasks;
using System.Runtime.InteropServices;
using MathWindow.ViewModel.Components.Data.Fields;

namespace MathWindow.ViewModel.Components.Data.Adapter
{
	public class ScriptAdapter
	{
		private ScriptParser _parser;
		private ScriptViewModel _viewModelFactory;

		private MainViewModel _model;
		public MainViewModel Model => _model;

		public ScriptAdapter()
		{
			// _model = new MainViewModel();
			_parser = new ScriptParser();
			_viewModelFactory = new ScriptViewModel();
		}

		public async Task Some()
		{
			await Task.Run(async() => {
				await _parser.Parse("table");
				string info = _parser.Output("table");
				_model.Model.Data.Calculus.Add(new NumberExpression("Output", info));
				/*
				var info = _parser.GetInfo("table");
				_model.Model.Data.Calculus.Add(new NumberExpression(info.FileName, info.Arguments));
				*/
			});
		}

		public async Task Connect()
		{
			await _parser.ParseAll();
			// await Some();
			// await Some();

			_model = _viewModelFactory.GetMainViewModel(_parser);
		}
	}
}
