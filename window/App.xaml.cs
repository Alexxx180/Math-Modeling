using System.Windows;
using MathWindow.View;
using MathWindow.ViewModel.Components;
using MathWindow.ViewModel.Components.Data.Adapter;

namespace MathWindow
{
	/// <summary> Interaction logic for App.xaml </summary>
	public partial class App : Application
	{
		private async void OnStartup(object sender, StartupEventArgs e)
		{
			ScriptAdapter adapter = new ScriptAdapter();
			IWindowService windows = new WindowService();
			await adapter.Connect();
			MainViewModel viewModel = adapter.Model;
			windows.ShowWindow(viewModel);
		}
	}
}
