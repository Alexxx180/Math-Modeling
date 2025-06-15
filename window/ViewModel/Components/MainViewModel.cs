using System.Linq;
using System.Windows.Input;
using System.Collections.ObjectModel;

namespace MathWindow.ViewModel.Components
{
	public class MainViewModel : NotifyPropertyChanged
	{
		public static MainViewModel Default
		{
			get
			{
				return new MainViewModel
				{
					Table = FileViewModel.Default,
					Model = FileViewModel.Default,
                    Evenly = FileViewModel.Default,
                };
			}
		}

		public FileViewModel Table { get; set; }
		public FileViewModel Model { get; set; }
        public FileViewModel Evenly { get; set; }
    }
}
