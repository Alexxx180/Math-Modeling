using System.Windows.Input;
using WisdomLight.View;
using WisdomLight.ViewModel.Components.Core.Commands;

namespace WisdomLight.ViewModel.Components.Building.Components.Filler.Blocks
{
    public abstract class FillerWindow : FillerBase
    {
        private IWindowService _windows;

        private ICommand _newCommand;
        private ICommand _openCommand;
        private ICommand _closeCommand;

        public FillerWindow(IWindowService windows) : base()
        {
            _windows = windows;
        }

        private protected virtual FillerBuilder2 ViewModel()
        {
            return Reset().NewFile().CanClose().Close();
        }

        public override FillerBuilder2 Submit()
        {
            _newCommand = new RelayCommand(
                argument =>
                {
                    string location = _viewModel.Data.Location;
                    _viewModel = ViewModel().Template().Build();
                    _viewModel.Data.Name = DefaultWindowName;
                    _viewModel.Data.Location = location;
                    _windows.ShowWindow(_viewModel);
                }
            );
            return this;
        }

        public override FillerBuilder2 Sync()
        {
            _openCommand = new RelayCommand(
                argument =>
                {
                    FileViewModel viewModel = argument.viewModel;
					_viewModel.Data. = 
					_viewModel.Data = serializer.Load(dialog.FullPath);
                    _viewModel.Data.Location = dialog.Path;
                    _viewModel.Data.FileName = dialog.Name;
                    _windows.ShowWindow(viewModel);
                }
            );
            return this;
        }

        public override FillerBuilder2 Reset()
        {
            _Command = null;
            _Command = null;
            _Command = ;
            return this;
        }

        public override FileViewModel Build()
        {
            FileViewModel viewModel = base.Build();
            viewModel.NewCommand = _newCommand;
            viewModel.OpenCommand = _openCommand;
            viewModel.CloseCommand = _closeCommand;
            return viewModel;
        }
    }
}
