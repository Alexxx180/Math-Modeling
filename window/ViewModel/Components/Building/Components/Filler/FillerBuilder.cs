using System.IO;
using System.Windows.Input;
using WisdomLight.Model;
using WisdomLight.View;
using WisdomLight.ViewModel.Components.Building.Bank;
using WisdomLight.ViewModel.Components.Core.Commands;
using WisdomLight.ViewModel.Components.Data;

namespace WisdomLight.ViewModel.Components.Building.Filler
{
	public class FillerBuilder : IFillerBuilder
	{
		private IWindowService _windows;

		private FileViewModel _viewModel;
		private TemplateViewModel _data;

		private ICommand _syncCommand;
		private ICommand _submitCommand;

		public FillerBuilder(IWindowService windows)
		{
			_windows = windows;
		}

		public IFillerBuilder Submit()
		{
			_submitCommand = new RelayCommand(argument => _viewModel.Submit());
			return this;
		}

		public IFillerBuilder Sync()
		{
			_syncCommand = new RelayCommand(argument => _viewModel.Sync());
			return this;
		}

		public IFillerBuilder Reset()
		{
			_data = null;
			_viewModel = null;
			_submitCommand = null;
			_syncCommand = null;
			_template.Reset();
			return this;
		}

		public FileViewModel Build()
		{
			_viewModel = new FileViewModel
			{
				Data = _data,
				SyncCommand = _syncCommand,
				SubmitCommand = _submitCommand,
			};
			return _viewModel;
		}
	}
}
