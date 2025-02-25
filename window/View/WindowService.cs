namespace MathWindow.View
{
    internal class WindowService : IWindowService
    {
        public void ShowWindow(object viewModel)
        {
            EditorWindow window = new EditorWindow()
            {
                Content = viewModel,
            };
            window.Show();
        }
    }
}
