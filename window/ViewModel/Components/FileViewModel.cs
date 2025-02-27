using System;
using System.Linq;
using System.Collections.ObjectModel;
using MathWindow.ViewModel.Components.Data;
using MathWindow.ViewModel.Components.Data.Fields;

namespace MathWindow.ViewModel.Components
{
	public class FileViewModel : NotifyPropertyChanged
	{
		public FileViewModel() {
			// Width = Defaults.Config.Margin.Overall;
		}

		public static FileViewModel Default = new FileViewModel
		{
			Data = new TemplateViewModel
			{
				Calculus = new ObservableCollection<NumberExpression>
				{
					NumberExpression.Default
				},
				Data = new ObservableCollection<ListExpression>
				{
					ListExpression.Default
				},
				Result = new ObservableCollection<GridExpression>
				{
					GridExpression.Default,
				}
			}
		};

		public TemplateViewModel Data { get; set; }
		public int Width { get; set; }
	}
}
