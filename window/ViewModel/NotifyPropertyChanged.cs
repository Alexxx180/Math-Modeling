﻿using System.ComponentModel;
using System.Runtime.CompilerServices;

namespace MathWindow.ViewModel
{
	public class NotifyPropertyChanged : INotifyPropertyChanged
	{
		#region INotifyPropertyChanged Members
		public event PropertyChangedEventHandler PropertyChanged;

		/// <summary> Raises this object's PropertyChanged event. </summary>
		/// <param name="propertyName">The property with a new value.</param>
		protected void OnPropertyChanged([CallerMemberName] string propertyName = null)
		{
			PropertyChangedEventHandler handler = PropertyChanged;
			if (handler != null)
			{
				PropertyChangedEventArgs e = new PropertyChangedEventArgs(propertyName);
				handler(this, e);
			}
		}
		#endregion
	}
}
