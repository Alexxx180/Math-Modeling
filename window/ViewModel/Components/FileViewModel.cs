using System.Windows.Input;
using WisdomLight.ViewModel.Components.Data;
using WisdomLight.ViewModel.Components.Building.Bank;

namespace WisdomLight.ViewModel.Components
{
	public class FileViewModel : NotifyPropertyChanged
	{
		public FileViewModel() { }

		public void Sync() {
			string[] lines = $"{Runtime}/fields.txt";
			foreach(string line in lines) {
				
			}
		}

		public void Submit() {
			
		}

		public ICommand SyncCommand { get; protected internal set; }
		public ICommand SubmitCommand { get; protected internal set; }

		public TemplateViewModel Data { get; set; }
		public int Width { get; set; }
	}
}
