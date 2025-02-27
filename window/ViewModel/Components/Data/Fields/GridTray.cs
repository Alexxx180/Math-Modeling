using System.Collections.Generic;
using System.Collections.ObjectModel;

namespace MathWindow.ViewModel.Components.Data.Fields
{
	public class GridTray
	{
		public string q1 { get; set; }
		public string q2 { get; set; }
		public string q3 { get; set; }
		public string q4 { get; set; }
		public string q5 { get; set; }
		public string q6 { get; set; }
		public string q7 { get; set; }
		public string q8 { get; set; }
		public string q9 { get; set; }
		public string q10 { get; set; }

		public GridTray(List<string> q)
		{
			q1 = q[0];
			q2 = q[1];
			q3 = q[2];
			q4 = q[3];
			q5 = q[4];
			q6 = q[5];
			q7 = q[6];
			q8 = q[7];
			q9 = q[8];
			q10 = q[9];
		}
	}
}
