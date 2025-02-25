using System.Linq;
using System.Threading.Tasks;

namespace MathWindow.ViewModel.Components.Data.Adapter
{
	public class ScriptAdapter
	{
		private ScriptParser _parser;
		private ScriptViewModel _viewModelFactory;
		private int _variant = 8;

		public ScriptAdapter()
		{
			_parser = new ScriptParser(_variant);
			_viewModelFactory = new ScriptViewModel();
			_variant = Search.Variant();
		}

		public MainViewModel Connect()
		{
			return _viewModelFactory.GetMainViewModel(_parser);
		}
	}
}
