using System;
using System.Linq;
using System.Collections.ObjectModel;
using WisdomLight.ViewModel.Components.Data;
using WisdomLight.ViewModel.Components.Data.Fields;

namespace WisdomLight.ViewModel.Components
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
				Calculus = new ObservableCollection<NumberExpression>(),
				Data = ListExpression.Default,
				Result = GridExpression.Default,
			}
		};

		public TemplateViewModel Data { get; set; }
		public int Width { get; set; }
	}
}
