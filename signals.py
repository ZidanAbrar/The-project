from django.db.models.signals import post_save
from django.dispatch import receiver
from comment.models import Comment


@receiver(post_save, sender=Comment)
def update_points_on_comment(sender, instance, created, **kwargs):
    if created:
        user = instance.user
        # Check if the user exists in the points table
        points, created = Points.objects.get_or_create(user=user)
        # Increment the comment count
        points.comment_count += 1
        points.save()
