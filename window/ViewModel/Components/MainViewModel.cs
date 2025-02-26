using System.Linq;
using System.Windows.Input;
using System.Collections.ObjectModel;

namespace MathWindow.ViewModel.Components
{
	public class MainViewModel : NotifyPropertyChanged
	{
		public MainViewModel() {
			Table = FileViewModel.Default;
			Model = FileViewModel.Default;
		}

		public FileViewModel Table { get; set; }
		public FileViewModel Model { get; set; }
	}
}
