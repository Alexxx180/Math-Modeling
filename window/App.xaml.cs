using System.Windows;
using MathWindow.View;
using MathWindow.ViewModel.Components;

namespace MathWindow
{
	/// <summary>
	/// Interaction logic for App.xaml
	/// </summary>
	public partial class App : Application
	{
		private void OnStartup(object sender, StartupEventArgs e)
		{
			System.Console.WriteLine("INIT");
			// /*
			IWindowService windows = new WindowService();
			MainViewModel viewModel = new MainViewModel();
			System.Console.WriteLine("VIEW MODEL INIT");
			windows.ShowWindow(viewModel);
			// */ return;
		}
	}
}
