from __future__ import unicode_literals

from django.db import models
from django.utils import timezone


class ToDoList(models.Model):
	HIGH = 'H'
	MEDIUM = 'M'
	LOW ='L'
	PRIORITY_CHOICES = (
		(HIGH, 'High'),
		(LOW, 'Low'),
		(MEDIUM, 'Medium'),
		)
	
	todo_task_id = models.AutoField(primary_key=True, unique=True)
	title = models.CharField(max_length=200, blank=True, null=True)
	todo_task = models.TextField()
	created_datetime = models.DateTimeField(
            default=timezone.now)
	last_edited_datetime = models.DateTimeField(
            default=timezone.now)
	is_completed = models.BooleanField(default=False)
	priority = models.CharField(max_length=1, choices = PRIORITY_CHOICES, 
									default = MEDIUM,
								)