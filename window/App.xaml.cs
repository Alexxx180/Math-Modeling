using System.Windows;
using WisdomLight.View;
using WisdomLight.ViewModel.Components;

namespace WisdomLight
{
	/// <summary>
	/// Interaction logic for App.xaml
	/// </summary>
	public partial class App : Application
	{
		private void OnStartup(object sender, StartupEventArgs e)
		{
			IWindowService windows = new WindowService();
			MainViewModel viewModel = new MainViewModel();
			windows.ShowWindow(viewModel);
		}
	}
}
