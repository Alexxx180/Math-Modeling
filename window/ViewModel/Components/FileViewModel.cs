using System.Windows.Input;
using WisdomLight.ViewModel.Components.Data;
using WisdomLight.ViewModel.Components.Building.Bank;
using static WisdomLight.ViewModel.Components.Building.Bank.Defaults;

namespace WisdomLight.ViewModel.Components
{
	public class FileViewModel : NotifyPropertyChanged
	{
		public FileViewModel(string config) {
			Width = (int)GetLines(config).First();
		}

		public TemplateViewModel Data { get; set; }
		public int Width { get; set; }
	}
}
