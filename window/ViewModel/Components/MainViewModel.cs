using System.Windows.Input;

namespace WisdomLight.ViewModel.Components
{
	public class MainViewModel : NotifyPropertyChanged
	{
		public MainViewModel() {}

		public ObservableCollection<FileViewModel> Data { get; set; }
	}
}
