using System.Linq;
using System.Threading.Tasks;

namespace WisdomLight.ViewModel.Components.Data.Adapter
{
	public class ScriptAdapter
	{
		private ScriptParser _parser;
		private ScriptViewModel _viewModelFactory;
		private int _variant;

		public ScriptAdapter()
		{
			_parser = new ScriptParser();
			_viewModelFactory = new ScriptViewModel();
			_variant = Search.Variant();
		}

		public MainViewModel Connect()
		{
			string[] kinds = { "table", "model" };
			Task.WaitAll(kinds.ForEach(i => _parser.Parse(_variant, kind)));

			return _viewModelFactory.GetMainViewModel(_parser, kinds);
		}
	}
}
