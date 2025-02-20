namespace WisdomLight.ViewModel.Components.Data.Fields
{
    public class NumberExpression : NameLabel
    {
		public NumberExpression() {}
		public NumberExpression(string name, string no)
		{
			Name = name;
			No = no;
		}

        private string _no;
        public string No
        {
            get => _no;
            set
            {
                _no = value;
                OnPropertyChanged();
                OnPropertyChanged(nameof(Value));
            }
        }

		public static NumberExpression Default = new NumberExpression("N/A", "N/A");
    }
}
