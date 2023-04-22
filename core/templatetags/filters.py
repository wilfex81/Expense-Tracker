from django import template
from datetime import date
from datetime import datetime

register = template.Library()

@register.filter
def filter_by_week_num(categories, current_week_num_str):
    current_week_num = datetime.strptime(current_week_num_str, '%B %d, %Y, %I:%M %p')
    current_year = current_week_num.year
    filtered_categories = categories.filter(
        budget_date__week=current_week_num.isocalendar()[1],
        budget_date__year=current_year)
    return filtered_categories
