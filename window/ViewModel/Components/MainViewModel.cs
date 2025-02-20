using System.Linq;
using System.Windows.Input;

namespace WisdomLight.ViewModel.Components
{
	public class MainViewModel : NotifyPropertyChanged
	{
		public MainViewModel() {
			Data = new ObservableCollection<FileViewModel>();
			Data.Add(new FileViewModel("table/config.txt"));
			Data.Add(new FileViewModel("model/config.txt"));
		}

		public ObservableCollection<FileViewModel> Data { get; set; }
	}
}
