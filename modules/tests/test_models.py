from mixer.backend.django import mixer
import pytest
from modules.models import Module


@pytest.mark.django_db
class TestModels:
    def test_modules_is_image_uploaded(self):
        module = mixer.blend(Module,image = 'media/images/test_image.jpeg' )
        assert module.is_image_uploaded == True
        
    def test_modules_is_image_not_uploaded(self):
        module = mixer.blend(Module,image = None)
        assert module.is_image_uploaded == False   