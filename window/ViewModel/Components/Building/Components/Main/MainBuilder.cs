using System;
using System.Collections.Generic;
using System.IO;
using System.Windows.Input;
using WisdomLight.Model;
using WisdomLight.View;
using WisdomLight.ViewModel.Components.Building.Bank;
using WisdomLight.ViewModel.Components.Building.Filler;
using WisdomLight.ViewModel.Components.Core.Commands;
using WisdomLight.ViewModel.Components.Data;
using WisdomLight.ViewModel.Components.Data.Units;

namespace WisdomLight.ViewModel.Components.Building.Main
{
	public class MainBuilder : IMainBuilder
	{
		private IWindowService _windows;

		private MainViewModel _viewModel;
		private IFillerBuilder _filler;

		public ICommand _firstTab;
		public ICommand _secondTab;
		
		public MainBuilder(IWindowService windows, IDialogService<DependenciesViewModel> dialog)
		{
			_windows = windows;
			_filler = new FillerBuilder(_windows, dialog);
		}

		public IMainBuilder SetSecondTab()
		{
			_openCommand = new RelayCommand(
				argument => { _viewModel.SetTab(1) }
			);
			return this;
		}

		public IMainBuilder SetFirstTab()
		{
			_firstTab = new RelayCommand(
				argument => { _viewModel.SetTab(0); }
			);
			return this;
		}
		
		public IMainBuilder Reset()
		{
			_viewModel = null;
			_firstTab = null;
			_secondTab = null;
			_filler.Reset();
			return this;
		}

		public MainViewModel Build()
		{
			_viewModel = new MainViewModel
			{
				Data = _data,
				AddInformation = _addInformation,
				DropInformation = _dropInformation,
			};
			return _viewModel;
		}
	}
}
