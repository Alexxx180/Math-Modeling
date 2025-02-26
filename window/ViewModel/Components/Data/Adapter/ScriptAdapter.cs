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
		private int _variant;

		public ScriptAdapter()
		{
			_variant = 8;
			_model = new MainViewModel();
			_parser = new ScriptParser(_variant);
			_viewModelFactory = new ScriptViewModel();
			//_variant = Search.Variant();
		}

		public async Task Some()
		{
			await Task.Run(() => { _model.Model.Data.Calculus.Add(NumberExpression.Default); });
		}

		public async Task Connect()
		{
			await _parser.ParseAll();
			// await Some();
			// await Some();

			//return _viewModelFactory.GetMainViewModel(_parser);
		}
	}
}
