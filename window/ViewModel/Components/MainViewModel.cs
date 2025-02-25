using System.Linq;
using System.Windows.Input;
using System.Collections.ObjectModel;

namespace MathWindow.ViewModel.Components
{
	public class MainViewModel : NotifyPropertyChanged
	{
		public MainViewModel() {}

		public ObservableCollection<FileViewModel> Data { get; set; }
	}
}
