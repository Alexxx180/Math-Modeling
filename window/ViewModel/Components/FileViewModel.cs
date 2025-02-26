using System;
using System.Linq;
using System.Collections.ObjectModel;
using MathWindow.ViewModel.Components.Data;
using MathWindow.ViewModel.Components.Data.Fields;

namespace MathWindow.ViewModel.Components
{
	public class FileViewModel : NotifyPropertyChanged
	{
		public FileViewModel() {}
		public FileViewModel(string config) {
			Width = Convert.ToInt32(Defaults.GetLines(config).First());
		}

		public static FileViewModel Default = new FileViewModel
		{
			Data = new TemplateViewModel
			{
				Calculus = new ObservableCollection<NumberExpression>
				{
					NumberExpression.Default
				},
				Data = ListExpression.Default,
				Result = GridExpression.Default,
			}
		};

		public TemplateViewModel Data { get; set; }
		public int Width { get; set; }
	}
}
