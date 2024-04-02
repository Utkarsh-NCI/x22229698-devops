from django.urls import reverse, resolve
class TestUrls:
    def test_index_view(self):
        path = reverse('modules:index', kwargs={})
        assert resolve(path).view_name == 'modules:index'
    def test_feedback_view(self):
        path = reverse('modules:feedback', kwargs={})
        assert resolve(path).view_name == 'modules:feedback'
    def test_module_url(self):
        path = reverse('modules:module', kwargs={'module_id':1})
        assert path == '/module/1/'     