using System;
using WisdomLight.Model;

namespace WisdomLight.ViewModel.Components.Data.Units.Fields
{
    public interface IExpression
    {
        public string Name { get; set; }
        public string Value { get; }
        public string Type { get; set; }
    }
}
