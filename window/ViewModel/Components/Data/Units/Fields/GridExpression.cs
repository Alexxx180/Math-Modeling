namespace WisdomLight.ViewModel.Components.Data.Units.Fields
{
    public class GridExpression : TypeLabel, IExpression
    {
		public GridExpression() {}

		public GridExpression(string name, ObservableCollection<List<string>> no)
		{
			Name = name;
			No = no;
		}

		private ObservableCollection<List<string>> _no;
		public ObservableCollection<List<string>> No
		{
			get => _no;
			set
			{
				_no = value;
				OnPropertyChanged();
			}
		}

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

        public string Value => No.ToString();

        public IExpression Clone()
        {
            return new GridExpression
            {
                Name = Name,
                No = No,
                Type = Type
            };
        }

        public override bool Equals(object obj)
        {
            if (obj == null)
                return false;

            if (obj is not IExpression textObj)
                return false;
            else
                return Equals(textObj);
        }

        public bool Equals(IExpression other)
        {
            if (other == null)
                return false;

            return Name == other.Name &&
                Value == other.Value &&
                Type == other.Type;
        }

        public override int GetHashCode()
        {
            return base.GetHashCode();
        }
    }
}
