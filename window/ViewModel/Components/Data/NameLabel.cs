namespace MathWindow.ViewModel.Components.Data
{
	public class NameLabel : NotifyPropertyChanged
	{
		private string _name;
		public string Name
		{
			get => _name;
			set
			{
				_name = value;
				OnPropertyChanged();
			}
		}
	}
}
