using MathWindow.ViewModel.Config;
using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace MathWindow.ViewModel.Components
{
    public class NormalViewModel
    {


        public int Width { get; set; }
        public ConfigFonts Fonts => Defaults.Config.Fonts;
        public ConfigColors Colors => Defaults.Config.Colors;
        public ConfigMargin Margin => Defaults.Config.Margin;
    }
}
