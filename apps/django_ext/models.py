from stories.models import Story
from categories import register_m2m, register_fk

register_m2m(Story)#, extra_params={'through':'StoryCategories'})
register_fk(Story, extra_params={'related_name':'primary_category'})