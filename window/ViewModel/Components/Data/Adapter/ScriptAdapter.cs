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
			_parser = new ScriptParser();
			_viewModelFactory = new ScriptViewModel();
		}

		public async Task Connect()
		{
			//_model = new MainViewModel { Table = FileViewModel.Default, Model = FileViewModel.Default };
			await _parser.ParseAll();
			_model = _viewModelFactory.GetMainViewModel(_parser);
		}
	}
}
